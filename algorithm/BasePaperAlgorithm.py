from algorithm.PaperAlgorithm import PaperAlgorithm
import json


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
        return combined_bits

    def get_message_and_image(self, image, json):
        pass

