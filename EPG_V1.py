#Password libs
import secrets
import math
import string

#Email libs
import smtplib
from email.message import EmailMessage
import schedule
import time
from dotenv import load_dotenv
import os

def password_generator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    full_pool = lower + upper + digits + symbols
    password_length = 16

    entropy = password_length * math.log2(len(full_pool))
    entropy = round(entropy)

    password = [secrets.choice(full_pool) for _ in range(password_length)]
    gen_password = "".join(password)

    print(f"Password: {gen_password}")
    print(f"Entropy: {entropy}")

    return gen_password, entropy

def main():
    load_dotenv()
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    EMAIL_TO = os.getenv("EMAIL_TO")

    gen_password, entropy = password_generator()
    smtp_server = "smtp.gmail.com"
    port = 587

    msg = EmailMessage()
    msg['Subject'] = 'Password Change Reminder'
    msg['From'] = EMAIL_USER
    msg['To'] = EMAIL_TO
    msg.set_content(
        f"Hello, this is your monthly reminder to change your password! "
        f"Here is your password: {gen_password} with an entropy of {entropy} bits."
    )

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.send_message(msg)

schedule.every().tuesday.at("17:12").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
