# -*- coding: utf-8 -*-
# Import flask and template operators
import os
from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# config
app.config.from_object('config.DevelopmentConfig')

db = SQLAlchemy(app)


# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Register blueprint(s)
from app.mod_share.controllers import mod_share as share_module
app.register_blueprint(share_module)
# app.register_blueprint(xyz_module)

# Build the database:
db.create_all()
