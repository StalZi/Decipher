from customtkinter import *

from options import *
from char_lim import *

from ciphers.caesar_file import caesar_dec
from ciphers.vigenere_file import vigenere_dec
from ciphers.atbash_file import atbash_dec
from ciphers.playfair_file import playfair_dec
from ciphers.A1Z26_file import a1z26_dec
from ciphers.hill_file import hill_dec
from ciphers.rail_fence_file import rail_fence_dec


VERSION = "1.4"

set_appearance_mode("dark")
set_default_color_theme("green")


def check(event):
    global keyText_trace_id

    dropdownLanguage.configure(state=NORMAL)
    checkboxVar.set(0)
    checkbox.place_forget()
    try:
        keyText.trace_vdelete("w", keyText_trace_id)
    except:
        pass

    if matrix_title.winfo_exists():

        matrix_title.place_forget()
        matrix_label.place_forget()

        matrix1.place_forget()
        matrix2.place_forget()
        matrix3.place_forget()
        matrix4.place_forget()

    match event:
        case "Цезарь":

            if dropdownRots.get() == "ROT?":
                button.configure(state=DISABLED)

            if dropdownLanguage.get() != "Язык?":
                dropdownRots.configure(state=NORMAL)
                if dropdownLanguage.get() == "Russian" or dropdownLanguage.get() == "Все, что ниже":
                    dropdownRots.configure(values=RotsRU)
                else:
                    dropdownRots.configure(values=RotsEN)

            keyEntry.grid_forget()
            dropdownLanguage.configure(values=whatLang)

            dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)
            dropdownRots.grid(row=0,column=2,padx=15,pady=20)

        case "Атбаш" | "A1Z26":

            if dropdownLanguage.get() != "Язык?":
                button.configure(state=NORMAL)

            dropdownRots.grid_forget()
            keyEntry.grid_forget()


            dropdownLanguage.grid(row=0,column=1)
            dropdownLanguage.configure(values=whatLang)

        case "Рейл":
            button.configure(state=NORMAL)

            dropdownLanguage.grid_forget()
            dropdownRots.grid_forget()
            keyEntry.grid_forget()

            keyEntry.configure(width=100)
            keyEntry.grid(row=0,column=1,padx=10,pady=20)

            keyText_trace_id = keyText.trace("w", lambda *args: character_limit3(keyText))

            checkbox.place(in_=keyEntry,relx=1.0,rely=0,x=10,y=0)
        
        case "Плейфер":

            dropdownRots.grid_forget()
            dropdownLanguage.set("English")
            dropdownLanguage.configure(state=DISABLED)
            button.configure(state=NORMAL)

            keyEntry.grid(row=1,column=1,pady=8)

        case "Виженер":

            if dropdownRots.get() == "ROT?":
                button.configure(state=DISABLED)
            
            if dropdownLanguage.get() == "Все, что ниже":
                dropdownLanguage.set("Язык?")
                dropdownRots.configure(state=DISABLED)

            else:
                dropdownRots.configure(state=NORMAL)

            if dropdownRots.get() != "0" and dropdownRots.get() != "1" and dropdownRots.get() != "All":
                dropdownRots.set("ROT?")
                button.configure(state=DISABLED)

            dropdownLanguage.configure(values=whatLangCut)
            dropdownRots.configure(values=RotsVG)

            keyEntry.grid(row=1,column=1,pady=8)

            dropdownRots.grid(row=0,column=2,padx=15,pady=20)
            
        case "Хилл":
            button.configure(state=NORMAL)

            dropdownLanguage.configure(values=whatLangCut)
            if dropdownLanguage.get() == "Все, что ниже":
                dropdownLanguage.set("Язык?")
                dropdownRots.configure(state=DISABLED)
                button.configure(state=DISABLED)

            dropdownRots.grid_forget()
            keyEntry.grid_forget()

            dropdownLanguage.grid(row=0,column=1)

            matrix_title.place(x=200,y=100)
            matrix_label.place(x=130,y=135)

            matrix1.place(x=147,y=135)
            matrix2.place(x=197,y=135)
            matrix3.place(x=255,y=135)
            matrix4.place(x=305,y=135)


    window.update()

    return


