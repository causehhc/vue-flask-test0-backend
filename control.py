import datetime
import uuid

import feedparser
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *


class SqlHandler:
    def __init__(self, user, passwd, host, name):
        engine = create_engine("mysql+pymysql://{}:{}@{}:3306/{}?charset=utf8mb4".format(user, passwd, host, name))
        DBSession = sessionmaker(bind=engine)
        self._sess = DBSession()

    def get_sess(self):
        return self._sess

    def src_addTitle(self, src_list):
        for src in src_list:
            if len(self._sess.query(M_Src).filter(M_Src.sname == src[0]).all()) != 0:
                print('insert fail! exists: {}'.format(src[0]))
            else:
                new_src = M_Src(sid=str(uuid.uuid1()),
                                sname=src[0],
                                surl=src[1],
                                supdated='2020')
                self._sess.add(new_src)
                print('insert finished! exists: {}'.format(src[0]))
        # 提交即保存到数据库
        self._sess.commit()

    def info_reflashAll(self, src_name_list=None, all_force=False):
        update_num = {}  # (src.stitle - cnt) 每个源更新的条目数量
        src_item_list = []  # 根据src更新对应info

        if src_name_list is not None:
            for src_name in src_name_list:
                src_item_list.append(self._sess.query(M_Src).filter(M_Src.sname == src_name).one())
        else:
            src_item_list = self._sess.query(M_Src).all()
        print('({}) src loaded...'.format(len(src_item_list)))

        for src_item in src_item_list:
            # 获取当前更新时间
            print('Requesting for feedparser: {}'.format(src_item.sname))
            RSS_dict = feedparser.parse(src_item.surl)
            if 'updated' in RSS_dict['feed']:
                updated_now = RSS_dict['feed']['updated']
            else:
                updated_now = 'no val'
            updated_local = src_item.supdated
            if (updated_now != 'no val' and updated_local != updated_now) or all_force:
                # 刷新src中的更新时间
                src_item.supdated = updated_now
                # 添加info中的条目
                add_cnt = 0
                for entry in RSS_dict['entries']:
                    ITitle = entry['title']
                    ILink = entry['link']
                    ISummer = entry['summary']
                    IUpdated = datetime.datetime.now().strftime('%Y_%m_%d-%H:%M')
                    if len(self._sess.query(M_Info).filter(M_Info.ititle == ITitle).all()) != 0:
                        print('update fail! is exists: {}'.format(ITitle))
                    else:
                        new_info = M_Info(iid=str(uuid.uuid1()),
                                          sid=src_item.sid,
                                          ititle=ITitle,
                                          ilink=ILink,
                                          isummer=ISummer,
                                          iupdated=IUpdated)
                        self._sess.add(new_info)
                        add_cnt += 1
                        print('update finished! add exists: {}'.format(ITitle))
                update_num[src_item.sname] = add_cnt
                print('one update: {}'.format(src_item.sname))
            else:
                print('updated fail! now not updated: {}'.format(src_item.sname))
        # 提交即保存到数据库
        self._sess.commit()
        print('check finished!')

        return update_num


def main():
    # sql = SqlHandler('root', 'password', 'localhost', 'hhctest')
    sql = SqlHandler('root', 'xld123456XLD', '192.168.2.174', 'hhctest')
    src_list = [
        ['BBC_News', 'http://feeds.bbci.co.uk/news/rss.xml'],
        ['Engadget', 'http://www.engadget.com/rss.xml'],
        ['Entrepreneur', 'http://feeds.feedburner.com/entrepreneur/latest'],
        ['Yanko_Design', 'http://www.yankodesign.com/feed/'],
        ['TEDTalks(video)', 'https://www.ted.com/feeds/talks.rss'],
        ['FAIL_Blog', 'http://feeds.feedburner.com/failblog'],
        ['github', 'https://github.com/guanguans/favorite-link/commits/master.atom']
    ]
    # sql.src_addTitle(src_list)
    sql.info_reflashAll(src_name_list=None, all_force=True)


if __name__ == '__main__':
    main()
