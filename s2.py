from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def start():
    return "WELCOME!!!"

@app.route('/one')
def one():
    return jsonify({'result':'one'})

@app.route('/para/<string:b>', methods=['GET'])
def para(b):
    return f'The input string is {b}'

@app.route('/getm')
def getm():
    name = request.args.get('name')
    age = request.args.get('age')
    if name.isalpha() and age.isnumeric():
        return f'{name} is {age} years old'
    else:
        return 'name should be string and age should be integer'

@app.route('/postm',methods=['POST'])
def postm():
    data = request.get_json()
    if data['att1'] == data['att2']:
        result = data['att1'] + data['att2']
    else:
        result = 'The words are not equal'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host='192.168.56.1')