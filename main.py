from customtkinter import *
from tkinter import Entry as tkEntry
from time import sleep

from caesar_file import *
from vigenere_file import *
from atbash_file import *

VERSION = "1.1"

set_appearance_mode("dark")
set_default_color_theme("green")
def rotsAnimation():

    fakeDropdownRots.place(x=345,y=40)

    i = 37
    while i < 52:

        fakeDropdownRots.place_configure(x=345,y=i)

        window.update()
        sleep(0.003)
        i +=1

    del(i)

    fakeDropdownRots.place_forget()
    dropdownRots.grid(row=0,column=2,padx=15,pady=20)

    window.update()

def check(event):
    dropdownLanguage.configure(state=NORMAL)

    if event == "Цезарь":
        if dropdownRots.get() == "ROT?":
            button.configure(state=DISABLED)

        keyEntry.grid_forget()
        dropdownLanguage.configure(values=whatLang)

        if not dropdownRots.winfo_ismapped():
            rotsAnimation()

    elif event == "Атбаш":

        dropdownRots.grid_forget()
        keyEntry.grid_forget()

        dropdownLanguage.configure(values=whatLang)

    elif event == "Виженер":
        if dropdownRots.get() == "ROT?":
            button.configure(state=DISABLED)
            
        if dropdownLanguage.get() == "Все, что ниже":
            dropdownLanguage.set("Язык?")
            dropdownRots.configure(state=DISABLED)
        
        if dropdownRots.get() != "0" and dropdownRots.get() != "1" and dropdownRots.get() != "All":
            dropdownRots.set("ROT?")
            button.configure(state=DISABLED)

        dropdownLanguage.configure(values=whatLangVigenere)
        dropdownRots.configure(values=RotsVG)
        
        keyEntry.grid(row=1,column=1,pady=8)

        if not dropdownRots.winfo_ismapped():
            rotsAnimation()

    window.update()

    return


def checkLanguage(event):

    global RotsEN
    global RotsRU

    if dropdownCipher.get() == "Виженер":

        dropdownRots.configure(values=RotsVG)
        dropdownRots.configure(state=NORMAL)

        window.update()
        return
    
    elif dropdownCipher.get() == "Цезарь":

        if event == "Все, что ниже" or event == "Русский":
            dropdownRots.configure(values=RotsRU)

        elif event == "English":
            dropdownRots.configure(values=RotsEN)

        dropdownRots.configure(state=NORMAL)

        window.update()
        return

    elif dropdownCipher.get() == "Атбаш":

        button.configure(state=NORMAL)

        window.update()
        return


def checkRot(event):

    button.configure(state=NORMAL)


def decipher(*event):
    if button.cget('state') == DISABLED:
        return
    
    try:
        label.place_forget()
        copy_button.place_forget()
    except:
        pass
    try:
        rotsFrame.place_forget()
        for widget in rot_labels:
            widget.pack_forget()
        del(temp_rots)
    except:
        pass
    try:
        label_backup.pack_forget()
        copy_button_backup.place_forget()
    except:
        pass

    window.update()

    if cipherEntry.get() != "":

        if dropdownCipher.get() == "Цезарь":
            after_dec(caesar_dec(dropdownLanguage.get(), cipherEntry.get(), dropdownRots.get()))

        elif dropdownCipher.get() == "Виженер" and keyEntry.get() != "":
            after_dec(vigenere_dec(dropdownLanguage.get(), cipherEntry.get(), keyEntry.get(), dropdownRots.get()))

        elif dropdownCipher.get() == "Атбаш":
            after_dec(atbash_dec(dropdownLanguage.get(), cipherEntry.get()))

        else:
            return

    else:
        return


def after_dec(deciphed:str) -> str:

    global rot_label, vg_rot_label0, vg_rot_label1, rot_labels, copy_button_backup, label_backup

    if isinstance(deciphed, list):

        rotsFrame.place(x=0,y=240)

        if dropdownCipher.get() == "Цезарь":
            rot_labels = []

            for i in range(len(deciphed)):
        
                rot_label = tkEntry(rotsFrame,
                                     font=("Ariel", 20),
                                     width=450,
                                     foreground="white",
                                     border=0,
                                     readonlybackground="#1c1c1c")
                
                rot_label.insert(0, f"Rot {i + 1} = {deciphed[i]}")
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


options = [
    "Цезарь",
    "Виженер",
    "Атбаш"
]
whatLang = [
    "Все, что ниже",
    "Русский",
    "English"
]

whatLangVigenere = [
    "Русский",
    "English"
]

RotsEN = [
    "All","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"
]
RotsRU = [
    "All","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32"
]
RotsVG = [
    "All","0","1"
]

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

keyEntry = CTkEntry(frame,
                    font=("Arial",15),
                    width=150,
                    placeholder_text="Key")

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