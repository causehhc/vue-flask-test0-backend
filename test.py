import time
from apscheduler.schedulers.background import BackgroundScheduler
from cache import RedisHelper
from cache import RedisHelper
from database import MySqlHelper
from models import *


if __name__ == '__main__':
    mysql = MySqlHelper('root', 'password', 'localhost', 'hhctest')
    # sql = SqlHandler('root', 'xld123456XLD', '192.168.2.174', 'hhctest')
    sess = mysql.get_db()

    user_src_list = sess.query(M_UtS).filter(M_UtS.uid == '49d007d8-9485-11eb-84f0-8c1645dc54e7').all()
    src_list = sess.query(M_Src).all()
    print(user_src_list)
    print(src_list)
