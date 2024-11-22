# import pywt
# import numpy as np
# from PIL import Image
#
#
# image_path = 'imagem.png'
#
#
# img = Image.open(image_path).convert('L')
# coeffs = pywt.dwt2(img, 'haar')
# (LL, (LH, HL, HH)) = coeffs
# LL_flaten = LL.flatten()
#
# print(LL_flaten[2])
# c_value = int(LL_flaten[2])
# print(c_value)
# bit = 0
# LL_flaten[2] = c_value & ~1 | bit
# print(LL_flaten[2])
#
# LL_shaped = LL_flaten.reshape(LL.shape)
# modified_coeffs = (LL_shaped, (LH, HL, HH))
#
# img_s = pywt.idwt2(modified_coeffs, 'haar')
#
# test = pywt.dwt2(img_s, 'haar')
#
# img_s = np.clip(img_s, 0, 255).astype(np.uint8)
#
# # Converter a matriz NumPy de volta para uma imagem PIL
# img_s_pil = Image.fromarray(img_s)
# # Salvar a imagem em um arquivo
# img_s_pil.save("imagem_reconstruida.png")
#
# img = Image.open("imagem_reconstruida.png").convert('L')
# coeffs = pywt.dwt2(img, 'haar')
#
# (LL2, (LH, HL, HH)) = test
# a = int(LL2.flatten()[2])
# print(LL2.flatten()[2])
# print(a & 1 )
#
# print(type(LL.shape))
#



import numpy as np
from PIL import Image

from criptography.image_compactator.CompactorImage import bits_to_bytes
from criptography.image_compactator.CompactorImageDWT import CompactImageDWT

# Imagem de exemplo (substitua por sua imagem real)
img_path = "imagem.png"

message = "testando testando"
message_bytes = message.encode()
bit_array = [int(bit) for byte in message_bytes for bit in bin(byte)[2:].zfill(8)]
print(bit_array)
c = CompactImageDWT()

img_s = c.compact_image_and_put_lsb_message(Image.open(img_path), bit_array)

message_bits_uncrypt = c.unpack_image_and_get_lsb_bits(img_s, (0,len(bit_array) - 1))

a = bits_to_bytes(message_bits_uncrypt)
print(bytes(a))


