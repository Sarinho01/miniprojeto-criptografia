def bits_to_bytes(bit_array):
    if len(bit_array) % 8 != 0:
        raise ValueError("O array de bits deve ter um comprimento múltiplo de 8.")

    byte_array = []
    for i in range(0, len(bit_array), 8):
        byte = int("".join(map(str, bit_array[i:i + 8])), 2)
        byte_array.append(byte)

    return bytes(byte_array)