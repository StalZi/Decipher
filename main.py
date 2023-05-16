from customtkinter import *
from tkinter import Entry as tkEntry
from time import sleep

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

            dropdownLanguage.configure(values=whatLangVigenere)
            dropdownRots.configure(values=RotsVG)

            keyEntry.grid(row=1,column=1,pady=8)

            dropdownRots.grid(row=0,column=2,padx=15,pady=20)
            
        case "Хилл":
            button.configure(state=NORMAL)

            dropdownLanguage.grid_forget()
            dropdownRots.grid_forget()
            keyEntry.grid_forget()

            matrix_title.place(x=275,y=5)
            matrix_label.place(x=205,y=32)

            matrix1.place(x=222,y=32)
            matrix2.place(x=272,y=32)
            matrix3.place(x=330,y=32)
            matrix4.place(x=380,y=32)


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
    

    label.place_forget()
    copy_button.place_forget()
    rotsFrame.place_forget()

    try:
        for widget in rot_labels:
            widget.pack_forget()
    except:
        pass
    try:
        label_backup.pack_forget()
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
                    after_dec(hill_dec(cipherEntry.get(),[[matrix_text1.get, matrix_text2],[matrix_text3, matrix_text4]]))
                except:
                    after_dec("Bad symbols (тут вообще пиздец, так что пишу на русском, возможные проблемы: Плохая матрица, спец символы в шифре(пробелы), длина шифра не квадрат числа)")

            case _:
                return
    else:
        return


def after_dec(deciphed:str) -> str:

    global rot_label, vg_rot_label0, vg_rot_label1, rot_labels, label_backup

    if dropdownRots.get() == "All" or checkboxVar.get() == 1:
        print("here?")
        rotsFrame.place(x=0,y=240)

        if dropdownCipher.get() == "Цезарь" or dropdownCipher.get() == "Рейл":
            rot_labels = []

            if dropdownCipher.get() == "Цезарь":
                text = (0, f"Rot {i + 1} = {deciphed[i]}")

            elif dropdownCipher.get() == "Рейл":
                text = (0, f"Num {i + 1} = {deciphed[i]}")

            for i in range(len(deciphed)):
        
                rot_label = tkEntry(rotsFrame,
                                    font=("Ariel", 20),
                                    width=450,
                                    foreground="white",
                                    border=0,
                                    readonlybackground="#1c1c1c")
                
                rot_label.insert(0, text)

                rot_label.configure(state="readonly")
                rot_label.pack(anchor=NW, pady=5)

                rot_labels.append(rot_label)

        elif dropdownCipher.get() == "Виженер":

            vg_rot_label0 = tkEntry(rotsFrame,
                                    font=("Ariel", 26),
                                    width=450,
                                    foreground="white",
                                    border=0,
                                    readonlybackground="#1c1c1c")
            
            vg_rot_label0(0, f"Rot 0 = {deciphed[0]}")
            vg_rot_label0(state="readonly")
            vg_rot_label0.pack(anchor=NW, pady=30)


            vg_rot_label1 = tkEntry(rotsFrame,
                                    font=("Ariel", 26),
                                    width=450,
                                    foreground="white",
                                    border=0,
                                    readonlybackground="#1c1c1c")
            
            vg_rot_label1(0, f"Rot 1 = {deciphed[1]}")
            vg_rot_label1(state="readonly")
            vg_rot_label1.pack(anchor=NW, pady=30)


    elif isinstance(deciphed, list) and dropdownCipher.get() == "A1Z26":
        if len(deciphed) > 126:
            rotsFrame.place(x=0,y=240)

            label_backup = CTkLabel(rotsFrame,
                                  font=("Ariel", 40),
                                  wraplength=420,
                                  width=420,
                                  compound=CENTER)
            
            copy_button.place_forget()

            label_backup.configure(text=("english - " + deciphed[0] + " and russian - " + deciphed[1]))
            label_backup.pack(side=TOP)
            copy_button.place(x=500,y=500)

        else:
            label.configure(text=("english - " + deciphed[0] + " and russian is : " + deciphed[1]))
            label.place(in_=button,relx=-1.0,rely=0,x=0,y=100)

            copy_button.place(in_=label,relx=1.0,rely=0.8,x=10,y=0)

    else:
        if len(deciphed) > 126:
            rotsFrame.place(x=0,y=240)

            label_backup = CTkLabel(rotsFrame,
                                  font=("Ariel", 40),
                                  wraplength=420,
                                  width=420,
                                  compound=CENTER)
            
            copy_button_backup = CTkButton(window,
                                         text="Copy",
                                         width=20,
                                         command=copy)

            label_backup.configure(text=deciphed)
            label_backup.pack(side=TOP)
            copy_button_backup.place(x=500,y=500)

        else:
            label.configure(text=deciphed)
            label.place(in_=button,relx=-1.0,rely=0,x=0,y=100)

            copy_button.place(in_=label,relx=1.0,rely=0.8,x=10,y=0)

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

matrix_title = CTkLabel(frame,
                        text="Матрица",
                        font=("Ariel", 20),
                        compound=CENTER)

matrix_label = CTkLabel(frame,
                        text="[[       ,       ],[       ,       ]]",
                        font=("Ariel", 20),
                        compound=CENTER)

matrix_text1 = StringVar()
matrix_text2 = StringVar()
matrix_text3 = StringVar()
matrix_text4 = StringVar()

matrix1 = CTkEntry(frame,
                    font=("Arial",15),
                    textvariable=matrix_text1,
                    width=30,
                    placeholder_text="3")
matrix1.insert(0, "3")

matrix2 = CTkEntry(frame,
                    font=("Arial",15),
                    textvariable=matrix_text2,
                    width=30,
                    placeholder_text="3")
matrix2.insert(0, "3")

matrix3 = CTkEntry(frame,
                    font=("Arial",15),
                    textvariable=matrix_text3,
                    width=30,
                    placeholder_text="2")
matrix3.insert(0, "2")

matrix4 = CTkEntry(frame,
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

rotsFrame = CTkScrollableFrame(window,
                     width=475,
                     height=330,
                     fg_color="#1c1c1c")

button = CTkButton(window,
                   text="Дешифровать",
                   font=("Arial",20),
                   command=decipher,
                   state=DISABLED,
                   width=150,
                   height=50)
button.place(x=170,y=175)
window.bind("<Return>", decipher)

label = CTkLabel(window,
                 font=("Ariel", 40),
                 wraplength=420,
                 width=420,
                 compound=CENTER)

copy_button = CTkButton(window,
                        text="Copy",
                        width=20,
                        command=copy)

notes = CTkTextbox(window,
                   font=("Ariel", 30),
                   width=300,
                   height=400)
notes.place(x=500,y=0)

window.mainloop()