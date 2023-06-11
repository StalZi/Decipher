from customtkinter import *
from PIL import Image
import os

from options import *
from char_lim import *
from animation import SlidePanel

from ciphers import *
from systems import *
from spectrs import *


VERSION = "1.6"

set_appearance_mode("dark")
set_default_color_theme("green")


# handling cipher selection
def check(event):
    if event != "Шифр?":
        global keyText_trace_id

        dropdownLanguage.configure(state=NORMAL)
        checkboxVar.set(0)
        checkbox.place_forget()
        try:
            keyText1.trace_vdelete("w", keyText_trace_id)
        except:
            pass

        keyEntry_morse2.grid_forget()
        keyEntry_morse3.place_forget()

    else:
        button.configure(state=DISABLED)

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

            keyEntry1.grid_forget()
            dropdownLanguage.configure(values=whatLang)

            dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)
            dropdownRots.grid(row=0,column=2,padx=15,pady=20)

        case "Атбаш":

            if dropdownLanguage.get() != "Язык?":
                button.configure(state=NORMAL)

            dropdownRots.grid_forget()
            keyEntry1.grid_forget()

            dropdownLanguage.grid(row=0,column=1)
            dropdownLanguage.configure(values=whatLang)
        
        case "A1Z26":

            if dropdownLanguage.get() != "Язык?":
                button.configure(state=NORMAL)

            checkbox.configure(text="A2Z52")
            dropdownRots.grid_forget()
            keyEntry1.grid_forget()

            dropdownLanguage.grid(row=0,column=1)
            checkbox.place(in_=dropdownLanguage,relx=1.0,rely=0,x=10,y=0)
            dropdownLanguage.configure(values=whatLang)

        case "Рейл":

            button.configure(state=NORMAL)
            checkbox.configure(text="All")

            dropdownLanguage.grid_forget()
            dropdownRots.grid_forget()
            keyEntry1.grid_forget()

            keyEntry1.configure(width=100)
            keyEntry1.grid(row=0,column=1,padx=10,pady=20)

            keyText_trace_id = keyText1.trace("w", lambda *args: character_limit3(keyText1))

            checkbox.place(in_=keyEntry1,relx=1.0,rely=0,x=10,y=0)
        
        case "Плейфер":

            dropdownRots.grid_forget()
            dropdownLanguage.set("English")
            dropdownLanguage.configure(state=DISABLED)
            button.configure(state=NORMAL)

            keyEntry1.grid(row=1,column=1,pady=8)

        case "Виженер":

            if dropdownRots.get() == "ROT?":
                button.configure(state=DISABLED)
            
            if dropdownLanguage.get() == "Все, что ниже":
                dropdownLanguage.set("Язык?")
                dropdownRots.configure(state=DISABLED)
                button.configure(state=DISABLED)

            else:
                dropdownRots.configure(state=NORMAL)

            if dropdownRots.get() != "0" and dropdownRots.get() != "1" and dropdownRots.get() != "All":
                dropdownRots.set("ROT?")
                button.configure(state=DISABLED)

            dropdownLanguage.configure(values=whatLangCut)
            dropdownRots.configure(values=RotsVG)

            keyEntry1.configure(state=NORMAL)
            keyEntry1.grid(row=1,column=1,pady=8)

            dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)
            dropdownRots.grid(row=0,column=2,padx=15,pady=20)
            
        case "Хилл":

            button.configure(state=NORMAL)

            dropdownLanguage.configure(values=whatLangCut)
            if dropdownLanguage.get() == "Все, что ниже":
                dropdownLanguage.set("Язык?")
                dropdownRots.configure(state=DISABLED)
                button.configure(state=DISABLED)

            dropdownRots.grid_forget()
            keyEntry1.grid_forget()

            dropdownLanguage.grid(row=0,column=1)

            matrix_title.place(x=200,y=100)
            matrix_label.place(x=130,y=135)

            matrix1.place(x=147,y=135)
            matrix2.place(x=197,y=135)
            matrix3.place(x=255,y=135)
            matrix4.place(x=305,y=135)

        case "Морзе":

            button.configure(state=NORMAL)
            dropdownLanguage.set("English")
            dropdownLanguage.configure(state=DISABLED)
            dropdownRots.grid(row=0,column=2,padx=15,pady=20)

            dropdownRots.grid_forget()
            keyEntry1.grid_forget()
            keyEntry_morse2.grid(row=1,columnspan=2,pady=8)
            keyEntry_morse3.place(in_=keyEntry_morse2,relx=1.0,rely=0,x=110,y=0)


    window.update()

