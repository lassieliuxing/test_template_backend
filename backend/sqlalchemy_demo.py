from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import yaml
from sqlalchemy import *
app=Flask(__name__)

with open("./data.yml")as f:
    result=yaml.safe_load(f)
    username=result.get("database").get('username')
    password=result.get("database").get('password')
    server=result.get("database").get('server')
    db=result.get("database").get('db')
    # 设置连接方法
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{server}:{db}?charset=utf8'
    # 设置参数，不设置的时候会抛出异常
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # app与SQLAlchemy绑定
    db = SQLAlchemy(app)
class User(db.Model):
    id=Column(Integer,primary_key=True)
    username=Column(String(80))


class Students(db.Model):
    id = Column(Integer, primary_key=True)
    username = Column(String(80))
    gender=Column(String(80))
if __name__ == '__main__':
    db.create_all()
    # # 删除表
    # db.drop_all()