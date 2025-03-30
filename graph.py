# graph.py

import tkinter as tk
from tkinter import filedialog, messagebox
from main import __ver__, __date__

import math, random

graphs = []

root = tk.Tk()
root.title(f'KxGraph {__ver__}')
root.geometry('1000x800')
photo = tk.PhotoImage(file = 'icon.ico')
root.iconphoto(True,photo)
root.config(background='#1b1b1b')

step = 1
offset = 50
index = -1

def graph(function):
    global x
    x = 0
    graphs.append([])
    while True:
        if x > int(root.winfo_width()/10):
            break
        try:
            if eval(function, globals())*10 >= root.winfo_height()-30: 
                print(eval(function, globals())*10)
                print(root.winfo_height()-30)
                x += step
                continue
            dot = tk.Canvas(root, width=10, height=10, highlightthickness=0)
            dot.place(x=x*10,y=(eval(function, globals())+offset)*10)
            graphs[-1].append(dot)
        except ZeroDivisionError:
            x += step
            continue
        except Exception as e:
            messagebox.showerror('KxGraph',f'Error occured while drawing a graph\n\n{e}')
            break
        x += step
    print(graphs)
    print(f'Total dots: {len(graphs[-1])}')
        

        
def reset():
    # tk.Canvas(root, width=root.winfo_width(), height=root.winfo_height()-20, bg='#1b1b1b', highlightthickness=0).place(x=0,y=0)
    global graphs, object
    for graph in graphs:
        for object in graph:
            object.destroy()
    graphs = []

def delete():
    global graphs, object
    if len(graphs) != 0:
        for object in graphs[index]:
            object.destroy()
    graphs.pop(index)

def update_settings():
    apply_btn.place(x=settings_root.winfo_width()-60,y=settings_root.winfo_height()-40)

def apply():
    global step, offset, index
    step = float(step_entry.get()) 
    offset = float(offset_entry.get())
    index = int(index_entry.get())

def settings():
    global settings_root, apply_btn, step_entry, offset_entry, index_entry
    settings_root = tk.Toplevel(root)
    settings_root.title(f'KxGraph {__ver__}')
    settings_root.geometry('500x500')
    settings_root.config(background='#1b1b1b')

    tk.Label(settings_root, text='Settings', fg='white', bg='#1b1b1b', font=('Arial',30)).place(x=10,y=10)

    tk.Label(settings_root, text='Step: ', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=10,y=60)
    step_entry = tk.Entry(settings_root, width=5, bg='#1b1b1b', fg='white', font=('Arial',10))
    step_entry.insert(0, str(step))
    step_entry.place(x=50,y=60)

    tk.Label(settings_root, text='Offset: ', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=10,y=90)
    offset_entry = tk.Entry(settings_root, width=5, bg='#1b1b1b', fg='white', font=('Arial',10))
    offset_entry.insert(0, str(offset))
    offset_entry.place(x=50,y=90)

    tk.Label(settings_root, text='Index: ', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=10,y=120)
    index_entry = tk.Entry(settings_root, width=5, bg='#1b1b1b', fg='white', font=('Arial',10))
    index_entry.insert(0, str(index))
    index_entry.place(x=50,y=120)

    apply_btn = tk.Button(settings_root, text='Apply', fg='white', bg='#1b1b1b', command=apply)
    apply_btn.place(x=440,y=460)
    
    settings_root.bind("<Configure>", lambda event: update_settings())
    settings_root.bind("<Return>", lambda event: apply())

    settings_root.mainloop()

def update_widjets(event):
    func.place(x=0,y=root.winfo_height()-20,width=root.winfo_width())
    submit.place(x=root.winfo_width()-69,y=root.winfo_height()-27)
    clear.place(x=root.winfo_width()-108,y=root.winfo_height()-27)
    delete_graph.place(x=root.winfo_width()-186,y=root.winfo_height()-27)

func = tk.Entry(root, bg='#1b1b1b', fg='white', insertbackground='white')
func.place(x=0,y=780,width=root.winfo_width())

submit = tk.Button(root, text='New graph', bg='#1b1b1b', fg='white', command=lambda: graph(func.get()))
clear = tk.Button(root, text='Reset', bg='#1b1b1b', fg='white', command=reset)
delete_graph = tk.Button(root, text='Delete graph', bg='#1b1b1b', fg='white', command=delete)

submit.place(x=0,y=0)

root.bind("<Configure>", update_widjets)

root.bind("<Return>", lambda event: graph(func.get()))
root.bind("<F5>", lambda event: graph(func.get()))
root.bind("<Escape>", lambda event: reset())

root.bind("<Control-p>", lambda event: settings())
root.bind("<Control-o>", lambda event: settings())

menu = tk.Menu(root)  
scenesMenu = tk.Menu(menu, tearoff=0)
fileMenu = tk.Menu(menu, tearoff=0)
fileMenu.add_command(label="Settings",command=settings)
fileMenu.add_command(label="Reset",command=reset)
fileMenu.add_command(label="Create graph",command=lambda: graph(func.get()))
fileMenu.add_command(label="Exit",command=quit)
menu.add_cascade(label="File", menu=fileMenu)

root.config(menu=menu)

settings()
root.mainloop()

