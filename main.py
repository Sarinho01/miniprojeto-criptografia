import time

from Crypto.PublicKey import RSA
from PIL import Image

from algorithm.BasePaperAlgorithm import BasePaperAlgorithm
from algorithm.ImprovementAlgorithm import ImprovedAlgorithm
from criptography.image_compactator.CompactorImageDWT import CompactImageDWT
from criptography.message_compactator.HuffmanCompactor import HuffmanCompactMessage
from criptography.message_encryption.RSACryptographyMessage import RSAEncryptMessage

keyBase = RSA.generate(2048)
message = "teste do saro é isso ou não" * 100
encryptMessage = RSAEncryptMessage(keyBase.public_key(), keyBase)
compactImage = CompactImageDWT()
compactMessage = HuffmanCompactMessage()

current_time = time.time()
baseAlgorithm = BasePaperAlgorithm(compactMessage, encryptMessage, compactImage)
img = baseAlgorithm.put_message_in_image_and_compact(Image.open("imagem.png"), message)
result = baseAlgorithm.get_message_and_image(img)
print(result)
print(time.time() - current_time)

 # ----------------------------------------------------------------------------------------------------------------------

current_time = time.time()
improvedAlgorithm = ImprovedAlgorithm(compactMessage, encryptMessage, compactImage)
img = improvedAlgorithm.put_message_in_image_and_compact(Image.open("imagem.png"), message.encode())
result = improvedAlgorithm.get_message_and_image(img)
print(result)
print(time.time() - current_time)

