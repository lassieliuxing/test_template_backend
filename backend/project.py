from flask import Flask, request
from flask_cors import CORS
from flask_restx import Resource, Api, Namespace
from flask_sqlalchemy import SQLAlchemy
import yaml
from sqlalchemy import *
from backend.log_util import logger

app = Flask(__name__)
CORS(app,supports_credentials=True)
api = Api(app)
# 用例的命名空间
case_ns = Namespace("case",description="项目管理")

@case_ns.route("")
class TestCaseServer(Resource):
    get_parser=api.parser()
    get_parser.add_argument("id",type=int,location="args")
    @case_ns.expect(get_parser)
    def get(self):
        """测试用例的查找"""
        case_id=request.args.get("id")
        logger.info(f"接收到的参数<===={case_id}")
        if case_id:
            case_data=TestCase.query.filter_by(id=case_id).first()
            if case_data:
                datas=[{"id":case_data.id,
                        "case_title":case_data.case_title,
                        "remark":case_data.remark}]
            else:
                datas=[]
        else:
            case_datas=TestCase.query.all()
            datas=[{"id":case_data.id,
                        "case_title":case_data.case_title,
                        "remark":case_data.remark}for case_data in case_datas]
        return datas
    post_pareser=api.parser()
    post_pareser.add_argument("id",type=int,required=True,location="json")
    post_pareser.add_argument("case_title",type=str,required=True,location="json")
    post_pareser.add_argument("remark",type=str,required=True,location="json")