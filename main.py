from flask import Flask, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def start():
    return render_template('home.html')

@app.route('/result')
def result():
    result_value = "This is a sample result."
    return render_template('result.html', result=result_value)

if __name__ == '__main__':
    app.run(host='192.168.56.1')
