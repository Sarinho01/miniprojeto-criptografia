import time

import numpy as np
from Crypto.PublicKey import RSA
from PIL import Image
from skimage.metrics import structural_similarity as ssim

from algorithm.BasePaperAlgorithm import BasePaperAlgorithm
from algorithm.ImprovementAlgorithm import ImprovedAlgorithm
from algorithm.PaperAlgorithm import PaperAlgorithm
from criptography.image_compactator.CompactorImageDWT import CompactImageDWT
from criptography.message_compactator.HuffmanCompactor import HuffmanCompactMessage
from criptography.message_encryption.RSACryptographyMessage import RSAEncryptMessage


def structural_similarity_index(image1, image2):
    image1_gray = np.mean(image1, axis=-1) if image1.ndim == 3 else image1
    image2_gray = np.mean(image2, axis=-1) if image2.ndim == 3 else image2

    image1_gray = image1_gray.astype(np.float32)
    image2_gray = image2_gray.astype(np.float32)

    data_range = image1_gray.max() - image1_gray.min()
    ssim_value, _ = ssim(image1_gray, image2_gray, full=True, data_range=data_range)

    return ssim_value


def mean_squared_error(image1, image2):
    difference = image1.astype(np.float32) - image2.astype(np.float32)
    squared_difference = difference ** 2

    mse = np.mean(squared_difference)
    return mse


def test_model_image(algorithm: PaperAlgorithm, image, message_data, name):
    start_time = time.time()

    image_result = algorithm.put_message_in_image_and_compact(image, message_data)

    compression_time = time.time() - start_time

    continue_time = time.time()
    _ = algorithm.get_message_and_image(image_result)

    extracting_time = time.time() - continue_time
    total_time = time.time() - start_time

    image_result = Image.fromarray(image_result).convert("L")

    image_result = np.array(image_result)
    image = np.array(image)

    mse = mean_squared_error(image, image_result)  #
    psnr = 10 * np.log10((255.0 ** 2) / mse)  #
    ssim_data = structural_similarity_index(image, image_result)  #

    print(f"\n{name}: ")
    print(f"MSE: {mse:.4f}")
    print(f"PSNR: {psnr:.4f}")
    print(f"SSIM: {ssim_data:.4f}")
    print(f"Encrypting time: {compression_time:.4f}")
    print(f"Extracting time: {extracting_time:.4f}")
    print(f"Total time: {total_time:.4f}")


images = [
    (Image.open("resources/arara_imagem.png").convert("L"), "arara"),
    (Image.open("resources/aviao_imagem.png").convert("L"), "aviao"),
    (Image.open("resources/navio_imagem.png").convert("L"), "navio"),
    (Image.open("resources/loira_imagem.png").convert("L"), "loira")
]

keyBase = RSA.generate(2048)
message = "orem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum." * 15
print(len(message))
encryptMessage = RSAEncryptMessage(keyBase.public_key(), keyBase)
compactImage = CompactImageDWT()
compactMessage = HuffmanCompactMessage()

baseAlgorithm = BasePaperAlgorithm(compactMessage, encryptMessage, compactImage)
improvedAlgorithm = ImprovedAlgorithm(compactMessage, encryptMessage, compactImage)

print("Base algorithm: \n")

for pair in images:
    test_model_image(baseAlgorithm, pair[0], message, pair[1])
print("-------------------------------------------------------------------")
print("Improved algorithm: \n")

for pair in images:
    test_model_image(improvedAlgorithm, pair[0], message, pair[1])
