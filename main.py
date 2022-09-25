try:
    import platform
    import os
    import sys
    import random
    import threading
    import string

    from pystyle import *
    from datetime import datetime
    from rich import print
    from rich.console import Console
    from contextlib import suppress
    import ctypes
    from src.methods.L4 import bomber, overload, ovh, syn, tcp, udp
    from src.methods.L7 import http
    from src.tools import (b64, hashes, ip_resolver, pinger, portscanner,
                        proxy_checker, ssh_bruteforce, tcp_client)
except ImportError as e:
    if 'ctpyes' in str(e):
        pass
    else:
        print(f"[red]Failed to import module(s): {e}[/red]")
        exit()
c = Console()
class main:
    def __init__(self) -> None:
        self._init()
        self.run()
    
    @staticmethod
    def _init() -> None:
        # init the console to allow for colors and other stuff
        System.Init()
        System.Clear()
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetConsoleTitleW(f"[{current_date}] Lunar Terminal")
        
        # check if the user is root/admin
        try:
            if os.getuid() != 0:
                print("[red]You need to have admin privileges to run this script.[/red]")
                print("[red]Please try again, this time using 'sudo'. Exiting.[/red]")
                exit(1)
        except AttributeError: # error gets thrown when running on windows
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            if not is_admin:
                print("[red]You need to have admin privileges to run this script.[/red]")
                print("[red]Please try again, this time 'as administrator'. Exiting.[/red]")
                exit(1)

    
    @staticmethod
    def set_title(title: str) -> None:
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetConsoleTitleW(f"[{current_date}] Lunar Terminal | {title}")
        
    @staticmethod
    def parse_command(command: str, args: list=[]) -> None:
        try:
            if command == 'b64':
                if args[0] == 'encode':
                    print(b64.B64(args[1]).encode())
                elif args[0] == 'decode':
                    print(b64.B64(args[1]).decode())
            elif command == 'hash':
                if args[0] == 'md5':
                    print(hashes.hashes.md5(args[1]))
                elif args[0] == 'sha1':
                    print(hashes.hashes.sha1(args[1]))
                elif args[0] == 'sha224':
                    print(hashes.hashes.sha224(args[1]))
                elif args[0] == 'sha256':
                    print(hashes.hashes.sha256(args[1]))
                elif args[0] == 'sha384':
                    print(hashes.hashes.sha384(args[1]))
                elif args[0] == 'sha512':
                    print(hashes.hashes.sha512(args[1]))
            elif command == 'resolve':
                ip_resolver.ip_resolver(args[0]).resolve()
            elif command == 'ping':
                pinger.Pinger(args[0], int(args[1])).ping_loop()
            elif command == 'portscan':
                target = args[0]
                scan_type = args[1]
                timeout = float(args[2])
                if scan_type == 'common':
                    portscanner.PortScanner(target, timeout).common()
                elif scan_type == 'full':
                    portscanner.PortScanner(target, timeout).full()
                elif scan_type == 'quick':
                    portscanner.PortScanner(target, timeout).quick()
                else:
                    print("[red]Invalid scan type. Types: common, full, quick[/red]")
            elif command == 'proxycheck':
                proxy_checker.ProxyChecker(args[0], float(args[1])).start()
            elif command == 'tcp':
                target = args[0]
                port = int(args[1])
                threads = int(args[2])
                timeout = int(args[3])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=tcp.tcp, args=(target,port,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:{port} for {timeout} seconds')
            elif command == 'udp':
                target = args[0]
                port=int(args[1])
                threads = int(args[2])
                timeout = int(args[3])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=udp.udp, args=(target,port,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:{port} for {timeout} seconds')
            elif command == 'http':
                target = args[0]
                threads = int(args[1])
                timeout = int(args[2])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=http.http, args=(target,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:80 for {timeout} seconds')
            elif command == 'syn':
                target = args[0]
                port = int(args[1])
                threads = int(args[2])
                timeout = int(args[3])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=syn.syn, args=(target,port,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:{port} for {timeout} seconds')
            elif command == 'ovh':
                target = args[0]
                port = int(args[1])
                threads = int(args[2])
                timeout = int(args[3])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=ovh.ovh, args=(target,port,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:{port} for {timeout} seconds')
            elif command == 'overload':
                target = args[0]
                port = int(args[1])
                threads = int(args[2])
                timeout = int(args[3])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=overload.overload, args=(target,port,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:{port} for {timeout} seconds')
            elif command == 'bomber':
                target = args[0]
                port = int(args[1])
                threads = int(args[2])
                timeout = int(args[3])
                for i in range(threads):
                    print(f"[green][+] Started {i} Threads...", end='\r')
                    threading.Thread(target=bomber.bomb, args=(target,port,1,timeout,)).start()
                print(f'[green][+] Started {threads} Threads to attack {target}:{port} for {timeout} seconds')
            elif command == 'bruteforce':
                target = args[0]
                port = int(args[1])
                username = str(args[2])
                timeout = float(args[4])
                wordlist = args[3]
                ssh_bruteforce.bruteforce(target, port, username, wordlist, timeout)
            elif command == 'tcp-client':
                host = args[0]
                port = int(args[1])
                timeout = float(args[2])
                tcp_client.Client(host, port, timeout)
        except IndexError:
            print(f'[red][-] Not enough arguments. Please refer to the "help" command for correct command format')



    def run(self) -> None:
        banner = f'''
[cyan]:##:::::::'##::::'##:'##::: ##::::'###::::'########::
[cyan]:##::::::: ##:::: ##: ###:: ##:::'## ##::: ##.... ##:
[cyan]:##::::::: ##:::: ##: ####: ##::'##:. ##:: ##:::: ##:
[cyan]:##::::::: ##:::: ##: ## ## ##:'##:::. ##: ########::
[cyan]:##::::::: ##:::: ##: ##. ####: #########: ##.. ##:::
[cyan]:##::::::: ##:::: ##: ##:. ###: ##.... ##: ##::. ##::
[cyan]:########:. #######:: ##::. ##: ##:::: ##: ##:::. ##:
[cyan]:.......:::.......:::..::::..::..:::::..::..:::::..::[/cyan]
    '''[1:]
        c.print(banner, justify='center')
        while True:
            command = input(f"[\u001b[1mroot@lunar\u001b[0m] > ")
            if command == 'help':
                print("[green]b64 encode <text>[/green]")
                print("[green]b64 decode <text>[/green]")
                print("[green]hash md5 <text>[/green]")
                print("[green]hash sha1 <text>[/green]")
                print("[green]hash sha224 <text>[/green]")
                print("[green]hash sha256 <text>[/green]")
                print("[green]hash sha384 <text>[/green]")
                print("[green]hash sha512 <text>[/green]")
                print("[green]resolve <ip> (domains/urls supported)[/green]")
                print("[green]ping <ip> <port>[/green]")
                print("[green]portscan <ip> <type of scan> <timeout>[/green]")
                print("[green]proxycheck <list of proxies> <timeout>[/green]")
                print("[green]bruteforce <ip> <port> <username> <wordlist>[/green]")
                print("[green]tcp-client <ip> <port> <timeout>[/green]")
                print("[green]bomber <ip> <port> <threads> <timeout>[/green]")
                print("[green]overload <ip> <port> <threads> <timeout>[/green]")
                print("[green]ovh <ip> <port> <threads> <timeout>[/green]")
                print("[green]syn <ip> <port> <threads> <timeout>[/green]")
                print("[green]tcp <ip> <port> <threads> <timeout>[/green]")
                print("[green]udp <ip> <port> <threads> <timeout>[/green]")
                print("[green]http <ip> <port> <threads> <timeout>[/green]")
            elif command == 'exit':
                os._exit(1)
            elif command == 'cls' or command == 'clear':
                os.system('cls' if os.name == 'nt' else 'clear')
                c.print(banner, justify='center')
            else:
                args = command.split(' ')
                command = args[0]
                args.pop(0)
                self.parse_command(command, args)


main()
