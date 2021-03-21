from flask import Flask, render_template, jsonify
import requests
from flask_cors import CORS
from random import *

app = Flask(__name__, template_folder='../dist', static_folder='../dist/static')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

lens = 10
items = {
        'body': {
            'content': [],
            'totalPages': '',
        }
    }
for i in range(lens):
    temp = {
            "postTitle": 'Title{}'.format(i),
            'postContent': 'Content{}'.format(i)
        }
    items['body']['content'].append(temp)
items['body']['totalPages'] = '5'


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/api/info')
def msg_load():
    # global idx
    response = items
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
