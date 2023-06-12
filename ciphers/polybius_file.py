from re import sub

def generate_array(alphabet:str, key:str) -> list:

    array = []
    _tmp = []
    key = sub(r'[^a-zA-Z]+', '', key)  # remove non-alpha character
    key = key.upper()

    if key:
        for k in key:
            alphabet = alphabet.replace(k, '')

        alphabet = key + alphabet

    for y in range(5):
        for x in range(5):
            _tmp.append(alphabet[0 + 5 * y + x])
        array.append(_tmp)
        _tmp = []

    return array

def decode(numbers:str, array:list) -> str:

    numbers = sub(r'[\D]+', '', numbers)  # remove non-digit character

    text = ''

    for number in range(0, len(numbers), 2):
        try:
            oy = int(numbers[number]) - 1
            ox = int(numbers[number + 1]) - 1
            text += array[oy][ox]
        except IndexError:
            pass
        continue

    return text

def polybius_dec(value:str, alphabet:str, key:str = '') -> str:
        decrypted = decode(value, generate_array(alphabet, key))
        
        if decrypted != "":
            return decrypted
        else:
            return "Bad symbols were given"