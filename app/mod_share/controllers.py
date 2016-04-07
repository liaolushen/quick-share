# -*- coding: utf-8 -*-
from flask import Blueprint, request, render_template, redirect,\
                    url_for, current_app, session
import os
from models import File
from app import db
from helper.mod_share_helper import get_file_format, generate_random_hash,\
                                generate_file_id
mod_share = Blueprint('share', __name__, url_prefix=None)


@mod_share.route('/', methods=['GET'])
def index():
    return render_template("share/index.html")


@mod_share.route('/share-upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    if file:
        file_id = generate_file_id()
        hash_code = generate_random_hash()
        file_name = file.filename
        file_format = get_file_format(file_name)
        db.session().add(
            File(file_id, file_name, file_format, hash_code)
        )
        db.session().commit()
        file.save(os.path.join(
            current_app.config['UPLOAD_FOLDER'], hash_code))
        print File.query.all()
        return redirect('http://www.baidu.com')
    return redirect('/')
