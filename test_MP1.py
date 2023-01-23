from flask import Flask, url_for
from flask import request
from flask import Response
from flask import json
from flask import jsonify


num_val = 0

app = Flask(__name__)

@app.route('/', methods =['POST'])
def api_root():
    global num_val
    num_val=0
    if request.method == 'POST':
        num_val = request.json['num']
        return num_val


@app.route('/', methods =['GET'])
def api_root1():
    if request.method == 'GET':
        return str(num_val)
    
if __name__ == '__main__':
    app.run('0.0.0.0', port=80)
