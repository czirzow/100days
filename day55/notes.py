# notes
# Guess the number website.

#https://localhost/uri

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world.'

@app.route('/bye')
def bye():
    return 'Thanks for all the fish.'


if __name__ == 'main':
    app.run()
