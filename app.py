import req
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    return "<p> Req app While Loop ... </p>"
app.run(port=7788,host='0.0.0.0')
