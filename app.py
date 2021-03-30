from flask import Flask, render_template, jsonify, request
import requests
from flask_cors import CORS
from random import *
import uuid

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/')


cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

user_dict = {}  # username:class<User>


class User:
    def __init__(self, ID):
        self.ID = ID
        self.name = None
        self.password = None


@app.route('/api/random')
def random_number():
    response = {
        'randomNumber': randint(1, 100)
    }
    return jsonify(response)


@app.route('/api/list/dynamic', methods=['GET'])
def msg_load_dynamic():
    print('msg_load_dynamic')
    lens = 25
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
            'postContent': 'Content{}'.format(i),
            'postSummer': 'Content{}'.format(i)
        }
        response['body']['content'].append(temp)
    response['body']['totalPages'] = '100'
    return jsonify(response)


@app.route('/api/list/export', methods=['GET'])
def msg_load_export():
    print('msg_load_export')
    lens = 25
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
    response['body']['totalPages'] = '100'
    return jsonify(response)


@app.route('/api/list/anls', methods=['GET'])
def msg_load_anls():
    print('msg_load_anls')
    print(user_dict)
    lens = 25
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
    response['body']['totalPages'] = '100'
    return jsonify(response)


@app.route('/api/user/login', methods=['POST'])
def user_login():
    post_data = request.get_json()
    print(post_data)
    response = {
        'code': 20000,
        'data': '8888',
    }
    if post_data['username'] in user_dict:
        if post_data['password'] == user_dict[post_data['username']].password:
            response['code'] = 20000
            response['data'] = user_dict[post_data['username']].ID
    else:
        new = User(uuid.uuid1())
        new.name = post_data['username']
        new.password = post_data['password']

        user_dict[new.name] = new
        response['code'] = 20000
        response['data'] = new.ID
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
    print(post_data)
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
