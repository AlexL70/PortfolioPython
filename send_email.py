import smtplib as smtp
import ssl
import os

class EmailParameters:
    HOST: str = "smtp.gmail.com"
    PORT: int = 465
    USERNAME: str = "alexander.levinson.70@gmail.com"
    PASSWORD: str = os.getenv("APP2_PORTFOLIO_EMAIL_PASSWORD")


receiver = "alexander_levinson@hotmail.com"

context = ssl.create_default_context()
message = """\
Subject: Second test Email sent from Python
Hi Alex,
How are you?
This is a test email from the Python script.
Bye.

Regards,
Alex
"""

with smtp.SMTP_SSL(EmailParameters.HOST, EmailParameters.PORT, context=context) as server:
    server.login(EmailParameters.USERNAME, EmailParameters.PASSWORD)
    server.sendmail(EmailParameters.USERNAME, receiver, message)