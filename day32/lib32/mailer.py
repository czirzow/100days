import smtplib
import os

hostname = str(os.environ.get('GOOGLE_HOST'))
username = str(os.environ.get('GOOGLE_EMAIL'))
password = str(os.environ.get('GOOGLE_PASS'))

# by default we do not want to send mail.
# this is just proof of concept code.
__ENABLED__ = False

def sendemail(to:str, subject:str, message:str) -> bool:
    """returns false if something went wrong"""
    try:
        with smtplib.SMTP_SSL(hostname) as smtp:
            smtp.login(user=username, password=password)
            if __ENABLED__:
                print(f"sending mail to {to}")
                smtp.sendmail(from_addr=username, to_addrs=to,
                              msg=f"Subject: {subject}\n\n{message}")
            else:
                print("noop response:", smtp.noop())
    except smtplib.SMTPException as e:
        print(f"Unable to sendmail: {e}")
        return False
    else:
        return True

