from tkinter import *
from tkinter import messagebox
import time


class Notify:
    def __init__(self):
        self.tk = Tk()
        self.tk.iconify()

    @staticmethod
    def showNotify(title, content):
        messagebox.showinfo(title, content)


if __name__ == '__main__':
    obj = Notify()
