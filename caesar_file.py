alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def caesarALL(value:str, rot:int) -> str:

    result = ""
    increment = 0

    for i in range(len(value)):
            print(i)
            if value[i] in alphabetRU:
                result += alphabetRU[alphabetRU.find(value[i]) - rot]

            elif value[i] in alphabetRU.upper():
                result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) - rot]

            elif value.lower()[i] in alphabetEN:
                while True:
                    try:
                        result += alphabetEN[alphabetEN.find(value[i]) - rot + increment]
                        break
                    except:
                        increment += 26
                    

            elif value[i] in alphabetEN.upper():
                while True:
                    try:
                        result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) - rot + increment]
                        break
                    except:
                        increment += 26

            else:
                result += value[i]

    return result


def caesarRU(value:str, rot:int) -> str:

    result = ""

    for i in range(len(value)):

        if value[i] in alphabetRU:
            result += alphabetRU[alphabetRU.find(value[i]) - rot]

        elif value[i] in alphabetRU.upper():
            result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) - rot]

        else:
            result += value[i]

    return result


def caesarEN(value:str, rot:int) -> str:

    result = ""

    for i in range(len(value)):

        if value.lower()[i] in alphabetEN:
            result += alphabetEN[alphabetEN.find(value.lower()[i]) - rot]

        elif value[i] in alphabetEN.upper():
            result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) - rot]

        else:
            result += value[i - 1]

    return result
                

def caesar_dec(language:str, value:str, rot:str) -> str:

    try:
        rot = int(rot)
    except:
        pass

    resultall = []


    if language == "Все, что ниже":

        if rot == "All":

            for i in range(1, 33):

                resultall.append(caesarALL(value, i))

            return resultall
        
        else:

            return caesarALL(value, rot)

    elif language == "Русский":

        if rot == "All":

            for i in range(1, len(alphabetRU)):

                resultall.append(caesarRU(value, i))

            return resultall
        
        else:

            return caesarRU(value, rot)


    elif language == "English":
        
        if rot == "All":

            for i in range(1, len(alphabetEN)):

                resultall.append(caesarEN(value, i))

            return resultall

        else:

            return caesarEN(value, rot)