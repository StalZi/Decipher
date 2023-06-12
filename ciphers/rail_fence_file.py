def decryptRailFence(cipher:str, key:int) -> str:

    rail = [['\n' for i in range(len(cipher))]
                for j in range(key)]
     
    dir_down = None
    row, col = 0, 0
     
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        if dir_down:
            row += 1
        else:
            row -= 1

    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
            (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1

    result = []
    row, col = 0, 0

    for i in range(len(cipher)):
         
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
             
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
             
        if dir_down:
            row += 1
        else:
            row -= 1

    return("".join(result))


def rail_fence_dec(value:str, key:int|str) -> str:
    
    if key == "All":
        all_nums = []

        for i in range(2, 101):

            all_nums.append(decryptRailFence(value, i))
        
        return all_nums

    else:

        return decryptRailFence(value, int(key))