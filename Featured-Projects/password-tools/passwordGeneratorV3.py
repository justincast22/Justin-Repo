import secrets
import math
import string

while True:
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

    print("Password Created!" + "\n")
    print(f"Password: {gen_password}")
    print(f"Entropy: {entropy}" + "\n")

    save_input = input("Would you like to save this password? (y/n): ")
    if save_input == "y":
        password_file = "/Users/titolin/Documents/GitHub/Justin-Repo/Featured-Projects/password-tools/Generated_Passwords.txt"
        with open(password_file, "a") as f:
            f.write(gen_password + "\n")
        print("Password Saved!" + "\n")

    cont_input = input("would you like to continue (y/n): ")
    if cont_input == "y":
        continue
    elif cont_input == "n":
        print("Shutting down." + "\n")
        break
