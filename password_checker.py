import re
from datetime import datetime


def password_checker():

    password = input("Enter Password : ")

    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"\d", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score <= 2:
        strength = "WEAK"

    elif score <= 4:
        strength = "MODERATE"

    else:
        strength = "STRONG"

    print("\nPassword Strength :", strength)

    with open("scan_history.txt", "a") as file:
        file.write(f"\n{datetime.now()}\n")
        file.write(f"Password Strength : {strength}\n")

if __name__ == "__main__":
    password_checker()        