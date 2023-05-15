alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def a1z26RU(value:list) -> str:
    result = ""

    for i in range(len(value)):
         
         splitted = value[i].split("-")

         for j in range(len(splitted)):

            result += alphabetRU[int(splitted[j]) - 1]

    return result

def a1z26EN(value:list) -> str:
    result = ""

    for i in range(len(value)):
         
         splitted = value[i].split("-")

         for j in range(len(splitted)):

            result += alphabetEN[int(splitted[j]) - 1]

    return result


def a1z26_dec(language:str, value:str) -> str:

    value = value.split(" ")

    if language == "Все, что ниже":
        try:
            return [a1z26EN(value), a1z26RU(value)]
        except:
            return a1z26RU(value)

    elif language == "Русский":

        return a1z26RU(value)


    elif language == "English":

        return a1z26EN(value)