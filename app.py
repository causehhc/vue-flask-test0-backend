from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import uuid
from models import *
from control import SqlHandler

app = Flask(__name__,
            template_folder='../frontend/dist',
            static_folder='../frontend/dist/static')

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

sql = SqlHandler('root', 'password', 'localhost', 'hhctest')
# sql = SqlHandler('root', 'xld123456XLD', '192.168.2.174', 'hhctest')
sess = sql.get_sess()


@app.route('/api/list/dynamic', methods=['POST'])
def msg_load_dynamic():
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


@app.route('/api/list/export', methods=['POST'])
def msg_load_export():
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
    print('user_login')
    post_data = request.get_json()
    data_list = sess.query(M_User).filter(M_User.uname == post_data['username']).all()
    response = {
        'code': 0,
        'data': '',
    }
    if len(data_list) == 0:  # 注册
        temp_uid = uuid.uuid1()
        new_user = M_User(uid=temp_uid,
                          uname=post_data['username'],
                          upassword=post_data['password'])
        sess.add(new_user)
        sess.commit()
        response['code'] = 20000
        response['data'] = str(temp_uid)
    else:  # 已存在，验证密码
        if post_data['password'] == data_list[0].upassword:
            response['code'] = 20000
            response['data'] = str(data_list[0].uid)
    return jsonify(response)


@app.route('/api/user/info', methods=['GET'])
def user_info():
    print('user_info', request.values.get('token'))
    response = {
        'code': 20000,
        'data': 'admin-token2',
    }
    return jsonify(response)


@app.route('/api/user/logout', methods=['POST'])
def user_logout():
    print('user_logout')
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
