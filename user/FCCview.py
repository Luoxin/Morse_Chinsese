from tkinter import *

from date.SQL import executeSQL


class FFCview:
    def __init__(self):
        self.root=Tk()
        self.root.title="四角码转换器"

        self.l_character = Label(self.root, text="汉字")
        l.grid(row=1, column=0, sticky=W)

        self.root.mainloop()


if __name__ == '__main__':
    a=FFCview()