from abc import ABC, abstractmethod
import hashlib


# Supertype / Abstract Class
class HashAlgorithm(ABC):

    @abstractmethod
    def hash(self, text):
        pass


# Subtype MD5
class MD5Hash(HashAlgorithm):

    def hash(self, text):
        return hashlib.md5(text.encode()).hexdigest()


# Subtype SHA1
class SHA1Hash(HashAlgorithm):

    def hash(self, text):
        return hashlib.sha1(text.encode()).hexdigest()


# Subtype SHA256
class SHA256Hash(HashAlgorithm):

    def hash(self, text):
        return hashlib.sha256(text.encode()).hexdigest()


# Manager Class
class HashManager:

    def __init__(self, algorithm):
        self.algorithm = algorithm

    def setAlgorithm(self, algorithm):
        self.algorithm = algorithm

    def generateHash(self, text):
        return self.algorithm.hash(text)


# Teks langsung ditentukan
teks = "Python OOP Subtyping"


# Menggunakan MD5
manager = HashManager(MD5Hash())
print("MD5    :", manager.generateHash(teks))


# Menggunakan SHA1
manager.setAlgorithm(SHA1Hash())
print("SHA1   :", manager.generateHash(teks))


# Menggunakan SHA256
manager.setAlgorithm(SHA256Hash())
print("SHA256 :", manager.generateHash(teks))