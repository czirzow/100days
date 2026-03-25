# notes
# Guess the number website.

#https://localhost/uri

from flask import Flask, render_template
from datetime import date
from mylib.guess import Guess
from mylib.npoint import Npoint

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

@app.route('/blog')
def blog():
    # https://api.npoint.io/c790b4d5cab58020d391
    blog = Npoint()
    blog_records = blog.get_records()
    return render_template('blog.html', blog_records=blog_records)

@app.route('/blog/<int:id>')
def blog_details(id):
    # https://api.npoint.io/c790b4d5cab58020d391
    blog = Npoint()
    return render_template('blog_details.html', blog=blog.get_record(id))


if __name__ == '__main__':
    app.run(debug=True)
