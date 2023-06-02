from base64 import b32decode

def base32_dec(base32_string:str) -> str:
    return str(b32decode(base32_string))[2:-1]