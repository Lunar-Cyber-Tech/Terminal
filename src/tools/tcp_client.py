import socket, threading
from rich import print


class Client:
    def __init__(self, host, port, timeout):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(timeout)
        try:
            self.sock.connect((host, port))
            self.connected = True
            print(f'[green][+] Connected to {host}:{port}')
        except:
            print(f'[red][-] Failed to connect to {host}:{port}')
        self.run()

    def send(self, msg):
        try:
            self.sock.send(msg.encode())
        except:
            return

    def receive(self):
        while True:
            try:
                data = self.sock.recv(1024)
                print(data.decode())
            except Exception as e:
                self.connected = False
                print(f'[red][-] Connection closed: {e}')
                self.sock.close()
                break
        self.sock.close()

    def run(self):
        threading.Thread(target=self.receive).start()
        while self.connected == True:
            msg = input("> ")
            self.send(msg)
        self.sock.close()

    def __del__(self):
        self.sock.close()
