from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS
from random import *

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

user_lib = {'admin': '111111', '2': '2'}


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/api/list/info', methods=['GET'])
def msg_load():
    lens = 10
    response = {
        'code': 20000,
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
        response['body']['content'].append(temp)
    response['body']['totalPages'] = '5'
    return jsonify(response)


@app.route('/api/user/login', methods=['POST'])
def user_login():
    post_data = request.get_json()
    response = {
        'code': 0,
        'data': 'admin-token',
    }
    if post_data['username'] in user_lib:
        if post_data['password'] == user_lib[post_data['username']]:
            response['code'] = 20000
    return jsonify(response)


@app.route('/api/user/info', methods=['GET'])
def user_info():
    response = {
        'code': 20000,
        'data': 'admin-token',
    }
    return jsonify(response)


@app.route('/api/user/logout', methods=['POST'])
def user_logout():
    post_data = request.get_json()
    response = {
        'code': 20000,
        'data': 'success',
    }
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
