from base64 import b64decode

def base64_dec(base64_string:str) -> str:
    return str(b64decode(base64_string))[2:-1]