from abc import ABC, abstractmethod

class EncryptMessage(ABC):

    @abstractmethod
    def encrypt_message_and_put_in_base64(self, message):
        pass

    @abstractmethod
    def dencrypt_message_in_base64(self, message):
        pass

    @abstractmethod
    def encrypt_message(self, message):
        pass

    @abstractmethod
    def dencrypt_message(self, message):
        pass