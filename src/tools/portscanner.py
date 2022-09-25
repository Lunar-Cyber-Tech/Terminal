import socket, threading
from rich.progress import track

class PortScanner:
    def __init__(self, ip, timeout=1):
        self.common_ports = [20, 21, 22, 23, 25, 53, 69, 79, 80, 123, 137, 138, 139, 143, 161, 162, 389, 443, 445, 7114, 8080, 9090, 25565]
        self.ip = ip
        self.timeout = timeout
        self.open_ports = []

    def connect(self, port):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(self.timeout)
            s.connect((self.ip, port))
            s.close()
            self.open_ports.append(port)
            #print(f"\u001b[32;1m{port} is open\u001b[0m")
        except:
            pass

    def common(self):
        for port in self.common_ports:
            result = threading.Thread(target=self.connect, args=(port,)).start()
        print(f"Open ports: {self.open_ports}")

    def quick(self, limit=10000):
        for i in track(range(1, limit), description="Scanning..."):
            result = threading.Thread(target=self.connect, args=(i,)).start()
        print(f"Open ports: {self.open_ports}")


    def full(self):
        for i in track(range(1, 65536), description="Scanning..."):
            result = threading.Thread(target=self.connect, args=(i,)).start()
        print(f"Open ports: {self.open_ports}")