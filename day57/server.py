# notes
# Guess the number website.

#https://localhost/uri

from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def root():
    year = date.today().year
    return render_template('index.html', year=year)

if __name__ == '__main__':
    app.run(debug=True)
