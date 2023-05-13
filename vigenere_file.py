alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

l2iRU = dict(zip(alphabetRU, range(len(alphabetRU))))
l2iEN = dict(zip(alphabetEN, range(len(alphabetEN))))

i2lRU = dict(zip(range(len(alphabetRU)), alphabetRU))
i2lEN = dict(zip(range(len(alphabetEN)), alphabetEN))

def vigenere_dec(value:str, language:str, key:str = None) -> str:

    value = value.lower()
    
    decrypted = ""
    split_encrypted = [
        value[i : i + len(key)] for i in range(0, len(value), len(key))
    ]
    
    if language == "Русский":
        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (l2iRU[letter] - l2iRU[key[i]]) % len(alphabetRU)
                decrypted += i2lRU[number]
                i += 1

    elif language == "English":

        for each_split in split_encrypted:
            i = 0
            for letter in each_split:
                number = (l2iEN[letter] - l2iEN[key[i]]) % len(alphabetEN)
                decrypted += i2lEN[number]
                i += 1

    return decrypted
