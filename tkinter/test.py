import os
# from tkinter import *
import tkinter

root = tkinter.Tk()
root.title("Dont know wth is this!")
w = tkinter.Label(root, text='GeeksForGeeks.org!')
b = tkinter.Button(root, text='Stop', width=25, command=root.destroy)
w.pack()
b.pack()
root.mainloop()
