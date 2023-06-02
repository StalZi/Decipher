def hex_dec(hex_string:str) -> str:
    return bytes.fromhex(hex_string).decode('utf-8')