from Crypto.PublicKey import RSA
from PIL import Image

from algorithm.ImprovementAlgorithm import ImprovedAlgorithm
from criptography.image_compactator.CompactorImageDWT import CompactImageDWT
from criptography.message_compactator.HuffmanCompactor import HuffmanCompactMessage
from criptography.message_encryption.RSACryptographyMessage import RSAEncryptMessage

keyBase = RSA.generate(2048)
encryptMessageImproved = RSAEncryptMessage(keyBase.public_key(), keyBase)
compactImageImproved = CompactImageDWT()
compactMessageImproved = HuffmanCompactMessage()
baseAlgorithm = ImprovedAlgorithm(compactMessageImproved, encryptMessageImproved, compactImageImproved)

img = baseAlgorithm.put_message_in_image_and_compact(Image.open("resources/loira_imagem.png"), "teste do saro é isso ou não")

result = baseAlgorithm.get_message_and_image(img)
print(result)

