# !/usr/bin/python3
from email.message import EmailMessage
import ssl
import smtplib
import json

if __name__ != "__main__":
    # create and send email
    def sendmail(receiverLst, subject, body):
        f = open('./assets/credentials.json')
        y = json.load(f)
        f.close()

        # create email
        em = EmailMessage()
        em["From"] = y["sender"]
        em["To"] = ", ".join(receiverLst)
        em["subject"] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
            smtp.login(y["sender"], y["passwd"])
            smtp.sendmail(y["sender"], receiverLst, em.as_string())
