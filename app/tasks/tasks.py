import smtplib
from email.message import EmailMessage

from celery import Celery

from config import (
    REDIS_HOST,
    REDIS_PORT,
    SMTP_HOST,
    SMTP_PORT,
    SMTP_USER,
    SMTP_PASSWORD,
)


celery = Celery("tasks", broker=f"redis://{REDIS_HOST}:{REDIS_PORT}")


def get_email_random_cat(username: str):
    email = EmailMessage()
    email["Subject"] = "Trade"
    email["From"] = SMTP_USER
    email["To"] = SMTP_USER  # user email: email['To'] = user@mail.com

    email.set_content(
        "<div>"
        f"<h1> Hello, {username}, here's your random cat:</h1>"
        "<img src='https://cataas.com/cat'"
        "</div>",
        subtype="html",
    )
    return email


@celery.task
def send_email_random_cat(username: str):
    email = get_email_random_cat(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
