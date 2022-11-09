from flask import Flask, request
from flask_restx import Resource, Api, Namespace, fields

from backend.log_util import logger

app = Flask(__name__)
# 通过api创建api实例
api = Api(app,version="2.0")
# 定义两个命名空间
hello_ns=Namespace("demo",description="demo学习")
case_ns=Namespace("case",description="用例管理")
# 使用api添加路由
# 多个路由，就有多种访问方式
# 将@api.route('/case')方式更改为 @case_ns.route("")
# @case_ns.route("/case"),定义子路由
@case_ns.route("/case")
# 类要继承resource模块
class Testcase(Resource):
    # restful风格的get方法
    # 方法中编辑业务逻辑
    @hello_ns.doc(params={'id':'An ID'})
    def get(self):
        return {"code":0,"msg":"get success"}

    post_model=api.model('PostModel',{
        # required为约束是否为必填项
        'name':fields.String(discriminator='The name',required=True),
        # enum枚举类型，只能选一个
        'type':fields.String(discriminator='The object type',enum=['A','B']),
        # min允许最小值为0
        'age':fields.Integer(min=0),
    })
    @hello_ns.doc(body=post_model)
    def post(self):
        return {"code":0,"msg":"post success"}
    def put(self):
        return {"code":0,"msg":"put  success"}
    def delete(self):
        return {"code":0,"msg":"delete success"}

@hello_ns.route("")
class Demo(Resource):
    # 方法中编辑业务逻辑
    # 定义parser解析器解析对象
    get_parser=api.parser()
    # 通过parser对象添加成测试数据  location的值是在request.arges中使用
    get_parser.add_argument('id',type=int,location="args")

    @hello_ns.expect(get_parser)
    # restful风格的get方法
    def get(self):
        logger.info(f"request.args{request.args}")
        return {"code":0,"msg":"get success"}

    post_parser=api.parser()
    post_parser.add_argument("id",type=int,location="json",required=True)
    post_parser.add_argument("casetitle",type=str,location="json",required=True)
    @hello_ns.expect(post_parser)
    def post(self):
        logger.info(f"request.json==={request.json}")
        return {"code":0,"msg":"post success"}
    def put(self):
        return {"code":0,"msg":"put  success"}
    def delete(self):
        return {"code":0,"msg":"delete success"}
# 通过api把命名空间添加进去
api.add_namespace(hello_ns,'/hello')
api.add_namespace(case_ns,'/case')
if __name__ == '__main__':
    app.run(debug=True)