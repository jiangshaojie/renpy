from flask import Flask
from flask import request
app = Flask(__name__)


@app.route('/test',methods=['post','get'])
def hello_world():
    a=request.headers
    # print(request.url)
    print(request.args)
    print(request.data)
    print(request.form)

    # print(type(a))
    for items in a:
        print(items)
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8090, debug=True)
