from abc import ABC, abstractmethod


def bits_to_bytes(bit_array):
    if len(bit_array) % 8 != 0:
        raise ValueError("O array de bits deve ter um comprimento múltiplo de 8.")

    byte_array = []
    for i in range(0, len(bit_array), 8):
        byte = int("".join(map(str, bit_array[i:i + 8])), 2)
        byte_array.append(byte)

    return bytes(byte_array)

class CompactImage(ABC):

    @abstractmethod
    def compact_image_and_put_lsb_message(self, image_path, message_bits):
        pass

    @abstractmethod
    def unpack_image_and_get_lsb_bits(self, image_path, extra_information):
        pass
