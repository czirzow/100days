# notes
# Guess the number website.

#https://localhost/uri

from flask import Flask, render_template
from datetime import date
from mylib.guess import Guess

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', today=date.today())

@app.route('/guess/<name>')
def guess(name):
    api = Guess(name=name)
    return render_template('guess.html',
                           name=name,
                           age=api.guess_age(),
                           gender=api.guess_gender(),
                           today=date.today()
                           )




if __name__ == '__main__':
    app.run(debug=True)
