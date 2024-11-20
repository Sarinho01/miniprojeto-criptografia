import base64
from abc import ABC

from Crypto.Cipher import PKCS1_OAEP

from criptography.message_encryption.EncryptMessage import EncryptMessage


class RSAEncryptMessage(EncryptMessage, ABC):

    def __init__(self, public_key, private_key):
        self.public_key = public_key
        self.private_key = private_key

    def encrypt_message_and_put_in_base64(self, message):
        encrypted_message = self.encrypt_message(message)
        encrypted_base64 = base64.b64encode(encrypted_message)

        return encrypted_base64.decode()

    def dencrypt_message_in_base64(self, message):
        encrypted_message = base64.b64decode(message)
        decrypted_message = self.dencrypt_message(encrypted_message)

        return decrypted_message.decode()

    def encrypt_message(self, message):
        cipher = PKCS1_OAEP.new(self.public_key)

        message_bytes = message.encode()
        max_chunk_size = self.public_key.size_in_bytes() - 42
        encrypted_chunks = []

        for i in range(0, len(message_bytes), max_chunk_size):
            chunk = message_bytes[i:i + max_chunk_size]
            encrypted_chunks.append(cipher.encrypt(chunk))

        return b''.join(encrypted_chunks)

    def dencrypt_message(self, message):
        cipher = PKCS1_OAEP.new(self.private_key)

        decrypted_chunks = []
        chunk_size = self.private_key.size_in_bytes()

        for i in range(0, len(message), chunk_size):
            chunk = message[i:i + chunk_size]
            decrypted_chunks.append(cipher.decrypt(chunk))

        return b''.join(decrypted_chunks)
