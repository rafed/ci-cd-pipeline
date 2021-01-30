from flask import Flask

app = Flask(__name__)

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
    app.run("localhost", 8000)