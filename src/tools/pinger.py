import socket, time

class Pinger:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

    def ping(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((self.ip, self.port))
            s.close()
            return True
        except Exception as e:
            return False

    def ping_loop(self, limit=1000):
        try:
            while True:
                if self.ping():
                    print(f"\u001b[32;1m{self.ip}:{self.port} is open\u001b[0m")
                else:
                    print(f"\u001b[31;1m{self.ip}:{self.port} is closed\u001b[0m")
                time.sleep(1)
        except KeyboardInterrupt:
            return