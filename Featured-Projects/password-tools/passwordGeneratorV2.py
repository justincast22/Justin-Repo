import secrets
import math
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

full_pool = lower + upper + digits + symbols

length_input = int(input("Choose amount of characters in password: "))

entropy = length_input * math.log2(len(full_pool))
entropy = round(entropy)

password = []

for i in range(length_input):
    password.append(secrets.choice(full_pool))

gen_password = "".join(password)

print(f"Password: {gen_password}")
print(f"Entropy: {entropy}")
