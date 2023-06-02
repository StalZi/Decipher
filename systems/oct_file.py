def oct_dec(oct_string:str) -> str:
    if oct_string.endswith("\\"):
        oct_string = oct_string[:-1]
    return (bytes([ord(c) for c in oct_string.replace(" ", "\\")])).decode("unicode_escape")