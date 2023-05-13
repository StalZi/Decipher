
alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def caesar_dec(language:str, rot:str, value:str) -> str:

    try:
        rot = int(rot)
    except:
        pass

    result = ""

    print(value)
    print(rot)

    if language == "Все, что ниже":

        if rot == "All":
            print("rot is all")
        
        else:

            for i in range(len(value)):

                if value[i] in alphabetRU:
                    result += alphabetRU[alphabetRU.find(value[i]) - rot]

                elif value[i] in alphabetRU.upper():
                    result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) - rot]

                elif value.lower()[i] in alphabetEN:
                    result += alphabetEN[alphabetEN.find(value.lower()[i]) - rot]

                elif value[i] in alphabetEN.upper():
                    result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) - rot]

                else:
                    result += value[i]
                    
            print(result)

    elif language == "Русский":

        if rot == "All":
            print("rot is all")
        

        else:

            for i in range(len(value)):

                if value[i] in alphabetRU:
                    result += alphabetRU[alphabetRU.find(value[i]) - rot]

                elif value[i] in alphabetRU.upper():
                    result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) - rot]

                else:
                    result += value[i]
                    
            
            print(result)

    elif language == "English":
        
        if rot == "All":
            print("rot is all")

        else:

            for i in range(len(value)):

                if value.lower()[i] in alphabetEN:
                    result += alphabetEN[alphabetEN.find(value.lower()[i]) - rot]

                elif value[i] in alphabetEN.upper():
                    result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) - rot]

                else:
                    result += value[i - 1]
        
            print(result)

    return result