def checkLanguage(event):

    global RotsEN
    global RotsRU
    
    match dropdownCipher.get():
        case "Виженер":

            dropdownRots.configure(values=RotsVG)
            dropdownRots.configure(state=NORMAL)

            window.update()
            return
        
        case "Цезарь":

            if event == "Все, что ниже" or event == "Русский":
                dropdownRots.configure(values=RotsRU)

            elif event == "English":
                dropdownRots.configure(values=RotsEN)

            dropdownRots.configure(state=NORMAL)

            window.update()
            return
        
        case "Атбаш" | "A1Z26":

            button.configure(state=NORMAL)

            window.update()
            return


def checkRot(event):

    button.configure(state=NORMAL)

def checkCheckbox():

    if checkboxVar.get() == 1:
        keyEntry.delete(0, END)
        keyEntry.configure(state=DISABLED)
        
    else:
        keyEntry.configure(state=NORMAL)


def decipher(*event):
    if button.cget('state') == DISABLED:
        return
    
    try:
        copy_button.destroy()
        label.destroy()
    except:
        pass

    manyFrame.place_forget()

    try:
        for widget in manyLabels:
            widget.pack_forget()
    except:
        pass

    if cipherEntry.get() != "":

        match dropdownCipher.get():
            
            case "Цезарь":

                after_dec(caesar_dec(dropdownLanguage.get(), cipherEntry.get(), dropdownRots.get()))

            case "Виженер" if keyText != "":
                
                try:
                    after_dec(vigenere_dec(dropdownLanguage.get(), cipherEntry.get(), keyText.get(), dropdownRots.get()))
                except:
                    after_dec("Bad symbols in the entry")

            case "Атбаш":

                after_dec(atbash_dec(dropdownLanguage.get(), cipherEntry.get()))

            case "Плейфер" if keyText != "":

                try:
                    after_dec(playfair_dec(cipherEntry.get(), keyText.get()))
                except:
                    after_dec("Bad symbols (!, ?, ., etc.) or the key is incorrect")

            case "Плейфер" if keyText != "":

                try:
                    after_dec(playfair_dec(cipherEntry.get(), keyText.get()))
                except:
                    after_dec("Bad symbols (!, ?, ., etc.) or the key is incorrect")

            case "A1Z26":

                try:
                    after_dec(a1z26_dec(dropdownLanguage.get(), cipherEntry.get()))
                except:
                    after_dec("Bad symbols (should be 1-2-15-2-1, etc.)")

            case "Рейл" if keyText != "":

                try:
                    if checkboxVar.get() == 1:
                        after_dec(rail_fence_dec(cipherEntry.get(), "All"))
                    else:
                        after_dec(rail_fence_dec(cipherEntry.get(), keyText.get()))
                except:
                    after_dec("Bad symbols, the key should be an integer")

            case "Хилл" if matrix1 != "" and matrix2 != "" and matrix3 != "" and matrix4 != "":

                try:
                    after_dec(hill_dec(dropdownLanguage.get(),cipherEntry.get(),[[matrix_text1.get(), matrix_text2.get()],[matrix_text3.get(), matrix_text4.get()]]))
                except:
                    after_dec("""Bad symbols (тут вообще пиздец, так что пишу на русском, возможные проблемы: 
Плохая матрица, спец символы в шифре(пробелы), длина шифра не квадрат числа)""")

            case _:
                return
    else:
        return


def after_dec(deciphed:str|list):
    global label, copy_button, manyLabels

    if len(deciphed) > 127 or isinstance(deciphed, list):
        manyFrame.place(x=0,y=250)

        if isinstance(deciphed, list):
            manyLabels = []

            for i in range(len(deciphed)):

                label = CTkEntry(manyFrame,
                                        font=("Ariel", 24),
                                        fg_color="transparent",
                                        border_width=0,
                                        width=475)
                
                if dropdownCipher.get() == "Виженер":
                    label.insert(0, f"{i} - {deciphed[i]}")
                elif dropdownCipher.get() == "Рейл":
                    label.insert(0, f"{i + 2} - {deciphed[i]}")
                else:
                    label.insert(0, f"{i + 1} - {deciphed[i]}")

                label.configure(state="readonly")

                label.pack(anchor=NW,pady=5)

                manyLabels.append(label)

            window.update()
            return

        label = CTkLabel(manyFrame,
                         font=("Ariel", 40),
                         wraplength=420,
                         width=420,
                         compound=CENTER,
                         text=deciphed)
        
        copy_button = CTkButton(window,
                                text="Copy",
                                width=20,
                                command=copy)
        
        label.pack(anchor=NW,pady=5)
        copy_button.place(x=500,y=500)


    else:

        label = CTkLabel(window,
                         font=("Ariel", 40),
                         wraplength=420,
                         width=420,
                         compound=CENTER,
                         text=deciphed)

        copy_button = CTkButton(window,
                                text="Copy",
                                width=20,
                                command=copy)


        label.place(in_=button,relx=-1.0,rely=1.0,x=0,y=50)
        copy_button.place(in_=label,relx=1.0,rely=0.95,x=0,y=0)


    window.update()