# handling language selection
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

# handling rot selection
def checkRot(event):

    button.configure(state=NORMAL)

# handling checkbox ticking in rail fence
def checkCheckbox():

    match dropdownCipher.get():
    
        case "Рейл":
            if checkboxVar.get() == 1:
                keyEntry1.delete(0, END)
                keyEntry1.configure(state=DISABLED)

            else:
                keyEntry1.configure(state=NORMAL)

        case "A1Z26":
            pass


# handling pressing the decrypt button
def decipher(*event):
    if button.cget('state') == DISABLED:
        return
    
    forget()

    if cipherEntry.get() == "":
        return

    match current_tab:
        case "ciphers":
            match dropdownCipher.get():
                case "Цезарь":
                
                    after_dec(caesar_dec(dropdownLanguage.get(), cipherEntry.get(), dropdownRots.get()))

                case "Виженер" if keyText1.get() != "":

                    try:
                        after_dec(vigenere_dec(dropdownLanguage.get(), cipherEntry.get(), keyText1.get(), dropdownRots.get()))
                    except:
                        after_dec("Bad symbols in the entry")

                case "Атбаш":
                
                    after_dec(atbash_dec(dropdownLanguage.get(), cipherEntry.get()))

                case "Плейфер" if keyText1.get() != "":
                
                    try:
                        after_dec(playfair_dec(cipherEntry.get(), keyText1.get()))
                    except:
                        after_dec("Bad symbols (!, ?, ., etc.) or the key is incorrect")

                case "A1Z26":
                
                    try:

                        if checkboxVar.get() == 1:
                            after_dec(a1z26_dec(dropdownLanguage.get(), cipherEntry.get(), True))
                        else:
                            after_dec(a1z26_dec(dropdownLanguage.get(), cipherEntry.get()))

                    except:
                        after_dec("Bad symbols (should be 1-2-15-2-1, etc.)")

                case "Рейл" if keyText1.get() != "":
                
                    try:

                        if checkboxVar.get() == 1:
                            after_dec(rail_fence_dec(cipherEntry.get(), "All"))
                        else:
                            after_dec(rail_fence_dec(cipherEntry.get(), keyText1.get()))

                    except:
                        after_dec("Bad symbols, the key should be an integer")

                case "Хилл" if matrix_text1.get() != "" and matrix_text2.get() != "" and matrix_text3.get() != "" and matrix_text4.get() != "":
                
                    try:
                        after_dec(hill_dec(dropdownLanguage.get(),cipherEntry.get(),[[matrix_text1.get(), matrix_text2.get()],[matrix_text3.get(), matrix_text4.get()]]))
                    except:
                        after_dec("Bad symbols (возможные проблемы: Плохая матрица, спец символы в шифре(пробелы), длина шифра не квадрат числа)")
                
                case "Морзе" if keyText_morse2.get() != "" and keyText_morse3.get() != "":
                    try:
                        after_dec(morse_dec(cipherEntry.get(), keyText_morse2.get(), keyText_morse3.get()))
                    except:
                        after_dec("Bad symbols, the key entries should announce what dash and dot are (default = '-' and '.')")


        case "systems":
            match SYSradio_var.get():

                case "bin (2)":

                    try:
                        after_dec(bin_dec(cipherEntry.get()))
                    except:
                        after_dec("Bad symbols, the text should be binary (00000001 00000011)")

                case "oct (8)":

                    try:
                        after_dec(oct_dec(cipherEntry.get()))
                    except:
                        after_dec("Bad symbols, the text should be octal escape (\\141\\142\\143)")

                case "hex (16)":

                    try:
                        after_dec(hex_dec(cipherEntry.get()))
                    except:
                        after_dec("Bad symbols, the text should be hexadecimal (68656c6c6f)")

                case "base32":

                    try:
                        after_dec(base32_dec(cipherEntry.get()))
                    except:
                        after_dec("Bad symbols, the text should be base32 (KB4XI2DPNYQGS4ZAMF3WK43PNVSSC===)")

                case "base64":

                    try:
                        after_dec(base64_dec(cipherEntry.get()))
                    except:
                        after_dec("Bad symbols, the text should be base64 (YWJvYmE=)")

                case "base85":

                    try:
                        after_dec(base85_dec(cipherEntry.get()))
                    except:
                        after_dec("Bad symbols, the text should be base85 (@:F.a@/)")

                case _:
                    return

