import os
from flask import Flask,redirect

app = Flask(_name_)

@app.route('/')
def hello():
    return redirect("http://3a0bb3ec3b83.ngrok.io", code=302)

if _name_ == '_main_':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run()
