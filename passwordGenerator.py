import secrets
import math
import string

def password_generator():
    #setting up password generation
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    full_pool = lower + upper + digits + symbols

    #sets password length
    password_length = 16
    
    #calculates entropy
    entropy = password_length * math.log2(len(full_pool))
    entropy = round(entropy)

    #creates password by first putting individual characters in a list and eventually joining them
    password = []
    for i in range(password_length):
        password.append(secrets.choice(full_pool))
    gen_password = "".join(password)

    #print results
    print(f"Password: {gen_password}")
    print(f"Entropy: {entropy}")

    return gen_password, entropy

password_generator()
