from Crypto.PublicKey import RSA
from PIL import Image

from algorithm.BasePaperAlgorithm import BasePaperAlgorithm
from criptography.image_compactator.CompactorImageDWT import CompactImageDWT
from criptography.message_compactator.HuffmanCompactor import HuffmanCompactMessage
from criptography.message_encryption.RSACryptographyMessage import RSAEncryptMessage

key = RSA.generate(2048)

encryptMessageBase = RSAEncryptMessage(key.public_key(), key)
compactImageBase = CompactImageDWT()
compactMessageBase = HuffmanCompactMessage()
baseAlgorithm = BasePaperAlgorithm(compactMessageBase, encryptMessageBase, compactImageBase)

img = baseAlgorithm.put_message_in_image_and_compact(Image.open("imagem.png"), "teste do saro é isso ou não")

print(baseAlgorithm.get_message_and_image(img))


