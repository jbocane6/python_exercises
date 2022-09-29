from email.message import EmailMessage
import data as d
import ssl
import smtplib

# email parts
email_sender = d.sender
email_password = d.password
email_receiver = d.receiver
subject = d.subject
body = d.body

# create email
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

