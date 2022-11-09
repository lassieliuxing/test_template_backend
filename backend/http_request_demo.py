from flask import Flask, request

from backend.log_util import logger

app = Flask(__name__)

@app.route("/testcase",methods=["get"])
def get_case():
    logger.info(f"请求参数为:{request.args}")
    result=request.args
    a=result.get("a")
    b=result.get("b")
    return{"code":0, "msg":"get success"}

@app.route("/testcase",methods=["post"])
def post_case():
    logger.info(f"获取参数为：{request.json}")
    return {"code":0,"msg":"post success"}
# 注册，用户名，密码，邮箱
@app.route("/testcase",methods=["put"])
def put_case():
    name=request.form.get("name")
    password=request.form.get("password")
    password_confirm=request.form.get("password_confirm")
    email=request.form.get("email")
    logger.info(request.form)
    logger.info(f"注册的用户信息为：name:{name},password:{password},password_confirm:{password_confirm},email:{email}")
    return {"code":0,"msg":"put success"}
@app.route("/file",methods=["post"])
def more_case():
    fileobj=request.files.get("file")
    logger.info(fileobj)
    filename=fileobj.filename
    logger.info(f"文件名为：{filename}")
    # fileobj.save("./logo1.png")
    return {"code":0,"msg":"post success"}
if __name__ == '__main__':
    app.run()