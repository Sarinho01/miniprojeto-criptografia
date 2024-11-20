import json

from Crypto.PublicKey import RSA

from algorithm.BasePaperAlgorithm import create_json, BasePaperAlgorithm
from criptography.message_compactator.HuffmanCompactor import HuffmanCompactMessage
from criptography.message_encryption.RSACryptographyMessage import RSAEncryptMessage

key = RSA.generate(2048)

r = RSAEncryptMessage(key.public_key(), key)
b = BasePaperAlgorithm(HuffmanCompactMessage(), r)

combined_bites = b.put_message_in_image_and_compact("", "teste do saro é isso ou não")

size_bytes = bytes(int(''.join(map(str, combined_bites[i:i+8])), 2) for i in range(0, 32, 8))
json_encrypted = bytes(int(''.join(map(str, combined_bites[i:i + 8])), 2) for i in range(32, int.from_bytes(size_bytes) + 32, 8))
json_decrypted_bytes = b.encrypt_message.dencrypt_message(json_encrypted)
json_obj = json.loads(json_decrypted_bytes)
codebook = json_obj["huffman_codebook"]
print(codebook)

message_compressed_bytes = combined_bites[int.from_bytes(size_bytes) + 32:]
message_encrypted = b.compactor_message.unpack_message(message_compressed_bytes, codebook)

print(b.encrypt_message.dencrypt_message_in_base64(message_encrypted))


