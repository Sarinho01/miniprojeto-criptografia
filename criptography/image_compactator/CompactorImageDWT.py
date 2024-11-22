import pywt
from PIL import Image

from criptography.image_compactator.CompactorImage import CompactImage


def embed_message(sub_band, message_bits):
    flat_sub_band = sub_band.flatten()
    for i, bit in enumerate(message_bits):
        flat_sub_band[i] = (int(flat_sub_band[i]) & ~1) | int(bit)
    return flat_sub_band.reshape(sub_band.shape)


def extract_message(sub_band, message_size):
    message_start = message_size[0]
    message_size_value = message_size[1]

    flat_sub_band = sub_band.flatten()
    message_bits = []
    for i, bit in enumerate(flat_sub_band):
        if i > message_size_value:
            return message_bits

        message_bits.append(int(flat_sub_band[i + message_start]) & 1)

    return message_bits


class CompactImageDWT(CompactImage):

    def compact_image_and_put_lsb_message(self, image, message_bits):
        coeffs = pywt.dwt2(image, 'haar')
        ll, (lh, hl, hh) = coeffs
        ll_with_message = embed_message(ll, message_bits)
        coeffs2 = (ll_with_message, (lh, hl, hh))
        compressed_image = pywt.idwt2(coeffs2, 'haar')

        return compressed_image

    def unpack_image_and_get_lsb_bits(self, image, message_size):
        coeffs = pywt.dwt2(image, 'haar')
        ll, (_, _, _) = coeffs
        print(ll.flatten())
        message_bits = extract_message(ll, message_size)
        return message_bits
