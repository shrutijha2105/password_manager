import random
import string

passwords = {}

try:
    with open("passwords.txt", "r") as file:
        for line in file:
            if ":" in line:
                website, pwd = line.strip().split(":")
                passwords[website] = pwd
except FileNotFoundError:
    pass  # This is fine now

def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%&"
    password = "".join(random.choice(chars) for _ in range(8))
    return password

while True:
    print("\n---PERSONAL PASSWORD MANAGER----")
    print("1. Save Password")
    print("2. View Passwords")
    print("3. Generate Password")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        site = input("Enter website:")
        pwd = input("Enter password:")

        passwords[site] = pwd

        with open("passwords.txt", "a")as file:
            file.write(f"{site}:{pwd}\n")

        print("Saved!")   

    elif choice == "2":
        if not passwords:
            print("No data")
        else:
            for site, pwd in passwords.items():
                print(site, ":", pwd)

    elif choice == "3":
        print("Generated Password", generate_password())

    elif choice == "4":
        print("ok bye cutie..")
        break

    else:
        print("In-valid input")