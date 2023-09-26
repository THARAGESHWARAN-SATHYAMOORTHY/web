from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def start():
    return "Hello !!! \n Welcome You all!!!"

@app.route('/json')
def js():
    return jsonify({'result':'success'})

@app.route('/para/<string:a>', methods=['GET'])
def para(a):
    return f'{a} is the passed string'

@app.route('/getm')
def getm():
    name = request.args.get('name')
    age = request.args.get('age')
    return f'{name} is {age} years old'
    
@app.route('/postm',methods=['POST'])
def postm():
    data = request.get_json()
    res = data['a'] + data['b']
    return jsonify({'res':res})

if __name__ == '__main__':
    app.run(host='192.168.56.1')
    