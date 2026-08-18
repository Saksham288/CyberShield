import os


def view_history():

    if not os.path.exists("scan_history.txt"):

        print("No History Found")

        return

    with open("scan_history.txt", "r") as file:

        print("\n")

        print(file.read())
if __name__ == "__main__":
    view_history()        