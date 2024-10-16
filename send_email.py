import smtplib as smtp
import ssl
import os


def send_email(sender: str, message: str):
    class EmailParameters:
        HOST: str = "smtp.gmail.com"
        PORT: int = 465
        USERNAME: str = "alexander.levinson.70@gmail.com"
        PASSWORD: str = os.getenv("APP2_PORTFOLIO_EMAIL_PASSWORD")


    receiver = EmailParameters.USERNAME

    context = ssl.create_default_context()
    message_string = f"""\
Subject: Portfolio App Contact Form
Reply-To: {sender}
{message}

Sent by: {sender}
From the "Contact Me" form on the Portfolio App.
"""

    with smtp.SMTP_SSL(EmailParameters.HOST, EmailParameters.PORT, context=context) as server:
        server.login(EmailParameters.USERNAME, EmailParameters.PASSWORD)
        server.sendmail(EmailParameters.USERNAME, receiver, message_string)
