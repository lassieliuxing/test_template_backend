from flask import Flask, request
from flask_restx import Resource, Api, Namespace
from flask_sqlalchemy import SQLAlchemy
import yaml
from sqlalchemy import *
from backend.log_util import logger

app = Flask(__name__)
api = Api(app)
# 用例的命名空间
case_ns = Namespace("case",description="用例管理")

with open("./data.yml", encoding='UTF-8') as f:
    result = yaml.safe_load(f)
    username = result.get("database").get('username')
    password = result.get("database").get('password')
    server = result.get("database").get('server')
    db = result.get("database").get('db')

# 设置连接方法
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{server}/{db}?charset=utf8"
# 设置参数，不设置的时候会抛出异常
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.app_context().push()
# app与SQLAlchemy绑定
db = SQLAlchemy(app)

# 创建用例表
class TestCase(db.Model):
    __tablename__ = "testcase"
    id = db.Column(Integer, primary_key=True)
    case_title = db.Column(String(80), nullable=False, unique=True)
    remark = db.Column(String(120))
@case_ns.route("")
class TestCaseServer(Resource):
    def get(self):
        """测试用例的查找"""
        logger.info("get method")
        return {"code":0,"msg":"get success"}

    post_pareser=api.parser()
    post_pareser.add_argument("id",type=int,required=True,location="json")
    post_pareser.add_argument("case_title",type=str,required=True,location="json")
    post_pareser.add_argument("remark",type=str,required=True,location="json")
    @case_ns.expect(post_pareser)
    def post(self):
        """测试用例的新增"""
        logger.info("post method")
        case_data=request.json
        logger.info(f"接收到的参数<===={case_data}")
        case_id=case_data.get("id")
        # 查询数据库是否有记录
        exists=TestCase.query.filter_by(id=case_id).first()
        logger.info(f"查询表结果：{exists}")
        # 如果存在，不执行新增操作，返回40001错误码
        # 如果不存在，则增加这条记录到库中
        if not exists:
            testcase=TestCase(**case_data)
            db.session.add(testcase)
            db.session.commit()
            return {"code":0,"msg":f"case id {case_id} success add"}
        else:
            return {"code":40001,"msg":"case is existes"}

    def put(self):
        """测试用例的修改"""
        logger.info("put method")
        return {"code":0,"msg":"put success"}
    def delete(self):
        """测试用例的删除"""
        logger.info("delete method")
        return {"code":0,"msg":"delete success"}
api.add_namespace(case_ns,"/testcase")



if __name__ == '__main__':
    # db.drop_all()
    # db.create_all()
    app.run(debug=True)
