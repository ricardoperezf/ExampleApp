from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World Jesus Fuentes! Hello World Jesus, nueestro poryecto jajajjaja!'
master

@app.route('/jesus')
def hellojesus():
    return 'Hello Jesus Fuentes!'

if __name__ == '__main__':
    app.run(host="0.0.0.0")
