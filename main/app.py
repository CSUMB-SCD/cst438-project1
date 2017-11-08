import os
from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@socketio.on('message')
def handleMessage(msg):
    send(msg, broadcast=True)
    print('Message: ' + str(msg)) #error happens here.
    
    
if __name__ == '__main__':
    socketio.run(app)
