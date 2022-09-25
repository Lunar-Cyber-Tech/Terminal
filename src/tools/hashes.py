import hashlib

class hashes:
    def __init__(self, string: str) -> None:
        self.string = string

    def md5(string) -> str:
        return hashlib.md5(string.encode()).hexdigest()

    def sha1(string) -> str:
        return hashlib.sha1(string.encode()).hexdigest()

    def sha224(string) -> str:
        return hashlib.sha224(string.encode()).hexdigest()

    def sha256(string) -> str:
        return hashlib.sha256(string.encode()).hexdigest()

    def sha384(string) -> str:
        return hashlib.sha384(string.encode()).hexdigest()

    def sha512(string) -> str:
        return hashlib.sha512(string.encode()).hexdigest()