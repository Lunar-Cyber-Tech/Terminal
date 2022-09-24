import hashlib

class hashes:
    def __init__(self, string: str) -> str:
        self.string = string

    def md5(self) -> str: return hashlib.md5(self.string.encode()).hexdigest()

    def sha1(self) -> str: return hashlib.sha1(self.string.encode()).hexdigest()

    def sha224(self) -> str: return hashlib.sha224(self.string.encode()).hexdigest()

    def sha256(self) -> str: return hashlib.sha256(self.string.encode()).hexdigest()

    def sha384(self) -> str: return hashlib.sha384(self.string.encode()).hexdigest()

    def sha512(self) -> str: return hashlib.sha512(self.string.encode()).hexdigest()

    def sha3_224(self) -> str: return hashlib.sha3_224(self.string.encode()).hexdigest()

    def sha3_256(self) -> str: return hashlib.sha3_256(self.string.encode()).hexdigest()

    def sha3_384(self) -> str: return hashlib.sha3_384(self.string.encode()).hexdigest()

    def sha3_512(self) -> str: return hashlib.sha3_512(self.string.encode()).hexdigest()