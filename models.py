from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text

# 生成一个SQLORM基类，创建表必须继承他，别问我啥意思就是这么规定的
Base = declarative_base()


# class M_Info(Base):
#     def __init__(self):
#         self.__tablename__ = 'info'
#         self.iid = Column(String(255), primary_key=True)
#         self.sid = Column(String(255))
#         self.ititle = Column(Text())
#         self.ilink = Column(Text())
#         self.isummary = Column(Text())
#         self.iupdated = Column(String(255))


class M_Info(Base):
    __tablename__ = 'info'
    iid = Column(String(255), primary_key=True)
    sid = Column(String(255))
    ititle = Column(Text())
    ilink = Column(Text())
    isummer = Column(Text())
    iupdated = Column(String(255))