# showing decrypted message properly
def after_dec(*deciphed:str|list, image:bool = False):
    global decrypted_label, copy_button, manyDecrypted_labels

    if image:
        decrypted_label = CTkLabel(window,
                                   image=CTkImage(dark_image=Image.open('spectrogram_files/spectrogram.png'),
                                                  size=(500,500)),
                                   text='')
        decrypted_label.place(x=0,y=100)

        reveal_output_button.place(x=500,y=450)


    elif isinstance(deciphed, list):
            
            manyFrame.place(x=0,y=250)
            manyDecrypted_labels = []

            for i in range(len(deciphed)):

                decrypted_label = CTkEntry(manyFrame,
                                        font=("Ariel", 24),
                                        fg_color="transparent",
                                        border_width=0,
                                        width=475)
                
                if dropdownCipher.get() == "Виженер":
                    decrypted_label.insert(0, f"    {i} - {deciphed[i]}")
                elif dropdownCipher.get() == "Рейл":
                    decrypted_label.insert(0, f"    {i + 2} - {deciphed[i]}")
                else:
                    decrypted_label.insert(0, f"    {i + 1} - {deciphed[i]}")

                decrypted_label.configure(state="readonly")

                decrypted_label.pack(anchor=NW,pady=5)

                manyDecrypted_labels.append(decrypted_label)

    elif len(deciphed) > 98:

        decrypted_label = CTkTextbox(window,
                         font=("Ariel", 40),
                         width=475,
                         height=300,
                         fg_color="#1c1c1c")
        decrypted_label.insert(INSERT, deciphed)
        decrypted_label.configure(state=DISABLED)
        
        decrypted_label.place(in_=button,relx=-1.0,rely=1.0,x=0,y=50)


    else:

        decrypted_label = CTkLabel(window,
                         font=("Ariel", 40),
                         wraplength=420,
                         width=420,
                         compound=CENTER,
                         text=deciphed)

        copy_button = CTkButton(window,
                                text="Copy",
                                width=20,
                                command=copy)


        decrypted_label.place(in_=button,relx=-1.0,rely=1.0,x=0,y=50)
        copy_button.place(in_=decrypted_label,relx=1.0,rely=0.95,x=0,y=0)


    navBar.lift()
    window.update()


# misc functions
def copy():

    window.clipboard_clear()
    window.clipboard_append(decrypted_label.cget("text"))


# forgetting widgets
def forget():
    try:
        decrypted_label.destroy()
        copy_button.destroy()
    except:
        pass
    manyFrame.place_forget()

    try:
        for widget in manyDecrypted_labels:
            widget.pack_forget()
    except:
        pass

def forget_everything_ciphers():

    frame.pack_forget()
    cipherEntry.pack_forget()

    matrix_title.place_forget()
    matrix_label.place_forget()

    matrix1.place_forget()
    matrix2.place_forget()
    matrix3.place_forget()
    matrix4.place_forget()

    checkbox.place_forget()
    button.place_forget()


    button.unbind("<Return>")

def forget_everything_systems():
    bin_radio.place_forget()
    oct_radio.place_forget()
    hex_radio.place_forget()
    base32_radio.place_forget()
    base64_radio.place_forget()
    base85_radio.place_forget()
    button.place_forget()

def forget_everything_alphabets():
    wingdings_radio.place_forget()
    ALPoutput.place_forget()
    try:
        for widget in qw_keyboard_buttons:
            widget.place_forget()
        for widget in ot_keyboard_buttons:
            widget.place_forget()
    except:
        pass
    qwerty_frame.place_forget()
    otherKeys_frame.place_forget()
    qwerty_label.place_forget()
    others_label

def forget_everything_spectrs():
    wav2img_button.place_forget()
    reveal_output_button.place_forget()


# handling navbar animation
navBar_open = False
def motion(event):
    global navBar_open
    
    if window.winfo_pointerx() - window.winfo_rootx() > 200:
        navBar_open = False
        navBar.animate_backwards()

    elif window.winfo_pointerx() - window.winfo_rootx() < 36 and not navBar_open:
        navBar_open = True
        navBar.animate_forward()


# ciphers tab
def navCiphers():
    global current_tab
    current_tab = "ciphers"
    forget()
    forget_everything_alphabets()
    forget_everything_systems()
    forget_everything_spectrs()

    cipherEntry.pack(anchor=NW)
    frame.pack(anchor=N,fill=BOTH)
    button.place(x=170,y=175)
    window.bind("<Return>", decipher)

    check(dropdownCipher.get())


