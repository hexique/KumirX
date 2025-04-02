# graph.py

import tkinter as tk
from tkinter import filedialog, messagebox
from main import __ver__, __date__

import math, random

graphs = []
graphdata = []

root = tk.Tk()
root.title(f'KxGraph {__ver__}')
root.geometry('1000x800')
photo = tk.PhotoImage(file = 'icon.ico')
root.iconphoto(True,photo)
root.config(background='#1b1b1b')

step = 1
scale = 'step*10'
offset = 40
index = -1

audit = ''

switch_color = tk.BooleanVar(value=True)
error_graph = tk.BooleanVar(value=True)
one_graph_max = tk.BooleanVar(value=False)

colors = ('#ff0000', '#00ff00', '#0000ff', '#ffff00', '#00ffff', '#ff00ff')

def save(text):
    file_path = filedialog.asksaveasfilename(
            initialfile=f"{func.get()}.txt",
            defaultextension=".txt",
            title="Save file",
            filetypes=[("Text file", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(text)

def colortable():
    color_root = tk.Toplevel(root)
    color_root.title(f'KxGraph {__ver__}')
    color_root.config(background='#1b1b1b')

    i = 0
    for data in graphdata:
        tk.Label(color_root, text=data['color'].lower(), bg=data['color'], justify='left').grid(row=i,column=0)
        tk.Label(color_root, text=data['function'], bg='#1b1b1b', fg='#ffffff', justify='left').grid(row=i,column=1)
        i += 1

    color_root.mainloop()

def graph(function):
    global x, audit
    x = 0
    if one_graph_max.get():
        delete(-1)
    graphs.append([])
    if switch_color.get():
        if len(graphs) > len(colors):
            color = '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        else:
            color = colors[len(graphs)-1]
    else:
        color = 'white'
    audit += f'Function: {function}\nGraph: {len(graphs)}\nScale: {eval(scale)} ({scale})\nStep: {step}\nOffset: {offset}\nColor: {color}\n\nDifferent color for every graph: {switch_color.get()}\nDelete graph after error: {error_graph.get()}\nGraph switch: {one_graph_max.get()}\n\nDots:\n'
    graphdata.append({'function': function, 'color': color})
    while True:
        if x > int(root.winfo_width()/10):
            break
        try:
            if eval(function, globals())+offset >= root.winfo_height()/10-2: 
                print(eval(function, globals())+offset, root.winfo_height()/10-2)
                x += step
                continue
            else:
                dot = tk.Canvas(root, width=eval(scale, globals()), height=eval(scale, globals()), highlightthickness=0, bg=color)
                dot.place(x=x*10,y=(eval(function, globals())+offset)*10)
                audit += f'{x} : {eval(function, globals())}\n'
                graphs[-1].append(dot)
        except ZeroDivisionError:
            x += step
            continue
        except Exception as e:
            messagebox.showerror('KxGraph',f'Error occured while drawing a graph\n\n{e}')
            if error_graph.get():
                delete(index)
            break
        x += step
    total_dots = 0
    for i in graphs:
        total_dots += len(i)
    audit += f'\nDots in graph: {len(graphs[-1])}\nDots of all time: {total_dots}\nGraphs: {len(graphs)}\n\n{"-"*10}\n\n'
    print(f'Total dots: {len(graphs[-1])}')
        
def reset():
    # tk.Canvas(root, width=root.winfo_width(), height=root.winfo_height()-20, bg='#1b1b1b', highlightthickness=0).place(x=0,y=0)
    global graphs, graphdata, object
    for graph in graphs:
        for object in graph:
            object.destroy()
    graphs = []
    graphdata = []

def delete(index):
    global graphs, graphdata, object
    if len(graphs) != 0:
        for object in graphs[index]:
            object.destroy()
    graphs.pop(index)
    graphdata.pop(index)

def update_settings():
    apply_btn.place(x=settings_root.winfo_width()-60,y=settings_root.winfo_height()-40)

def apply():
    global step, offset, index, scale
    step = float(step_entry.get()) 
    offset = float(offset_entry.get())
    index = int(index_entry.get())
    scale = scale_entry.get()

    line.place(x=0,y=offset*10)
    line['height'] = eval(scale, globals())
    line['bg'] = offsetcol_entry.get()

    
def settings():
    global settings_root, apply_btn, switch_color, error_graph, one_graph_max, step_entry, offset_entry, index_entry, scale_entry, offsetcol_entry
    settings_root = tk.Toplevel(root)
    settings_root.title(f'KxGraph {__ver__}')
    settings_root.geometry('500x500')
    settings_root.config(background='#1b1b1b')

    tk.Label(settings_root, text='Settings', fg='white', bg='#1b1b1b', font=('Arial',30)).place(x=10,y=10)

    tk.Label(settings_root, text='Step', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=60)
    step_entry = tk.Entry(settings_root, width=7, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    step_entry.insert(0, str(step))
    step_entry.place(x=10,y=60)

    tk.Label(settings_root, text='Scale', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=90)
    scale_entry = tk.Entry(settings_root, width=7, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    scale_entry.insert(0, scale)
    scale_entry.place(x=10,y=90)

    tk.Label(settings_root, text='Offset', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=120)
    offset_entry = tk.Entry(settings_root, width=7, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    offset_entry.insert(0, str(offset))
    offset_entry.place(x=10,y=120)

    tk.Label(settings_root, text='Offset color', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=150)
    offsetcol_entry = tk.Entry(settings_root, width=7, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    offsetcol_entry.insert(0, line['bg'])
    offsetcol_entry.place(x=10,y=150)

    tk.Label(settings_root, text='Index', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=180)
    index_entry = tk.Entry(settings_root, width=7, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    index_entry.insert(0, str(index))
    index_entry.place(x=10,y=180)

    tk.Checkbutton(settings_root, text='Different color for every graph', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=switch_color).place(x=10,y=210)
    tk.Checkbutton(settings_root, text='Delete graph after error', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=error_graph).place(x=10,y=240)
    tk.Checkbutton(settings_root, text='Graph switch', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=one_graph_max).place(x=10,y=270)

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
delete_graph = tk.Button(root, text='Delete graph', bg='#1b1b1b', fg='white', command=lambda: delete(index))

line = tk.Canvas(root, width=2000, height=eval(scale, globals()), bg='#2d2d2d', highlightthickness=0)
line.place(x=0, y=offset*10)

submit.place(x=0,y=0)

root.bind("<Configure>", update_widjets)

root.bind("<Return>", lambda event: graph(func.get()))
root.bind("<F5>", lambda event: graph(func.get()))
root.bind("<Escape>", lambda event: reset())
root.bind("<Delete>", lambda event: delete(index))
root.bind("<Control-Delete>", lambda event: delete(-1))
root.bind("<Shift-Delete>", lambda event: delete(0))
root.bind("<Control-s>", lambda event: save(audit))
root.bind("<Control-p>", lambda event: settings())
root.bind("<Control-g>", lambda event: colortable())
root.bind("<Tab>", lambda event: settings())

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

