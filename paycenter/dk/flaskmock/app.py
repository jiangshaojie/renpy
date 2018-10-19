from flask import Flask
from flask import request
# from flask import Request
app = Flask(__name__)
import json

@app.route('/test',methods=['post','get'])
def hello_world():

    print("*******开始********")
    # if request.headers['Content-Type']=='application/json':
    #     print("request :",json.loads(request.data))
    # else:
    #     pass
    print(request.url)
    print("args   :",request.args)
    print("请求方法",request.method)
    print(request.form)
    print(request.data)


    print("********结束*******")
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8090, debug=True)
