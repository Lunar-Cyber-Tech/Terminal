import socket

class Pinger:
    def __init__(self, ip: str, port: int, timeout=1):
        self.ip = ip
        self.port = port
        self.timeout = timeout

    def ping(self):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.ip, self.port))
            s.close()
            return True
        except Exception as e:
            return False

    def ping_loop(self, limit=1000):
        for i in range(1, limit):
            if self.ping():
                print(f"\u001b[32;1m{i} is open\u001b[0m")
            else:
                print(f"\u001b[31;1m{i} is closed\u001b[0m")