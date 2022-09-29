# !/usr/bin/python3
from email.message import EmailMessage
import data as d
import ssl
import smtplib

def send(receiver, subject, body):
    # create email
    em = EmailMessage()
    em["From"] = d.email_sender
    em["To"] = receiver
    em["subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
        smtp.login(d.email_sender, d.email_password)
        smtp.sendmail(d.email_sender, receiver, em.as_string())
