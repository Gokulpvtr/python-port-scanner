import socket
import threading
import json
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

# Banner
print("====================================")
print(" Advanced Port Scanner ")
print(" Author: Gokulkrishnan S")
print("====================================")

target = input("Enter target (IP or domain): ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}")
print("Scan started at:", datetime.now())
print("-" * 40)

open_ports = []

# Service mapping
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

# Scan function
def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            service = services.get(port, "Unknown")

            # Banner grabbing
            try:
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(1024).decode().strip()
            except:
                banner = "No banner"

            print(Fore.GREEN + f"[OPEN] Port {port} ({service})")
            open_ports.append({
                "port": port,
                "service": service,
                "banner": banner
            })

        sock.close()

    except:
        pass


# Multi-threading
threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for threads to finish
for t in threads:
    t.join()

# Save results
with open("results.json", "w") as file:
    json.dump(open_ports, file, indent=4)

print("\nScan completed!")
print(f"Open ports found: {len(open_ports)}")
print("Results saved to results.json")