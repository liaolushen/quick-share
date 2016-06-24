# -*- coding: utf-8 -*-
import os
from flask import Blueprint, request, session, jsonify, send_from_directory
from flask.ext.api import status
from app import app, db
from app.models.share_mod import File, TmpFileMap
from app.common import api_format

share = Blueprint('api_share', __name__)

@share.route('/upload', methods=['GET', 'POST'])
def upload_file():
    """
    Handle the file upload

    Args:
        flowIdentifier: 文件的ID
        flowFilename: 文件的名字
        flowTotalSize: 文件的大小
        flowChunkNumber: 当前分片序号
        flowCurrentChunkSize: 当前分片的大小
        roomId: 当前房间的目录
    """
    if request.method == 'GET':
        if request.args.get('flowChunkNumber') == '1':
            tmp_file = TmpFileMap.query.get(request.args.get('flowIdentifier'))
            if not tmp_file:
                db.session.add(
                    TmpFileMap(
                        file_identifer=request.args.get('flowIdentifier'),
                        file_name=request.args.get('flowFilename'),
                        total_size=int(request.args.get('flowTotalSize')),
                        current_size=0,
                        current_chunk=0,
                        room_id=request.args.get('roomId'),
                    )
                )
                db.session.commit()
        return "Ready for content", status.HTTP_204_NO_CONTENT
    elif request.method == 'POST':
        file_chunk = request.files['file'].read()
        tmp_file = TmpFileMap.query.get(request.form['flowIdentifier'])
        if tmp_file.current_chunk + 1 == int(request.form['flowChunkNumber']):
            tmp_file.current_size += int(request.form['flowCurrentChunkSize'])
            tmp_file.current_chunk += 1
            with open(os.path.join(app.config['TMP_UPLOAD_FOLDER'],
                      request.form['flowIdentifier']), 'a') as f:
                f.write(file_chunk)
        if tmp_file.current_size == tmp_file.total_size:
            new_file = File(
                file_name=tmp_file.file_name,
                file_format=tmp_file.file_format,
                file_size=tmp_file.total_size,
                room_id=tmp_file.room_id
            )
            db.session.add(new_file)
            db.session.commit()
            os.rename(
                os.path.join(app.config['TMP_UPLOAD_FOLDER'], tmp_file.id),
                os.path.join(app.config['UPLOAD_FOLDER'], str(new_file.id)))
            db.session.delete(tmp_file)
        db.session.commit()
        print File.query.all()
        return "OK", status.HTTP_200_OK

@share.route('/download', methods=['GET'])
def download_file():
    file_id = request.values['file_id']
    result_file = File.query.get(int(file_id))
    if result_file is None:
        return jsonify(api_format(status.HTTP_404_NOT_FOUND, "No such file"))
    return send_from_directory(
        app.config['UPLOAD_FOLDER'],
        str(file_id),
        as_attachment=True,
        attachment_filename=result_file.file_name.encode('utf8'))

@share.route('/get-file-list', methods=['GET'])
def get_file_list():
    room_id = request.values['room_id']
    result_list = File.query.filter_by(room_id=room_id)
    file_list = []
    for file_item in result_list:
        file_list.append({
            'file_id': file_item.id,
            'file_name': file_item.file_name,
            'file_format': file_item.file_format,
            'file_size': file_item.file_size
        })
    return jsonify(api_format(status.HTTP_200_OK, "ok", {'room_id': room_id, 'file_list': file_list}))
