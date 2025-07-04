import socket

def scan(target, ports):
    print(f"Scanning target: {target}")
    for port in ports:
        try:
            sock = socket.socket()
            sock.settimeout(1)
            sock.connect((target, port))
            print(f"[+] Port {port} is open.")
            sock.close()
        except:
            pass

if __name__ == "__main__":
    target = input("Enter target IP: ")
    ports = range(1, 1024)
    scan(target, ports)
