#!/bin/python3

import os
import sys
from smtplib import SMTP_SSL, SMTP_SSL_PORT
from email.message import EmailMessage


def email_message(email_from, email_to, subject, body, attachments=None):
    message = EmailMessage()
    message["From"] = email_from
    message["To"] = email_to
    message["Subject"] = subject
    message.set_content(body)
    if attachments:  # Expects the attachment(s) to a dictionary
        for attachment in attachments:
            message.add_attachment(
                attachment["data"],
                filename=attachment["name"],
                maintype="application",  # application/octet-stream used as generic types
                subtype="octet-stream")
    return message


def email_send(smtp_server, email_auth, email_from, email_to, email_message):
    server = SMTP_SSL(smtp_server, port=SMTP_SSL_PORT)
    server.login(email_from, email_auth)
    server.sendmail(email_from, email_to.split(","), email_message.as_bytes())
    server.quit()
    return None


def main(
        smtp_server, email_from, email_auth, email_to, subject, message,
        attachments):
    attachment_list = []
    with open(message, "r") as m:
        body = m.read()
    if attachments:
        # Reads the attachment(s) and appends it to the list as a dictionary
        for attachment in attachments:
            with open(attachment, "rb") as a:
                attachment_list.append({"data": a.read(), "name": attachment})
    email = email_message(email_from,
                          email_to,
                          subject,
                          body,
                          attachment_list)
    email_send(smtp_server, email_auth, email_from, email_to, email)
    return None


if __name__ == "__main__":
    try:
        attachments = sys.argv[4].split(",")
    except:
        attachments = None
    try:
        smtp_server = os.environ["SMTP_SERVER"]
        email_from = os.environ["EMAIL_FROM"]
        email_auth = os.environ["EMAIL_AUTH"]
        email_to = sys.argv[1]
        subject = sys.argv[2]
        message = sys.argv[3]
        main(smtp_server, email_from, email_auth,
             email_to, subject, message, attachments)
        print(f"Email sent to: {email_to}")
    except Exception as e:
        print(e)
