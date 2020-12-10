from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response, Response
from flask_dance.contrib.github import make_github_blueprint, github
import io
import cv2
import os 
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(_name_, static_folder='static')
app.config["SECRET_KEY"]="secretkey"
vc = cv2.VideoCapture(0)


github_blueprint = make_github_blueprint(client_id='69149c692d8813491c06',
                                         client_secret='3f0a6bfc6363d32acced4f2737a4f4c84d0e8888')

app.register_blueprint(github_blueprint, url_prefix='/github_login')


@app.route('/')
def github_login():

    if not github.authorized:
        return redirect(url_for('github.login'))
    else:
        account_info = github.get('/user')
        if account_info.ok:
            account_info_json = account_info.json()
            return render_template('index.html')

    return '<h1>Request failed!</h1>'


def gen():
    """Video streaming generator function."""
    while True:
        read_return_code, frame = vc.read()
        encode_return_code, image_buffer = cv2.imencode('.jpg', frame)
        io_buf = io.BytesIO(image_buffer)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + io_buf.read() + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(
        gen(),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


if _name_ == "_main_":
    #app.run(debug=True)
    app.run(host="0.0.0.0", port=8080)
