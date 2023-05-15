def fence(lst, numrails):
    fence = [[None] * len(lst) for n in range(numrails)]
    rails = range(numrails - 1) + range(numrails - 1, 0, -1)
    
    for n, x in enumerate(lst):
        fence[rails[n % len(rails)]][n] = x

    return [c for rail in fence for c in rail if c is not None]


def rail_fence_decode(text, n):
    rng = range(len(text))
    pos = fence(rng, n)
    return ''.join(text[pos.index(n)] for n in rng)


def rail_fence_dec(value:str, key:int|str):
    
    if key == "All":
        all_nums = []

        for i in range(1, 101):

            all_nums.append(rail_fence_decode(value, i))
        
        return all_nums

    else:

        return rail_fence_decode(value, int(key))