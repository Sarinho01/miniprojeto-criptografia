from abc import ABC, abstractmethod

class CompactImage(ABC):

    @abstractmethod
    def compact_image_and_put_lsb_message(self, image_path, message_bits):
        pass

    @abstractmethod
    def unpack_image_and_get_lsb_bits(self, image_path, extra_information):
        pass
