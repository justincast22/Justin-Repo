#Password libs
import secrets
import math
import string

#Email libs
import smtplib
from email.message import EmailMessage
import schedule
import time

def password_generator():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    full_pool = lower + upper + digits + symbols

    password_length = 16

    entropy = password_length * math.log2(len(full_pool))
    entropy = round(entropy)

    password = []
    for i in range(password_length):
        password.append(secrets.choice(full_pool))
    gen_password = "".join(password)

    print(f"Password: {gen_password}")
    print(f"Entropy: {entropy}")

    return gen_password, entropy

def main():
    gen_password, entropy = password_generator()
    smtp_server = "smtp.gmail.com"
    port = 587

    msg = EmailMessage()
    msg['Subject'] = 'Password Change Reminder'
    msg['From'] = 'justincas0522@gmail.com'
    msg['To'] = 'titoc0522@gmail.com'
    msg.set_content(f'Hello this is your monthly reminder to change your password! Here is your password: {gen_password} with an entropy of {entropy}')

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login('justincas0522@gmail.com', 'cgdb zskp zuub ubkf')
        server.send_message(msg)

schedule.every().tuesday.at("17:12").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)