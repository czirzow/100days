
import datetime as dt
import random as rand

with open('data/quotes.txt') as fh:
    lines = fh.read().split("\n")

now = dt.datetime.now()

quote = ''
if now.isoweekday() == 6:
    quote = rand.choice(lines)
    print(quote)

if quote != '':
    email = f"""Subject: This is the subject

    {quote}

    Curt.
    """
    print(email)
