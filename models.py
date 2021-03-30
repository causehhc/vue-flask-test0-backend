from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

# 生成一个SQLORM基类，创建表必须继承他，别问我啥意思就是这么规定的
Base = declarative_base()


class M_Info(Base):
    __tablename__ = 'info'
    iid = Column(String(255), primary_key=True)
    sid = Column(String(255))
    ititle = Column(Text())
    ilink = Column(Text())
    isummer = Column(Text())
    iupdated = Column(String(255))


class M_User(Base):
    __tablename__ = 'user'
    uid = Column(String(255), primary_key=True)
    uname = Column(String(255))
    upassword = Column(String(255))


class M_Src(Base):
    __tablename__ = 'src'
    sid = Column(String(255), primary_key=True)
    sname = Column(String(255))
    surl = Column(String(255))
    supdated = Column(String(255))


class M_UtI(Base):
    __tablename__ = 'usertoinfo'
    id = Column(String(255), primary_key=True)
    uid = Column(String(255))
    iid = Column(String(255))


class M_UtS(Base):
    __tablename__ = 'usertosrc'
    id = Column(String(255), primary_key=True)
    uid = Column(String(255))
    sid = Column(String(255))


class M_UtU(Base):
    __tablename__ = 'usertouser'
    id = Column(String(255), primary_key=True)
    uid = Column(String(255))
    uidshost = Column(String(255))
