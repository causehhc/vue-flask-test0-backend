from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_paginate import Pagination

from models import M_Info

app = Flask(__name__, template_folder='../frontend/dist', static_folder='../frontend/dist/')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

engine = create_engine("mysql+pymysql://root:password@127.0.0.1:3306/hhctest?charset=utf8")
DBSession = sessionmaker(bind=engine)
sess = DBSession()


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
            'postContent': 'Content{}'.format(i)
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


@app.route('/api/list/anls', methods=['POST'])
def msg_load_anls():
    post_data = request.get_json()
    print('msg_load_anls', post_data)
    limit = 25
    start = post_data['count'] - 1
    end = start + limit
    data_list = sess.query(M_Info).slice(start, end).all()
    response = {
        'code': 20000,
        'body': {
            'content': [],
            'totalPages': '',
        }
    }
    for data in data_list:
        temp = {
            "postTitle": '{}'.format(data.ititle),
            'postContent': '{}'.format(data.isummer)
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
        'data': 'admin-token',
    }
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


if __name__ == '__main__':
    app.run()
