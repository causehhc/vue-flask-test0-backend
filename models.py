from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

# 生成一个SQLORM基类，创建表必须继承他，别问我啥意思就是这么规定的
Base = declarative_base()


class M_Info(Base):
    __tablename__ = 'info'
    iid = Column(String(190), primary_key=True)
    sid = Column(String(190))
    ititle = Column(Text())
    ilink = Column(Text())
    isummer = Column(Text())
    iupdated = Column(String(190))
    ilikes = Column(String(190))


class M_User(Base):
    __tablename__ = 'user'
    uid = Column(String(190), primary_key=True)
    uname = Column(String(190))
    upassword = Column(String(190))


class M_Src(Base):
    __tablename__ = 'src'
    sid = Column(String(190), primary_key=True)
    sname = Column(String(190))
    surl = Column(String(190))
    supdated = Column(String(190))
    ssummer = Column(String(190))


class M_UtI(Base):
    __tablename__ = 'usertoinfo'
    id = Column(String(190), primary_key=True)
    uid = Column(String(190))
    iid = Column(String(190))


class M_UtS(Base):
    __tablename__ = 'usertosrc'
    id = Column(String(190), primary_key=True)
    uid = Column(String(190))
    sid = Column(String(190))


class M_UtU(Base):
    __tablename__ = 'usertouser'
    id = Column(String(190), primary_key=True)
    uid = Column(String(190))
    uidshost = Column(String(190))


class M_Loginlog(Base):
    __tablename__ = 'loginlog'
    id = Column(String(190), primary_key=True)
    ip = Column(String(190))
    name = Column(String(190))
    password = Column(String(190))
    date = Column(String(190))
