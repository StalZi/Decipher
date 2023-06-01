def bin_dec(bin_string:str) -> str:
    result = []
    bin_string = bin_string.split(" ")
    
    for i in range(len(bin_string)):
        result.append(''.join(chr(int(bin_string[i][j*8:j*8+8],2)) for j in range(len(bin_string[i])//8)))

    return " ".join(result)