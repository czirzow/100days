# notes
# Guess the number website.

#https://localhost/uri

from flask import Flask

def logging_decorator(func):
    def log(*args):
        print('You called')
        print(f"{func.__name__}({','.join(map(str,args))})")
        rc = func(*args)
        print(f"It returned: {rc}")
    return log


@logging_decorator
def a_function(*args):
    return sum(args)

a_function(1, 2, 3)

exit()


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world.'

def make_bold(func):
    def bold():
        return '<b>' + func() + '</b>'
    return bold

@app.route('/bye')
@make_bold
def bye():
    return 'Thanks for all the fish.'


@app.route('/username/<name>')
def greate(name):
    return f"Hello {name}"

if __name__ == '__main__':
    app.run(debug=True)
