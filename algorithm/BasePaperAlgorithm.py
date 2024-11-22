from algorithm.PaperAlgorithm import PaperAlgorithm
import json

from criptography.image_compactator.CompactorImage import bits_to_bytes


def create_json(codebook, message_size):
    json_data = {
        "message_size": message_size,
        "huffman_codebook": codebook
    }

    return json.dumps(json_data)


class BasePaperAlgorithm(PaperAlgorithm):
    def put_message_in_image_and_compact(self, image, message):
        message_encrypted = self.encrypt_message.encrypt_message_and_put_in_base64(message)
        message_compressed_bits, codebook = self.compactor_message.compact_message(message_encrypted)

        json_data = create_json(codebook, len(message_compressed_bits))

        json_encrypted = self.encrypt_message.encrypt_message(json_data)

        json_encrypted_bits_array = [int(bit) for byte in json_encrypted for bit in format(byte, '08b')]

        json_encrypted_bits_size = len(json_encrypted_bits_array)
        json_encrypted_bits_size_array_bits = [int(bit) for bit in format(json_encrypted_bits_size, '032b')]

        combined_bits = json_encrypted_bits_size_array_bits + json_encrypted_bits_array + message_compressed_bits

        image_embed_message = self.compact_image.compact_image_and_put_lsb_message(image, combined_bits)

        return image_embed_message

    def get_message_and_image(self, image):
        current_index = 0

        json_size_bits = self.compact_image.unpack_image_and_get_lsb_bits(image, (current_index, 31))
        current_index += 32

        json_size = int.from_bytes(bits_to_bytes(json_size_bits))

        json_data_encrypted_bits = self.compact_image.unpack_image_and_get_lsb_bits(image, (current_index, json_size - 1))
        current_index = json_size + current_index

        json_data = self.encrypt_message.dencrypt_message(bits_to_bytes(json_data_encrypted_bits))

        json_data = json.loads(json_data)

        codebook = json_data["huffman_codebook"]
        message_size = json_data["message_size"]

        message_compressed_bites = self.compact_image.unpack_image_and_get_lsb_bits(image, (current_index, message_size - 1))

        message_encrypted_base64 = self.compactor_message.unpack_message(message_compressed_bites, codebook)

        message_bytes = self.encrypt_message.dencrypt_message_in_base64(message_encrypted_base64)

        return message_bytes
