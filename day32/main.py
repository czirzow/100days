##################### Extra Hard Starting Project ######################
import random as rand
import lib32.mailer as mailer
import lib32.birthdays as bd

template_files = [
        'templates/letter_1.txt',
        'templates/letter_2.txt',
        'templates/letter_3.txt',
        ]


# 2. Check if today matches a birthday in the birthdays.csv
birthdays = bd.today()
if len(birthdays) == 0:
    print("No Birthdays today")
    exit()


emails_sent = 0
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
        if mailer.sendemail(email, "Happy Birthday!", email_body):
            emails_sent += 1

print(f"sent {emails_sent} of {len(birthdays)}")

