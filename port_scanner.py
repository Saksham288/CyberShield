import socket
from datetime import datetime
def port_scanner():

    ip = input("Enter IP Address : ")

    ports = {
        21: "FTP",
        22: "SSH",
        80: "HTTP",
        443: "HTTPS"
    }

    print("\nScanning...\n")

    history = ""

    for port, service in ports.items():

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((ip, port))

        if result == 0:
            status = "Open"

        else:
            status = "Closed"

        print(f"{port} ({service}) : {status}")

        history += f"{port} {service} : {status}\n"

        sock.close()

    with open("scan_history.txt", "a") as file:
        file.write(f"\n{datetime.now()}\n")
        file.write(f"Port Scan : {ip}\n")
        file.write(history)

if __name__ == "__main__":
    port_scanner()        