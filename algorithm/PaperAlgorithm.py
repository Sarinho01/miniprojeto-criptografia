from abc import ABC, abstractmethod

from criptography.message_compactator.CompactorMessage import CompactMessage
from criptography.message_encryption.EncryptMessage import EncryptMessage


class PaperAlgorithm(ABC):
        def __init__(self, compactor_message: CompactMessage, encrypt_message: EncryptMessage):
            self.compactor_message = compactor_message
            self.encrypt_message = encrypt_message

        @abstractmethod
        def put_message_in_image_and_compact(self, image, message):
            pass

        @abstractmethod
        def get_message_and_image(self, image, json):
            pass
