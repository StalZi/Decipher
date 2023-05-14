alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def atbashALL(value:str) -> str:
    result = ""

    for i in range(len(value)):
            
            if value[i] in alphabetRU:

                result += alphabetRU[len(alphabetRU) - alphabetRU.find(value[i]) - 1]

            elif value[i] in alphabetEN:
                 
                result += alphabetEN[len(alphabetEN) - alphabetEN.find(value[i]) - 1]

            else:

                result += value[i]

    return result

def atbashRU(value:str) -> str:
    result = ""

    for i in range(len(value)):
            
            if value[i] in alphabetRU:

                result += alphabetRU[len(alphabetRU) - alphabetRU.find(value[i])]

            else:

                result += value[i]

    return result

def atbashEN(value:str) -> str:
    result = ""

    for i in range(len(value)):
            
            if value[i] in alphabetRU:

                result += alphabetEN[len(alphabetEN) - alphabetEN.find(value[i])]

            else:
                result += value[i]

    return result

def atbash_dec(language:str, value:str) -> str:

    if language == "Все, что ниже":

        return atbashALL(value)


    elif language == "Русский":

        return atbashRU(value)


    elif language == "English":

        return atbashEN(value)