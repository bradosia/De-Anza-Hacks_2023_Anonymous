import os
from flask import Flask, request, url_for, render_template, redirect

app = Flask(__name__)
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


if __name__ == "__main__":
    app.run()