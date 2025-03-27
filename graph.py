# graph.py

import tkinter as tk
from tkinter import filedialog, messagebox
import math

__ver__ = '1.0'
__date__ = '26.03.2025'

root = tk.Tk()
root.title(f'KXGraph {__ver__}')
root.geometry('1000x800')
photo = tk.PhotoImage(file = 'icon.ico')
root.iconphoto(True,photo)
root.config(background='#1b1b1b')

def update_widjets(event):
    print(root.winfo_width(),root.winfo_height())
    func.place(x=0,y=root.winfo_height()-20,width=root.winfo_width())
    submit.place(x=root.winfo_width()-69,y=root.winfo_height()-27)

def graph(function):
    global x
    x = 0
    for x in range(80):
        tk.Canvas(root, width=10, height=10, highlightthickness=0).place(x=x*10,y=eval(function, globals())*10)

func = tk.Entry(root, bg='#1b1b1b', fg='white', insertbackground='white')
func.place(x=0,y=780,width=root.winfo_width())
submit = tk.Button(root, text='New graph', bg='#1b1b1b', fg='white', command=lambda: graph(func.get()))
submit.place(x=0,y=0)

root.bind("<Configure>", update_widjets)

root.mainloop()