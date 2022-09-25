import socket, threading
from contextlib import suppress
from time import sleep
from rich import print

class ProxyChecker:
    def __init__(self, file, timeout: float):
        self.working_proxies = []
        self.proxies = 0
        self.failed_proxies = []
        self.file = file
        self.timeout = timeout

    def start(self):
        with suppress(Exception):
            try:
                with open(self.file, 'r') as f:
                    for line in f:
                        line=line.strip()
                        threading.Thread(target=self.check_proxy, args=(line.split(':')[0], line.split(':')[1])).start()
                f.close()
                self.save_proxies()
            except FileNotFoundError:
                print(f'[-] {self.file} not found')
            
    def check_proxy(self, ip, port):
        if ip in self.working_proxies or ip in self.failed_proxies:
            return
        else:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(self.timeout)
                s.connect((ip, int(port)))
                s.close()
                self.proxies += 1
                with open('working-proxies.txt', 'a') as f:
                    f.write(f'{ip}:{port}\n')
                f.close()
                self.working_proxies.append(ip + ':' + str(port)) if ip + ':' + str(port) not in self.working_proxies else None
            except:
                self.proxies += 1
                self.failed_proxies.append(ip + ':' + str(port))

    def save_proxies(self):
        sleep(1)
        with open('working-proxies.txt', 'w') as f:
            for proxy in self.working_proxies:
                f.write(proxy + '\n')
        f.close()
        print(f'[+][green] {len(self.working_proxies)} working proxies found')
        print(f'[-][red] {len(self.failed_proxies)} failed proxies found')
        print(f'[*][yellow] {self.proxies} proxies total')