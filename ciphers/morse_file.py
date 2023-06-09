def morse_dec(morse_string:str, dash:str = "-", dot:str = ".") -> str:
    decode_table = {
    f'{dot}{dash}': 'A',
    f'{dash}{dot}{dot}{dot}': 'B',
    f'{dash}{dot}{dash}{dot}': 'C',
    f'{dash}{dot}{dot}': 'D',
    f'{dot}': 'E',
    f'{dot}{dot}{dash}{dot}': 'F',
    f'{dash}{dash}{dot}': 'G',
    f'{dot}{dot}{dot}{dot}': 'H',
    f'{dot}{dot}': 'I',
    f'{dot}{dash}{dash}{dash}': 'J',
    f'{dash}{dot}{dash}': 'K',
    f'{dot}{dash}{dot}{dot}': 'L',
    f'{dash}{dash}': 'M',
    f'{dash}{dot}': 'N',
    f'{dash}{dash}{dash}': 'O',
    f'{dot}{dash}{dash}{dot}': 'P',
    f'{dash}{dash}{dot}{dash}': 'Q',
    f'{dot}{dash}{dot}': 'R',
    f'{dot}{dot}{dot}': 'S',
    f'{dash}': 'T',
    f'{dot}{dot}{dash}': 'U',
    f'{dot}{dot}{dot}{dash}': 'V',
    f'{dot}{dash}{dash}': 'W',
    f'{dash}{dot}{dot}{dash}': 'X',
    f'{dash}{dot}{dash}{dash}': 'Y',
    f'{dash}{dash}{dot}{dot}': 'Z',
    f'{dash}{dash}{dash}{dash}{dash}': '0',
    f'{dot}{dash}{dash}{dash}{dash}': '1',
    f'{dot}{dot}{dash}{dash}{dash}': '2',
    f'{dot}{dot}{dot}{dash}{dash}': '3',
    f'{dot}{dot}{dot}{dot}{dash}': '4',
    f'{dot}{dot}{dot}{dot}{dot}': '5',
    f'{dash}{dot}{dot}{dot}{dot}': '6',
    f'{dash}{dash}{dot}{dot}{dot}': '7',
    f'{dash}{dash}{dash}{dot}{dot}': '8',
    f'{dash}{dash}{dash}{dash}{dot}': '9',
    f'{dot}{dash}{dot}{dash}{dot}{dash}': '.',
    f'{dash}{dash}{dot}{dot}{dash}{dash}': ':',
    f'{dot}{dot}{dash}{dash}{dot}{dot}': '?',
    f'SPACE': ' '
    }

    symbols = morse_string.replace("   ", " SPACE ").split(" ")
    return "".join(decode_table[x] for x in symbols)