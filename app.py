from flask import Flask, render_template, jsonify
import requests
from flask_cors import CORS
from random import *

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../dist/frontend/static')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

some_list = []
lens = 20
for i in range(lens):
    item = {
        'body': {
            'content': '',
            'totalPages': ''
        },
    }
    item['body']['content'] = 'page{}'.format(i)
    item['body']['totalPages'] = '{}'.format(lens)
    some_list.append(item)


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


idx = 0


@app.route('/api/info')
def msg_load():
    global idx
    response = some_list[idx]
    idx += 1
    if idx == len(some_list):
        idx = 0
    return jsonify(response)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    if app.debug:
        return requests.get('http://localhost:8080/{}'.format(path)).text
    return render_template("index.html")
    # return 'hello'


if __name__ == '__main__':
    app.run()
