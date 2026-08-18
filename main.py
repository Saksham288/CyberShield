import os
from password_checker import password_checker
from port_scanner import port_scanner
from log_scanner import log_scanner
from website_checker import website_checker
from history import view_history


def clear():
    os.system("cls" if os.name == "nt" else "clear")


while True:

    clear()

    print("=" * 50)
    print("      CYBERSHIELD TOOLKIT")
    print("=" * 50)

    print("1. Password Strength Checker")
    print("2. Port Scanner")
    print("3. Security Log Scanner")
    print("4. Website Availability Checker")
    print("5. View Scan History")
    print("6. Exit")

    choice = input("\nEnter Choice : ")

    if choice == "1":
        password_checker()

    elif choice == "2":
        port_scanner()

    elif choice == "3":
        log_scanner()

    elif choice == "4":
        website_checker()

    elif choice == "5":
        view_history()

    elif choice == "6":
        print("\nThank You for using CyberShield")
        break

    else:
        print("\nInvalid Choice")

    input("\nPress Enter...")