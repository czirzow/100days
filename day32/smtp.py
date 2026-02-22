import smtplib

smtp_hostname='smtp.gmail.com'
email='czirzow@gmail.com'
password='qqgt vlhb oorr ldwr'

def send_email(to, message):
    if 0:
        with smtplib.SMTP_SSL(smtp_hostname) as smtp:
            smtp.login(user=email, password=password)
            # can we do an operation?
            print(smtp.noop())

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
