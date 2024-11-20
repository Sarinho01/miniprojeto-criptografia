import collections

import huffman

from criptography.message_compactator.CompactorMessage import CompactMessage


class HuffmanCompactMessage(CompactMessage):

    def compact_message(self, message):
        codebook = huffman.codebook(collections.Counter(message).items())

        text_bytes = "".join([codebook[char] for char in message])

        return [int(bit) for bit in text_bytes], codebook


    def unpack_message(self, message_bits, extra_information):
        codebook_inverted = {v: k for k, v in extra_information.items()}

        message = ""
        current_bits = ""
        for bite in message_bits:
            current_bits += str(bite)
            if current_bits in codebook_inverted:
                message += codebook_inverted[current_bits]
                current_bits = ""

        return message