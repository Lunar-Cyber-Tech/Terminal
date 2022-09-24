try:
    import ctypes
    import platform
    import os
    import random
    import string

    from pystyle import *
    from datetime import datetime
    from rich import print
    from rich.console import Console

    from src.common import database
    from src.methods.L4 import bomber, overload, ovh, syn, tcp, udp
    from src.methods.L7 import http
    from src.tools import (b64, hashes, ip_resolver, pinger, portscanner,
                        proxy_checker, ssh_bruteforce, tcp_client)
except ImportError as e:
    print(f"[red]Failed to import module(s): {e}[/red]")
    exit()

class main:
    def __init__(self) -> None:
        self._init()
        self.main()
    
    @staticmethod
    def _init() -> None:
        # init the console to allow for colors and other stuff
        System.Init()
        System.Clear()
        now = datetime.now()
        current_date = now.strftime("%d/%m/%Y")
        if platform.system() == "Windows":
            ctypes.windll.kernel32.SetConsoleTitleW(f"[{current_date}] Terminal Hacker | {platform.system()} | {platform.release()} | {platform.version()}")
        else:
            print(f"\033]0;[{current_date}] Terminal Hacker | {System.GetOS()}\007")

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
            ctypes.windll.kernel32.SetConsoleTitleW(f"[{current_date}] Terminal Hacker | {platform.system()} | {platform.release()} | {platform.version()} | {title}")
        else:
            print(f"\033]0;[{current_date}] Terminal Hacker | {platform.system()} | {platform.release()} | {platform.version()} | {title}\007")

    def main(self) -> None:
        self.set_title("Main Menu")
        print("[bold blue]Welcome to Terminal Hacker![/bold blue]")
        print("[bold blue]Please select an option:[/bold blue]")
        print("[bold blue]1. [bold green]L4[/bold green] - Layer 4 Attacks[/bold blue]")
        print("[bold blue]2. [bold green]L7[/bold green] - Layer 7 Attacks[/bold blue]")
        print("[bold blue]3. [bold green]Tools[/bold green] - Tools[/bold blue]")
        print("[bold blue]4. [bold green]Database[/bold green] - Database[/bold blue]")
        print("[bold blue]5. [bold green]Exit[/bold green] - Exit[/bold blue]")
        print("[bold blue]6. [bold green]About[/bold green] - About[/bold blue]")
        print("[bold blue]7. [bold green]Help[/bold green] - Help[/bold blue]")
        print("[bold blue]8. [bold green]Credits[/bold green] - Credits[/bold blue]")
        print("[bold blue]9. [bold green]Donate[/bold green] - Donate[/bold blue]")
        print("[bold blue]10. [bold green]Update[/bold green] - Update[/bold blue]")
        print("[bold blue]11. [bold green]Clear[/bold green] - Clear[/bold blue]")
        print("[bold blue]12. [bold green]Settings[/bold green] - Settings[/bold blue]")
        print("[bold blue]13. [bold green]License[/bold green] - License[/bold blue]")
        print("[bold blue]14. [bold green]Changelog[/bold green] - Changelog[/bold blue]")
        print("[bold blue]15. [bold green]Report a bug[/bold green] - Report a bug[/bold blue]")
        print("[bold blue]16. [bold green]Contact[/bold green] - Contact[/bold blue]")
        print("[bold blue]17. [bold green]Discord[/bold green] - Discord[/bold blue]")
        print("[bold blue]18. [bold green]Github[/bold green] - Github[/bold blue]")
        print("[bold blue]19. [bold green]Twitter[/bold green] - Twitter[/bold blue]")
        input()


main()