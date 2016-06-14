from flask import session, render_template, redirect, url_for
from flask.ext.api import status
from app import app

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), status.HTTP_404_NOT_FOUND


# Index Page
@app.route('/')
def index():
    return render_template('index.html')


# Test file upload
@app.route('/share')
def share():
    return render_template('share.html')
