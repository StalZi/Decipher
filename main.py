from customtkinter import *
from caesar_file import *
from vigenere_file import *


set_appearance_mode("dark")
set_default_color_theme("green")


def check(event):

    if event == "Цезарь":
        dropdownLanguage.configure(values=whatCaesar)

        if dropdownLanguage.get() == "Язык?" and dropdownRots.get() == "ROT?":

            dropdownLanguage.configure(values=whatCaesar)
            dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)
            dropdownRots.grid(row=0,column=2,padx=15,pady=20)
            keyEntry.grid_forget()

            window.update()

            return

        elif dropdownLanguage.get() != "Язык?":
            if dropdownLanguage.get() == "Русский":
                dropdownRots.configure(values=RotsRU)
            else:
                dropdownRots.configure(values=RotsEN)

            keyEntry.grid_forget()
            window.update()

            return
            
        keyEntry.grid_forget()
        window.update()

        return

    elif event == "Виженер":
        if dropdownLanguage.get() == "Язык?" and dropdownRots.get() == "ROT?":

            dropdownLanguage.configure(values=whatVigenere)
            dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)
            dropdownRots.grid(row=0,column=2,padx=15,pady=20)
            keyEntry.grid(row=1,column=1,pady=8)

            window.update

            return

        elif (dropdownRots.get() != "0" and dropdownRots.get() != "1" and dropdownRots.get() != "All") or dropdownLanguage.get() == "Все, что ниже":

            if dropdownRots.get() != "0" and dropdownRots.get() != "1" and dropdownRots.get() != "All":
                dropdownRots.set("ROT?")

            if dropdownLanguage.get() == "Все, что ниже":
                dropdownLanguage.set("Язык?")

            dropdownRots.configure(values=RotsVG)
            dropdownLanguage.configure(values=whatVigenere)
            keyEntry.grid(row=1,column=1,pady=8)

            window.update

            return

        keyEntry.grid(row=1,column=1,pady=8)
        window.update

        return


def checkLanguage(event):

    global RotsEN
    global RotsRU

    if dropdownCipher.get() == "Виженер":
        dropdownRots.configure(values=RotsVG)
        dropdownRots.configure(state=NORMAL)

        window.update()
        return

    elif event == "Все, что ниже":
        dropdownRots.configure(values=RotsRU)

    elif event == "Русский":
        dropdownRots.configure(values=RotsRU)

    elif event == "English":
        dropdownRots.configure(values=RotsEN)

    dropdownRots.configure(state=NORMAL)

    window.update()


def checkRot(event):

    button.configure(state=NORMAL)


def decipher(*event):
    if button.cget('state') == DISABLED:
        return
    
    try:
        label.place_forget()
    except:
        pass
    try:
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

    window.update()

    if cipherEntry.get() != "":

        if dropdownCipher.get() == "Цезарь":
            after_dec(caesar_dec(dropdownLanguage.get(), cipherEntry.get(), dropdownRots.get()))

        elif dropdownCipher.get() == "Виженер" and keyEntry.get() != "":
            after_dec(vigenere_dec(dropdownLanguage.get(), cipherEntry.get(), keyEntry.get(), dropdownRots.get()))

        else:
            return

    else:
        return


def after_dec(deciphed:str) -> str:

    global rot_label, vg_rot_label0, vg_rot_label1, rot_labels, temp_rots

    if isinstance(deciphed, list):

        rotsFrame.place(x=0,y=240)

        if dropdownCipher.get() == "Цезарь":
            rot_labels = []

            for i in range(len(deciphed)):
        
                rot_label = CTkLabel(rotsFrame,
                         text=f"Rot {i + 1} = {deciphed[i]}",
                         font=("Ariel", 20),
                         wraplength=450)
                
                rot_label.pack(anchor=NW)

                copy_button.place(in_=rot_label,relx=1.1,rely=0.9,x=30,y=0)

                rot_labels.append(rot_label)

        elif dropdownCipher.get() == "Виженер":

            vg_rot_label0 = CTkLabel(rotsFrame,
                                 text=f"Rot 0 = {deciphed[0]}",
                                 font=("Ariel", 26),
                                 wraplength=450)
            vg_rot_label0.pack(anchor=NW, pady=30)

            vg_rot_label1 = CTkLabel(rotsFrame,
                                 text=f"Rot 1 = {deciphed[1]}",
                                 font=("Ariel", 26),
                                 wraplength=450)
            vg_rot_label1.pack(anchor=NW, pady=30)


    else:

        label.configure(text=deciphed)
        label.place(in_=button,relx=-1.0,rely=0,x=0,y=100)

        copy_button.place(in_=label,relx=0.9,rely=0.8,x=30,y=0)

    window.update()


def copy():

    window.clipboard_clear()
    window.clipboard_append(label.cget("text"))


# ---------------------------------------

window = CTk()
window.title("Decipher by StalZi 1.0")
window.geometry("800x600")
window.resizable(False, True)

# ---------------------------------------


options = [
    "Цезарь",
    "Виженер"
]
whatCaesar = [
    "Все, что ниже",
    "Русский",
    "English"
]

whatVigenere = [
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
                         command=checkLanguage)
dropdownLanguage.set("Язык?")

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
                 wraplength=450,
                 width=450,
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