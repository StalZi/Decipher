#
#   Uses Kryptor because i couldn't handle this shit
#

from kryptor.hill_cipher import HillCipher


def hill_dec(value:str, key:list):
    
    return HillCipher.decrypt(value, key)