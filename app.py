import os
from flask import Flask,redirect

app = Flask(_name_)

@app.route('/')
def hello():
    return redirect("http://10357c3651c3.ngrok.io", code=302)

if _name_ == '_main_':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run()
