import base64


class B64:
    def __init__(self, data):
        self.data = data

    def encode(self):
        return base64.b64encode(self.data.encode()).decode()

    def decode(self):
        return base64.b64decode(self.data.encode()).decode()