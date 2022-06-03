from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "<h1>Hello, World!<h1>"


@app.route('/about')
def about():
    return "gg"


@app.route('/base')
def base():
    return "base"


if __name__ == '__main__':
   app.run(host='0.0.0.0')