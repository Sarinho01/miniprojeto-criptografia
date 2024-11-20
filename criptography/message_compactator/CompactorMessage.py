from abc import ABC, abstractmethod


class CompactMessage(ABC):

    @abstractmethod
    def compact_message(self, message):
        pass

    @abstractmethod
    def unpack_message(self, message_bits, extra_information):
        pass