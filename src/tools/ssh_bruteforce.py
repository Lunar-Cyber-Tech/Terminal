import socket
from ssh2.session import Session

def connect(host: str, user: str, passwd: str, port: int, timeout: float=1.0):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((host, port))
        s = Session()
        s.handshake(sock)
        s.userauth_password(user, passwd) # try to login
        print(f'\u001b[32;1m[+] {host}:{port} - {user}:{passwd}\u001b[0m')
        return True
    except Exception as e:
        if str(e) == 'timed out':
            print(f"\u001b[33;1m[!] Timed out\u001b[0m")
        else:
            pass
    finally:
        sock.close()