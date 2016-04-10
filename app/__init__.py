# -*- coding: utf-8 -*-
# Import flask and template operators
import os
from flask import Flask, render_template
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
from views.share import share
app.register_blueprint(share, url_prefix=None)

# Build the database:
db.create_all()
