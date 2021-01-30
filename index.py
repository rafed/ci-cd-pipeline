from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return {
        'msg': 'Hello World!'
    }

@app.route('/add/<a>/<b>')
def add_route(a, b):
    return {
        'sum': add(a, b)
    }

# Takes two numbers as strings
def add(a,b):
    a = int(a)
    b = int(b)
    return a + b


if __name__ == "__main__":
    app.run("0.0.0.0", 8000)