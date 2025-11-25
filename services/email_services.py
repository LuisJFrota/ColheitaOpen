import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(to, subject, message):
    email_address = os.getenv("EMAIL")
    email_password = os.getenv("EMAIL_PASSWORD")

    msg = MIMEText(message, "plain", "utf-8")
    msg['Subject'] = subject
    msg['From'] = email_address
    msg['To'] = to

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(email_address, email_password)
            smtp.send_message(msg)
        return True

    except Exception as e:
        print("Erro ao enviar email:", e)
        return False
