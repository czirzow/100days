import smtplib

smtp_hostname='smtp.gmail.com'
my_email='czirzow@gmail.com'
password='qqgt vlhb oorr ldwr'

# by default we do not want to send mail.
# this is just proof of concept code.
__ENABLED__ = False

def sendemail(to, subject, message):
    with smtplib.SMTP_SSL(smtp_hostname) as smtp:
        smtp.login(user=my_email, password=password)
        if __ENABLED__:
            smtp.sendmail(from_addr=my_email, to_addrs=to,
                          msg=f"Subject: {subject}\n\n{message}")
        else:
            print(smtp.noop())

