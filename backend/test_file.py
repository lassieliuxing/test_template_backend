import requests

def test_file():
    # 模拟发送图片请求
    url="http://127.0.0.1:5000/file"
    # file={'file':open("C:/Users/打工人/Desktop/测试资料/图片/logo.jpg",'rb')}
    file={'file':open("./recource/test.jpg",'rb')}
    r=requests.post(url,files=file)
    assert r.status_code==200