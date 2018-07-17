from Morse.changeMorse import Morse

from tkinter import *


morse=Morse()

def toCode():
    s_character=e_character.get()
    s_code=morse.LettetoMorse(s_character)
    e_code.delete(0,END)
    e_code.insert(END,s_code)
    pass

def toCharacter():
    s_code=e_code.get()
    s_character=morse.MorsetoLetter(s_code)
    e_character.delete(0,END)
    e_character.insert(END,s_character)
    pass


root=Tk()
root.title = "Morse"

l_character = Label(root, text="原文")
l_character.grid(row=0, column=0, sticky=W)

e_character = Entry(root,width="50")
e_character.grid(row=0, column=1, sticky=E)

l_code = Label(root, text="密文")
l_code.grid(row=1, column=0, sticky=W)

e_code = Entry(root,width="50")
e_code.grid(row=1, column=1, sticky=E)

bl = Button(root, text="转换为Morse",command=toCode)
bl.grid(row=0, column=3, stick=W)

bl = Button(root, text="转换为Letter",command=toCharacter)
bl.grid(row=1, column=3, stick=W)





root.mainloop()