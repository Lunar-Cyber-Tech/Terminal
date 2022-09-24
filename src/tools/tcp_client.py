import socket, threading


class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))
        self.run()

    def send(self, msg):
        self.sock.send(msg.encode())

    def receive(self):
        while True:
            data = self.sock.recv(1024)
            print(data.decode())

    def run(self):
        threading.Thread(target=self.receive).start()
        while True:
            msg = input("> ")
            self.send(msg)

    def __del__(self):
        self.sock.close()