from flask import Flask, request, jsonify

app = Flask(__name__)

#  @app.route(url_pattern, [method/options])

@app.route('/')
def start():
    return "Hello World!!!!"

@app.route('/add', methods=['POST','GET'])
def add():
    if(request.method=='POST'):
        data = request.get_json()
        result = data['a'] + data['b']
        return jsonify({'result': result})
    else:
        return "Hello!!!"
    
@app.route("/addg/<int:a>/<int:b>",methods=['GET'])
def da(a,b):
    return jsonify({'result':a+b})

@app.route('/subtract', methods=['POST'])
def subtract():
    data = request.get_json()
    result = data['a'] - data['b']
    return jsonify({'result': result})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    result = data['a'] * data['b']
    return jsonify({'result': result})

@app.route('/divide', methods=['POST'])
def divide():
    data = request.get_json()
    if data['b'] == 0:
        return jsonify({'error': 'Division by zero is not allowed'}), 400
    result = data['a'] / data['b']
    return jsonify({'result': result})

@app.route('/user')
def get_user_details():
    name = request.args.get('name')
    age = request.args.get('age')
    if age.isnumeric() and name.isalpha:
        return f"Name: {name}\nAge: {age}"
    else:
        return "PODA MAIRU"

if __name__ == '__main__':
    app.run(host="192.168.56.1")