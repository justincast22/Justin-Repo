import secrets
import math
import string
import random

def password_generator_random():
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

def password_generator_Chunked():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    all_chars = lower + upper + digits
    pool_1 = random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars)
    pool_2 = random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars)
    pool_3 = random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars)
    pool_4 = random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars) + random.choice(all_chars)

    full_pool = pool_1 + "-" + pool_2 + "-" + pool_3 + "-" + pool_4

    print(full_pool)

def password_generator_Chunked_v2():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    all_chars = lower + upper + digits
    pool_1 = ''.join(random.choice(all_chars) for _ in range(4))
    pool_2 = ''.join(random.choice(all_chars) for _ in range(4))
    pool_3 = ''.join(random.choice(all_chars) for _ in range(4))
    pool_4 = ''.join(random.choice(all_chars) for _ in range(4))


    full_pool = pool_1 + "-" + pool_2 + "-" + pool_3 + "-" + pool_4

    print(full_pool)

def password_generator_Chunked_v3():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    all_chars = lower + upper + digits
    pools = []

    chunk_length = int(input("Choose amount of chunks in password: "))
    chunk_size = int(input("Choose size of each chunk: "))

    for _ in range(chunk_length):
        pool = ''.join(random.choice(all_chars) for _ in range(chunk_size))
        pools.append(pool)

    full_pool = '-'.join(pools)
    print(full_pool)

def password_generator_Chunked_v4():
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits

    all_chars = lower + upper + digits
    pools = []

    chunk_length = int(input("Choose amount of chunks in password: "))
    chunk_size = int(input("Choose size of each chunk: "))

    for _ in range(chunk_length):
        pool = ''.join(secrets.choice(all_chars) for _ in range(chunk_size))
        pools.append(pool)

    full_pool = '-'.join(pools)
    print(full_pool)




#password_generator_random()
#password_generator_Chunked()
#password_generator_Chunked_v2()
#password_generator_Chunked_v3()
password_generator_Chunked_v4()