def copy():

    window.clipboard_clear()
    window.clipboard_append(label.cget("text"))


# ---------------------------------------

window = CTk()
window.title(f"Decipher by StalZi {VERSION}")
window.geometry("800x600")
window.resizable(False, True)

# ---------------------------------------

cipherEntry = CTkEntry(window,
                    font=("Arial", 20),
                    width=500,
                    placeholder_text="Cipher")
cipherEntry.pack(anchor=NW)

frame = CTkFrame(window)
frame.pack(anchor=N,fill=BOTH)

dropdownCipher = CTkOptionMenu(frame,
                         values=options,
                         command=check)
dropdownCipher.set("Шифр?")
dropdownCipher.grid(row=0,column=0,padx=10,pady=20)

dropdownLanguage = CTkOptionMenu(frame,
                         values=None,
                         command=checkLanguage,
                         state=DISABLED)
dropdownLanguage.set("Язык?")
dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)

fakeDropdownRots = CTkOptionMenu(window,
                         values=None,
                         command=checkRot,
                         state=DISABLED)
fakeDropdownRots.set("ROT?")

dropdownRots = CTkOptionMenu(frame,
                         values=None,
                         command=checkRot,
                         state=DISABLED)
dropdownRots.set("ROT?")

checkboxVar = IntVar()

checkbox = CTkCheckBox(frame,
                       variable=checkboxVar,
                       text="All",
                       command=checkCheckbox)

matrix_title = CTkLabel(window,
                        text="Матрица",
                        font=("Ariel", 20),
                        compound=CENTER)

matrix_label = CTkLabel(window,
                        text="[[       ,       ],[       ,       ]]",
                        font=("Ariel", 20),
                        compound=CENTER)

matrix_text1 = StringVar()
matrix_text2 = StringVar()
matrix_text3 = StringVar()
matrix_text4 = StringVar()

matrix1 = CTkEntry(window,
                    font=("Arial",15),
                    textvariable=matrix_text1,
                    width=30,
                    placeholder_text="3")
matrix1.insert(0, "3")

matrix2 = CTkEntry(window,
                    font=("Arial",15),
                    textvariable=matrix_text2,
                    width=30,
                    placeholder_text="3")
matrix2.insert(0, "3")

matrix3 = CTkEntry(window,
                    font=("Arial",15),
                    textvariable=matrix_text3,
                    width=30,
                    placeholder_text="2")
matrix3.insert(0, "2")

matrix4 = CTkEntry(window,
                    font=("Arial",15),
                    textvariable=matrix_text4,
                    width=30,
                    placeholder_text="5")
matrix4.insert(0, "5")

matrix_text1.trace("w", lambda *args: character_limit1(matrix_text1))
matrix_text2.trace("w", lambda *args: character_limit1(matrix_text2))
matrix_text3.trace("w", lambda *args: character_limit1(matrix_text3))
matrix_text4.trace("w", lambda *args: character_limit1(matrix_text4))

keyText = StringVar()

keyEntry = CTkEntry(frame,
                    font=("Arial",15),
                    textvariable=keyText,
                    width=150)

manyFrame = CTkScrollableFrame(window,
                     width=475,
                     height=330,
                     fg_color="#1c1c1c")

button = CTkButton(window,
                   text="Дешифровать",
                   font=("Arial",20),
                   command=decipher,
                   state=DISABLED,
                   width=150,
                   height=50,
                   fg_color="#253322",
                   hover_color="#26a80c")
button.place(x=170,y=175)
window.bind("<Return>", decipher)

notes = CTkTextbox(window,
                   font=("Ariel", 30),
                   width=300,
                   height=400)
notes.place(x=500,y=0)

window.mainloop()