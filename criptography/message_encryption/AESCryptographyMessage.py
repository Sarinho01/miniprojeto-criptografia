import base64

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util import Counter

from criptography.message_encryption.EncryptMessage import EncryptMessage


class AESEncryptMessage(EncryptMessage):

    def __init__(self, key):
        self.key = key

    def encrypt_message_and_put_in_base64(self, message):
        encrypted_message = self.encrypt_message(message)
        encrypted_base64 = base64.b64encode(encrypted_message)

        return encrypted_base64.decode()

    def dencrypt_message_in_base64(self, message):
        encrypted_message = base64.b64decode(message)
        decrypted_message = self.dencrypt_message(encrypted_message)

        return decrypted_message.decode()

    def encrypt_message(self, message):
        nonce = get_random_bytes(8)
        counter = Counter.new(64, prefix=nonce)

        cipher = AES.new(self.key, AES.MODE_CTR, counter=counter)

        ciphertext = cipher.encrypt(message)

        return nonce + ciphertext

    def dencrypt_message(self, message):
        nonce = message[:8]
        ciphertext = message[8:]

        counter = Counter.new(64, prefix=nonce)

        cipher = AES.new(self.key, AES.MODE_CTR, counter=counter)

        decrypted_message = cipher.decrypt(ciphertext)

        return decrypted_message
