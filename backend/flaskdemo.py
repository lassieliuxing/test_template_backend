import logging

from flask import Flask

# 创建flask应用程序实例
from backend.log_util import logger
# 创建flask实例
app = Flask(__name__)
# 添加路由
@app.route("/userinfo/<string:username>")
def hello_world(username):
    logger.info("这是")
    return f"<p>Hello,{username} World!</p>"
@app.route("/")
def hi():
    return "hahaha"

# # 启动入口
if __name__ == '__main__':
    # flask服务启动起来
    # 轮询等待方式，等待浏览器发来请求
    # 会一直接受请求
    app.run()
