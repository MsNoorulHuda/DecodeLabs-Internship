import secrets
import string
#input from user
length = int(input("Enter password length: "))
#conditions
if length <= 0:
    print("Please enter a valid password length.")
elif length > 200:
    print("Password length is too large.")
else:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = []
    #for lopp
    for i in range(length):
        password.append(secrets.choice(characters))
    print("Generated Password:", ''.join(password))