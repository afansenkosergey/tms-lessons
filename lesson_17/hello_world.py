from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<p>Hello world</p>'


@app.route('/<string:name>')
def user_name(name: str):
    return f'<p>Hello {name}</p>'


if __name__ == '__main__':
    app.run(port=8080, debug=True)
