##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random as rand
import lib32.mailer as mailer


csv_file = 'data/birthdays.csv'
template_files = [
        'templates/letter_1.txt',
        'templates/letter_2.txt',
        'templates/letter_3.txt',
        ]


# 2. Check if today matches a birthday in the birthdays.csv
birthdays = {}

try:
    df = pd.read_csv(csv_file)

except FileNotFoundError as e:
    print(f"Unable to open file: {e}")
    exit()
except pd.errors.EmptyDataError as e:
    print(f"Problem parsing file: {e}")
    pass
except pd.errors.ParserError as e:
    print(f"Problem parsing file: {e}")
    pass
else:
    now = dt.datetime.now()
    birthdays = {r.person:r.email for (_,r) in df.iterrows()
                 if r.month == now.month and r.day == now.day}

if len(birthdays) == 0:
    print("No Birthdays today")
    exit()


for name, email in birthdays.items():

    letter_file = rand.choice(template_files)
    try:
        with open(letter_file) as fh:
            email_body = fh.read().replace('[NAME]', name)

    except FileNotFoundError as e:
        print(e)
    else:
        print("v"*15)
        print(email_body)
        print("^"*15)
        rc = mailer.sendemail(email, "Happy Birthday!", email_body)
        # do something with rc?

