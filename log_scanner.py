from datetime import datetime
import os

def log_scanner():

    base_dir = os.path.dirname(os.path.abspath(__file__))

    log_file = os.path.join(base_dir, "security_log.txt")
    history_file = os.path.join(base_dir, "scan_history.txt")

    if not os.path.exists(log_file):
        print("\nsecurity_log.txt not found!")
        print("Expected location:")
        print(log_file)
        return

    keywords = ["ERROR", "FAILED LOGIN", "WARNING"]

    with open(log_file, "r") as file:
        data = file.read().upper()

    print("\nSecurity Log Scan Report")
    print("----------------------------")

    history = ""

    for word in keywords:
        count = data.count(word)
        print(f"{word} : {count}")
        history += f"{word} : {count}\n"

    with open(history_file, "a") as file:
        file.write(f"\n{datetime.now()}\n")
        file.write("Log Scanner\n")
        file.write(history)


if __name__ == "__main__":
    log_scanner()