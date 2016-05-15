from flask import session, render_template, redirect, url_for
from flask.ext.api import status
from app import app

from manage import manage
from share import share
from chat import chat


app.register_blueprint(manage, url_prefix='/manage')
app.register_blueprint(share, url_prefix='/share')
app.register_blueprint(chat, url_prefix='/chat')

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), status.HTTP_404_NOT_FOUND


# Index Page
@app.route('/')
def index():
    return redirect(url_for('view_manage.index'))
