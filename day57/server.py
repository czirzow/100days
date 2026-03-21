# notes
# Guess the number website.

#https://localhost/uri

from flask import Flask, render_template
from datetime import date

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html', today=date.today())

if __name__ == '__main__':
    app.run(debug=True)
