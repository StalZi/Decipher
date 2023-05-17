import numpy as np
from egcd import egcd

alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

l2iRU = dict(zip(alphabetRU, range(len(alphabetRU))))
l2iEN = dict(zip(alphabetEN, range(len(alphabetEN))))
i2lRU = dict(zip(range(len(alphabetRU)), alphabetRU))
i2lEN = dict(zip(range(len(alphabetEN)), alphabetEN))

def matrix_mod_inv(matrix, modulus):

    det = int(np.round(np.linalg.det(np.float64(matrix))))
    det_inv = egcd(det, modulus)[1] % modulus
    matrix_modulus_inv = (
        det_inv * np.round(det * np.linalg.inv(np.float64(matrix))).astype(int) % modulus
    )

    return matrix_modulus_inv

def decryptEN(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(l2iEN[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabetEN)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += i2lEN[number]

    print(decrypted)
    return decrypted


def decryptRU(cipher, Kinv):
    decrypted = ""
    cipher_in_numbers = []

    for letter in cipher:
        cipher_in_numbers.append(l2iRU[letter])

    split_C = [
        cipher_in_numbers[i : i + int(Kinv.shape[0])]
        for i in range(0, len(cipher_in_numbers), int(Kinv.shape[0]))
    ]

    for C in split_C:
        C = np.transpose(np.asarray(C))[:, np.newaxis]
        numbers = np.dot(Kinv, C) % len(alphabetRU)
        n = numbers.shape[0]

        for idx in range(n):
            number = int(numbers[idx, 0])
            decrypted += i2lRU[number]

    return decrypted


def hill_dec(language:str, value:str, key:list):

    K = np.matrix(key)

    match language:
        case "Русский":
            Kinv = matrix_mod_inv(K, len(alphabetRU))
            return decryptRU(value, Kinv)
        case "English":
            Kinv = matrix_mod_inv(K, len(alphabetEN))
            return decryptEN(value, Kinv)