# systems tab
def navSystems():
    global current_tab
    current_tab = "systems"
    forget()
    forget_everything_alphabets()
    forget_everything_ciphers()
    forget_everything_spectrs()

    cipherEntry.pack(anchor=NW)

    bin_radio.place(x=20,y=40)
    oct_radio.place(x=200,y=40)
    hex_radio.place(x=380,y=40)
    base32_radio.place(x=20,y=100)
    base64_radio.place(x=200,y=100)
    base85_radio.place(x=380,y=100)

    button.place(x=170,y=175)
    window.bind("<Return>", decipher)

    if SYSradio_var.get() != "":
        button.configure(state=NORMAL)
    else:
        button.configure(state=DISABLED)

    navBar.lift()

def SYSradiobutton_event():
    button.configure(state=NORMAL)


# alphabets tab
def navAlphabets():
    global current_tab
    current_tab = "alphabets"
    forget()
    forget_everything_ciphers()
    forget_everything_systems()
    forget_everything_spectrs()

    wingdings_radio.place(x=25,y=20)
    

    ALPoutput.place(x=25,y=60)

    qwerty_label.place(x=175,y=215)
    qwerty_frame.place(x=25,y=250)
    others_label.place(x=210,y=560)
    otherKeys_frame.place(x=26,y=450)

def ALPradiobutton_event():
    global qw_keyboard_buttons, ot_keyboard_buttons
    match ALPradio_var.get():
        case "GWD":
            qw_keyboard_buttons = []
            for i, qw_key_row in enumerate(qwerty_keyboard):
                for j, qw_key in enumerate(qw_key_row):

                    qw_keyboard_button = CTkButton(qwerty_frame,
                                                width=45,
                                                height=45,
                                                command=lambda qw_key=qw_key: ALPbutton_event(qw_key),
                                                corner_radius=0,
                                                fg_color="black",
                                                font=("Wingdings", 26),
                                                text=qw_key)
                    qw_keyboard_button.grid_propagate(False)
                    qw_keyboard_button.grid(row=i,column=j)

                    qw_keyboard_buttons.append(qw_keyboard_button)

            ot_keyboard_buttons = []
            for i, ot_key_row in enumerate(others_keyboard):

                for j, ot_key in enumerate(ot_key_row):

                    ot_keyboard_button = CTkButton(otherKeys_frame,
                                                width=32,
                                                height=50,
                                                command=lambda ot_key=ot_key: ALPbutton_event(ot_key),
                                                corner_radius=0,
                                                fg_color="black",
                                                font=("Wingdings", 24),
                                                text=ot_key)
                    ot_keyboard_button.grid_propagate(False)
                    ot_keyboard_button.grid(row=i,column=j)

                    ot_keyboard_buttons.append(ot_keyboard_button)
def ALPbutton_event(key):
    ALPoutput.insert(INSERT, key)


# spectrs tab
def navSpectrs():
    global current_tab
    current_tab = "spectrs"
    forget()
    forget_everything_ciphers()
    forget_everything_systems()
    forget_everything_spectrs()
    wav2img_button.place(x=160,y=50)

def wav2img():
    try:
        wav2img_dec()
        after_dec(image=True)
    except:
        after_dec("Bad file")
def reveal_output():
    os.system(f'start {os.path.realpath("spectrogram_files")}')
# ---------------------------------------

window = CTk()
window.title(f"Decipher by StalZi {VERSION}")
window.geometry("800x600")
window.resizable(False, False)

current_tab = "ciphers"
# ---------------------------------------
#region of widgets
# the main entry at the top
cipherEntry = CTkEntry(window,
                    font=("Arial", 20),
                    width=500,
                    placeholder_text="Cipher",
                    corner_radius=0)
cipherEntry.pack(anchor=NW)

# the main decrypt button
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

# the notes box
notes = CTkTextbox(window,
                   font=("Ariel", 30),
                   width=300,
                   height=400)
notes.place(x=500,y=-4)

# the navigation bar and showing it when needed
navBar = SlidePanel(window,
                    -0.3,
                    0.01)

window.bind("<Motion>", motion)


# --------------- tab widgets ---------------
# default tab
navButtonCiphers = CTkButton(navBar,
                      corner_radius=0,
                      text="Шифры",
                      command=navCiphers)
navButtonCiphers.pack(side=TOP)

# ciphers widgets

# the frame with all the tools for decrypting some cipher
frame = CTkFrame(window,
                 corner_radius=0)
frame.pack(anchor=N,fill=BOTH)

# the cipher selection menu
dropdownCipher = CTkOptionMenu(frame,
                         values=options,
                         command=check)
dropdownCipher.set("Шифр?")
dropdownCipher.grid(row=0,column=0,padx=10,pady=20)

