alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

l2iRU = dict(zip(alphabetRU, range(len(alphabetRU))))
l2iEN = dict(zip(alphabetEN, range(len(alphabetEN))))

i2lRU = dict(zip(range(len(alphabetRU)), alphabetRU))
i2lEN = dict(zip(range(len(alphabetEN)), alphabetEN))


def vigenereRU(split_encrypted, key):
    decrypted = ""

    for each_split in split_encrypted:
            
            i = 0

            for letter in each_split:
                try:
                    number = (l2iRU[letter] - l2iRU[key[i]]) % len(alphabetRU)
                    decrypted += i2lRU[number]
                except:
                    decrypted = "Bad symbols in the entry"
                    return decrypted
                i += 1

    return decrypted

def vigenereEN(split_encrypted, key):
    decrypted = ""

    for each_split in split_encrypted:
            
            i = 0

            for letter in each_split:
                try:
                    number = (l2iEN[letter] - l2iEN[key[i]]) % len(alphabetEN)
                    decrypted += i2lEN[number]
                except:
                    decrypted = "Bad symbols in the entry"
                    return decrypted
                i += 1

    return decrypted

def vigenere_dec(language:str, value:str, key:str, rot:str) -> str:

    try:
        rot = int(rot)
    except:
        pass

    value = value.lower()
    
    if rot == 1 or rot == "All":

        valueR1 = ""

        for i in range(len(value)):

            if value[i] in alphabetRU:
                valueR1 += alphabetRU[alphabetRU.find(value[i]) - 1]

            elif value[i] in alphabetRU.upper():
                valueR1 += alphabetRU.upper()[alphabetRU.upper().find(value[i]) - 1]

            elif value.lower()[i] in alphabetEN:
                valueR1 += alphabetEN[alphabetEN.find(value.lower()[i]) - 1]

            elif value[i] in alphabetEN.upper():
                valueR1 += alphabetEN.upper()[alphabetEN.upper().find(value[i]) - 1]

            else:
                valueR1 += value[i]

        split_encryptedR1 = [
        valueR1[i : i + len(key)] for i in range(0, len(valueR1), len(key))
    ]
    


    split_encrypted = [
        value[i : i + len(key)] for i in range(0, len(value), len(key))
    ]
    


    if language == "Русский":

        if rot == 0:

            return vigenereRU(split_encrypted, key)
        
        elif rot == 1:

            return vigenereRU(split_encryptedR1, key)
        
        else:
            return [vigenereRU(split_encrypted, key), vigenereRU(split_encryptedR1, key)]

    elif language == "English":
            
        if rot == 0:

            return vigenereEN(split_encrypted, key)
        
        elif rot == 1:
             
            return vigenereEN(split_encryptedR1, key)
        
        else:
            return [vigenereEN(split_encrypted, key), vigenereEN(split_encryptedR1, key)]
