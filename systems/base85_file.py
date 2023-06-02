from base64 import a85decode

def base85_dec(base85_string:str) -> str:
    return str(a85decode(base85_string))[2:-1]