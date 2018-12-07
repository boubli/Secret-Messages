from tkinter import *
from tkinter import ttk
import sys, random
from tkinter import  messagebox


def mess():
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def main():
        myMessage = vv.get()
        myKey = ve.get()
        myMode = v.get()

        if myMode == 'You':
            translated = encryptMessage(myKey, myMessage)
            vvv.set(translated)
        elif myMode == 'Hem':
            translated = decryptMessage(myKey, myMessage)
            vvv.set(translated)
        else:
            messagebox.showerror(title='Warning', message='Please select the encryption type')

        checkValidKey(myKey)

    def checkValidKey(key):
        keyList = list(key)
        lettersList = list(LETTERS)
        keyList.sort()
        lettersList.sort()
        if keyList != lettersList:
            sys.exit('There is an error in the key or symbol set.')

    def encryptMessage(key, message):
        return translateMessage(key, message, 'encrypt')

    def decryptMessage(key, message):
        return translateMessage(key, message, 'decrypt')

    def translateMessage(key, message, mode):
        translated = ''
        charsA = LETTERS
        charsB = key
        if mode == 'decrypt':
            # For decrypting, we can use the same code as encrypting. We
            # just need to swap where the key and LETTERS strings are used.
            charsA, charsB = charsB, charsA

        # loop through each symbol in the message
        for symbol in message:
            if symbol.upper() in charsA:
                # encrypt/decrypt the symbol
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated += charsB[symIndex].lower()
            else:
                # symbol is not in LETTERS, just add it
                translated += symbol

        return translated

    def getRandomKey():
        key = list(LETTERS)
        random.shuffle(key)
        return ''.join(key)

    def close():
      window.destroy()

    window = Tk()
    window.title("Encrypt Messages")
    window.configure(background="#0097e6")
    window.geometry("600x560+380+150")
    window.iconbitmap('secret.icns')
    style = ttk.Style()
    style.theme_use('clam')
    style.configure('TButton', background="#bdc3c7", foreground="#2c3e50", )

    Label(window, text="Select encryption type", bg="#0097e6", fg="white", pady=12).pack()
    v = StringVar()
    mode = Entry(window, width=20, textvariable=v, ).pack()

    Label(window, text="Your Key Alpha", bg="#0097e6", fg="white", pady=12).pack()
    ve = StringVar(value='ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    mode = Entry(window, width=60, textvariable=ve).pack()


    Label(window, text="Selet Your Message", bg="#0097e6", fg="white", pady=12).pack()
    vv = StringVar()
    messageBox = Entry(window, width=60, textvariable=vv).pack(ipady=30)

    ttk.Button(window, text="Enceypet", command=main, ).pack(pady=12)

    Label(window, text="This is Your Message", bg="#0097e6", fg="white", pady=12).pack()
    vvv = StringVar()
    outbput = Entry(window, width=40, textvariable=vvv).pack(ipady=30)

    ttk.Button(window, text="Exit", command=close).pack(pady=12)

    window.mainloop()





def checkVild():
    if pss.get() == "admin" and usr.get() == "admin":
        admin.destroy()
    mess()


#  ======== MAIN FRAM ==========================================

admin = Tk()  # This is Name of root you can Edit 'Admin'
admin.title("Login Admin")  # This is Title (" ")
admin.geometry("600x470+380+150")   # You Can Edit Size
admin.configure(background="#00a8ff")  # Edit Background Don't Delete '#'
style = ttk.Style()

# ======= This is Label, Entry, Button ===============================================
# ---- ----- ---- START info is Title --- ---- --- #
info = Label(admin, font=('Asap', 30), text="LOGIN", bg="#00a8ff", fg="white")
info.pack(pady=20)
# ---- ----- ---- END info is Title --- ---- --- #
# ---- ----- ---- START User Entry --- ---- --- #
usr = StringVar()
user = Entry(admin, width=30, bg="#f5f6fa", textvariable=usr)
user.pack(pady=20)
# ---- ----- ---- END User Entry --- ---- --- #
# ---- ----- ---- START Password Entry --- ---- --- #
pss = StringVar()
password = Entry(admin, width=30, bg="#f5f6fa", show="*", textvariable=pss)
password.pack(pady=20)
# ---- ----- ---- END Password Entry --- ---- --- #
# ---- ----- ---- START Button --- ---- --- #
btn = Button(admin, font=('arial', 14, 'bold'), text="LOGIN", width=10, heigh=2, command=checkVild)
btn.pack()
# ---- ----- ---- END Button --- ---- --- #
# ========= END =======================================================================
admin.mainloop()
