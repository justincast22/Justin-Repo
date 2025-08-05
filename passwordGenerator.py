import secrets
import math
import string

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

password_generator()
