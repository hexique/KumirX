import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('KumirX')
root.geometry('1000x800')
photo = tk.PhotoImage(file = 'icon.ico')
root.iconphoto(True,photo)
root.config(background='#1b1b1b')

pos = [0, 0]
result = '''использовать Робот
алг
нач
'''

def copy():
    root.clipboard_clear()
    root.clipboard_append(code.get('1.0',tk.END))
    print(code.get('1.0',tk.END))

pointer = tk.Canvas(root, bg='red', highlightthickness=0, borderwidth=0, width=20, height=20)
pointer.place(x = pos[0] * 20, y = pos[1] * 20)

code = tk.Text(root, width=32, height=50, bg='#1b1b1b', fg='white')
code.place(x=740,y=0)

tk.Button(root,text='Copy', bg='#1b1b1b', fg='white', command=copy).place(x=685,y=770)

def move(x, y, fill):
    global pos, result
    if fill:
        tk.Canvas(root, bg='white', highlightthickness=0, borderwidth=0, width=20, height=20).place(x = pos[0] * 20, y = pos[1] * 20)
    elif fill == False:
        tk.Canvas(root, bg='#1b1b1b', highlightthickness=0, borderwidth=0, width=20, height=20).place(x = pos[0] * 20, y = pos[1] * 20)
    pos[0] += x
    pos[1] += y
    pointer.place(x = pos[0] * 20, y = pos[1] * 20)
    if fill:
        result += 'закрасить\n'
    if y == -1:
        result += 'вверх\n'
    elif y == 1:
        result += 'вниз\n'
    elif x == -1:
        result += 'влево\n'
    elif x == 1:
        result += 'вправо\n'
    code.delete('1.0',tk.END)
    code.insert('1.0',f'{result}\nкон')

    print(result)


    print(pos[0], pos[1])

move(0, 0, None)

root.bind("<w>", lambda event: move(0, -1, True))
root.bind("<a>", lambda event: move(-1, 0, True))
root.bind("<s>", lambda event: move(0, 1, True))
root.bind("<d>", lambda event: move(1, 0, True))

root.bind("<Control-w>", lambda event: move(0, -1, None))
root.bind("<Control-a>", lambda event: move(-1, 0, None))
root.bind("<Control-s>", lambda event: move(0, 1, None))
root.bind("<Control-d>", lambda event: move(1, 0, None))
root.bind("<Shift-w>", lambda event: move(0, -1, None))
root.bind("<Shift-a>", lambda event: move(-1, 0, None))
root.bind("<Shift-s>", lambda event: move(0, 1, None))
root.bind("<Shift-d>", lambda event: move(1, 0, None))



root.mainloop()