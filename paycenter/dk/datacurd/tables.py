#coding:utf-8
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class dk_biz(Base):
    # 表的名字:
    __tablename__ = 'dk_biz'

    # 表的结构:
    id = Column('id',Integer,primary_key=True)
    ucid = Column('ucid',String(20))
    order_no=Column('order_no',String(20))

# 初始化数据库连接:
engine = create_engine('mysql+mysqlconnector://work:RqQb5YFfOH5ojZ16@rdsqv39909q66i6efi0k.mysql.rds.aliyuncs.com:3306/paycenter')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

dkbiz=dk_biz('20181012144311297000008352059823')



# 创建Session:
session = DBSession()
# 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
user = session.query(dkbiz).filter(dkbiz.order_no=='20181012144311297000008352059823')
# 打印类型和对象的name属性:
print('type:', type(user))
print('name:', user.ucid)
# 关闭Session:
session.close()
