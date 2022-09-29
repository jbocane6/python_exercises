# !/usr/bin/python3
from email.message import EmailMessage
import ssl
import smtplib
import json


def send(receiver, subject, body):
    # Opening JSON file
    f = open('./assets/credentials.json')
    y = json.load(f)
    f.close()
    # create email
    em = EmailMessage()
    em["From"] = y["sender"]
    em["To"] = receiver
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(y["sender"], y["passwd"])
        smtp.sendmail(y["sender"], receiver, em.as_string())
