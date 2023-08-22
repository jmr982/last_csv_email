#!/bin/python3

from datetime import date
from parse_last_to_csv import get_log, parse_log_to_csv
from send_email import email_message, email_send
import os


def main(smtp_server, email_auth, email_from, email_to):
    today = str(date.today())
    last = bytes(parse_log_to_csv(get_log("last")), "utf-8")
    lastb = bytes(parse_log_to_csv(get_log("lastb")), "utf-8")
    subject = f"Login data: {today}"
    body = "Attached last and lastb since 'yesterday'."
    attachments = [{"data":last, "name": f"last_{today}.csv"},
            {"data": lastb, "name": f"lastb_{today}.csv"}]
    message = email_message(f"{os.uname()[1]} <{email_from}>",
            email_to,
            subject,
            body,
            attachments)
    email_send(smtp_server, email_auth, email_from, email_to, message)
    return None


if __name__ == "__main__":
    try:
        smtp_server = os.environ["SMTP_SERVER"]
        email_auth = os.environ["EMAIL_AUTH"]
        email_from = os.environ["EMAIL_FROM"]
        email_to = os.environ["EMAIL_TO"]
        main(smtp_server, email_auth, email_from, email_to)
    except Exception as e:
        print(e)
