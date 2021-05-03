import redis
from models import *


class RedisHelper:
    def __init__(self):
        self.__REDIS_HOST = 'localhost'
        self.__REDIS_PORT = 6379
        self.__redis_pool = redis.ConnectionPool(host=self.__REDIS_HOST, port=self.__REDIS_PORT)
        self.__redis_conn = redis.Redis(connection_pool=self.__redis_pool)

    def reset_redis(self):
        self.__redis_conn.flushall()

    def add_likes(self, info_id):
        self.__redis_conn.incr(info_id, amount=1)

    def commit_to_sql(self, db):
        key_list = self.__redis_conn.keys()
        for key in key_list:
            val = self.__redis_conn.get(key)
            user_result = db.session.query(M_Info).filter_by(iid=key).first()
            # 更新字段名称
            tmp = user_result.ilikes
            user_result.ilikes = str(int(tmp) + int(val))
            print('commit', key, val)
            self.__redis_conn.delete(key)
        if len(key_list) != 0:
            # 提交即保存到数据库
            db.session.commit()
            print('commit ok')


if __name__ == '__main__':
    r = RedisHelper()
    while True:
        a = input()

        if a == '0':
            r.commit_to_sql()
        else:
            r.add_likes(a)
