# -*- coding: utf-8 -*-
# Import flask and template operators
import os
from flask import Flask, render_template, redirect, request, url_for,\
                  session
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.api import status

# Define the WSGI application object
app = Flask(__name__)

# config
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), status.HTTP_404_NOT_FOUND


# Register blueprint(s)
from views.manage import manage
from views.share import share
from views.chat import chat
app.register_blueprint(manage, url_prefix='/manage')
app.register_blueprint(share, url_prefix='/share')
app.register_blueprint(chat, url_prefix='/chat')


# Index Page
@app.route('/')
def index():
    if 'manage_email' in session:
        return redirect(url_for('manage.index'))
    else:
        return redirect(url_for('manage.login'))


# Build the database:
db.create_all()
