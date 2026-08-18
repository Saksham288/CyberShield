import requests
from datetime import datetime


def website_checker():

    website = input("Enter Website URL : ")

    try:

        response = requests.get(website, timeout=5)

        print("\nWebsite is Online")

        print("Status Code :", response.status_code)

        status = "Online"

    except:

        print("\nWebsite is Offline")

        status = "Offline"

    with open("scan_history.txt", "a") as file:

        file.write(f"\n{datetime.now()}\n")

        file.write(f"Website : {website}\n")

        file.write(f"Status : {status}\n")

if __name__ == "__main__":
    website_checker()        