import os
from flask import Flask, request, url_for, render_template, redirect
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
application = app

@app.route('/',methods=['GET','POST'])
def my_maps():

  mapbox_access_token = os.environ.get("MAPBOX_ACCESS_TOKEN")

  return render_template('index.html',
        mapbox_access_token=mapbox_access_token)
        
@app.route("/api")
def hello():
    return "Hello World!"

@app.route("/<string:name>/")
def say_hello(name):
    return f"Hello {name}!"

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

if __name__ == "__main__":
    socketio.run(app)

