from flask import Flask, session
from flask.ext.session import Session
import os

user = os.environ.get('user', None)
pwd = os.environ.get('dbpwd',None)
app = Flask(__name__)

# config
SESSION_TYPE = 'mongodb'
app.config.from_object(__name__)
Session(app)
SESSION_MONGODB('mongodb://'+user+':'+pwd+'@ds155325.mlab.com:55325/recipe_finder_users')
SESSION_MONGODB_DB('recipe_finder_users')
SESSION_MONGODB_COLLECT('users')

@app.route('/set/')
def set():
    session['key'] = 'value'
    return 'ok'

@app.route('/get/')
def get():
    return session.get('key', 'not set')