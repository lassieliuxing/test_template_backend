from flask import Flask, jsonify, render_template, make_response

app=Flask(__name__)

@app.route('/text')
def get_text():
    return '返回文本'
@app.route('/huoge')
def tuple_res():
    return '返回元组',{"hahah":"xixixi"}
@app.route('/dict')
def get_dict():
    return {"status":0}
@app.route('/json')
def get_json():
    return jsonify({"status":0})
@app.route('/json1')
def get_json1():
    return jsonify(status=1,name="heheheh")
@app.route('/')
def index():
    resp=make_response(render_template('demo.html'))
    # 设置cookie
    resp.set_cookie('username','the username')
    # 设置响应头信息
    resp.headers["haha"]="xixixhshajsh"
    return resp
if __name__ == '__main__':
    app.run()
    # app.run(host="0.0.0.0",port=5000,debug=True)