# the language selection menu
dropdownLanguage = CTkOptionMenu(frame,
                         values=None,
                         command=checkLanguage,
                         state=DISABLED)
dropdownLanguage.set("Язык?")
dropdownLanguage.grid(row=0,column=1,padx=15,pady=20)

# the rots selection menu
dropdownRots = CTkOptionMenu(frame,
                         values=None,
                         command=checkRot,
                         state=DISABLED)
dropdownRots.set("ROT?")

# the checkbox for the rail fence cipher
checkboxVar = IntVar()

checkbox = CTkCheckBox(frame,
                       variable=checkboxVar,
                       command=checkCheckbox)

# matrix stuff for the hill cipher
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

# key entrys for different ciphers
keyText1 = StringVar()
keyText_morse2 = StringVar()
keyText_morse3 = StringVar()
keyText_morse2.set("-")
keyText_morse3.set(".")

keyEntry1 = CTkEntry(frame,
                     font=("Arial",15),
                     textvariable=keyText1,
                     width=150)

keyEntry_morse2 = CTkEntry(frame,
                           font=("Arial",15),
                           textvariable=keyText_morse2,
                           width=50)

keyEntry_morse3 = CTkEntry(frame,
                           font=("Arial",15),
                           textvariable=keyText_morse3,
                           width=50)

# the frame for displaying decrypted text if there is too many of it
manyFrame = CTkScrollableFrame(window,
                               width=475,
                               height=330,
                               fg_color="#1c1c1c")

# ----------
navButtonSystems = CTkButton(navBar,
                      corner_radius=0,
                      text="Системы",
                      command=navSystems)
navButtonSystems.pack(side=TOP)

# systems widgets

SYSradio_var = StringVar()
bin_radio = CTkRadioButton(window,
                           text="bin (2)",
                           value="bin (2)",
                           font=("Ariel", 20),
                           variable=SYSradio_var,
                           command=SYSradiobutton_event)
oct_radio = CTkRadioButton(window,
                           text="oct (8)",
                           value="oct (8)",
                           font=("Ariel", 20),
                           variable=SYSradio_var,
                           command=SYSradiobutton_event)
hex_radio = CTkRadioButton(window,
                           text="hex (16)",
                           value="hex (16)",
                           font=("Ariel", 20),
                           variable=SYSradio_var,
                           command=SYSradiobutton_event)
base32_radio = CTkRadioButton(window,
                              text="base32",
                              value="base32",
                              font=("Ariel", 20),
                              variable=SYSradio_var,
                              command=SYSradiobutton_event)
base64_radio = CTkRadioButton(window,
                              text="base64",
                              value="base64",
                              font=("Ariel", 20),
                              variable=SYSradio_var,
                              command=SYSradiobutton_event)

base85_radio = CTkRadioButton(window,
                              text="base85",
                              value="base85",
                              font=("Ariel", 20),
                              variable=SYSradio_var,
                              command=SYSradiobutton_event)

# ------------
navButtonAlphabets = CTkButton(navBar,
                               corner_radius=0,
                               text="Алфавиты",
                               command=navAlphabets)
navButtonAlphabets.pack(side=TOP)

# ------------
navButtonAlphabets = CTkButton(navBar,
                               corner_radius=0,
                               text="Спектрограммы",
                               command=navSpectrs)
navButtonAlphabets.pack(side=TOP)

# alphabets widgets

ALPradio_var = StringVar()
wingdings_radio = CTkRadioButton(window,
                              text="Gaster wingdings",
                              value="GWD",
                              font=("Ariel", 20),
                              variable=ALPradio_var,
                              command=ALPradiobutton_event)

ALPoutput = CTkTextbox(window,
                   font=("Ariel", 30),
                   width=450,
                   height=150)

qwerty_label = CTkLabel(window,
                        font=("Ariel", 30),
                        text="QWERTY")

qwerty_frame = CTkFrame(window,
                        width=450,
                        height=180)
qwerty_frame.grid_propagate(False)

others_label = CTkLabel(window,
                        font=("Ariel", 30),
                        text="Other")

otherKeys_frame = CTkFrame(window,
                           width=450,
                           height=100)
qwerty_frame.grid_propagate(False)

# spectrs widgets

wav2img_button = CTkButton(window,
                           text="WAV -> IMG",
                           command=wav2img)

reveal_output_button = CTkButton(window,
                               text="Открыть в папке",
                               command=reveal_output)

# --------------- tab widgets ---------------
notes.lift()
navBar.lift()
#endregion

window.mainloop()