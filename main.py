import tkinter as tk
from tkinter import filedialog, messagebox

__ver__ = '1.1.1'

root = tk.Tk()
root.title(f'KumirX {__ver__}')
root.geometry('1000x800')
photo = tk.PhotoImage(file = 'icon.ico')
root.iconphoto(True,photo)
root.config(background='#1b1b1b')

scale = 20
cooldown = 0
path = None
color = 'white'

pos = [0, 0]

keywords = {
    'updelete ': 'вверх\n',
    'leftdelete ': 'влево\n',
    'downdelete ': 'вниз\n',
    'rightdelete ': 'вправо\n',

    'upwithout ': 'вверх\n',
    'leftwithout ': 'влево\n',
    'downwithout ': 'вниз\n',
    'rightwithout ': 'вправо\n',

    'wdelete ': 'вверх\n',
    'adelete ': 'влево\n',
    'sdelete ': 'вниз\n',
    'ddelete ': 'вправо\n',

    'wwithout ': 'вверх\n',
    'awithout ': 'влево\n',
    'swithout ': 'вниз\n',
    'dwithout ': 'вправо\n',

    'upd ': 'вверх\n',
    'leftd ': 'влево\n',
    'downd ': 'вниз\n',
    'rightd ': 'вправо\n',

    'upw ': 'вверх\n',
    'leftw ': 'влево\n',
    'downw ': 'вниз\n',
    'rightw ': 'вправо\n',

    'up ': 'вверх\nзакрасить\n',
    'left ': 'влево\nзакрасить\n',
    'down ': 'вниз\nзакрасить\n',
    'right ': 'вправо\nзакрасить\n',

    '↑d ': 'вверх\n',
    '←d ': 'влево\n',
    '↓d ': 'вниз\n',
    '→d ': 'вправо\n',

    '↑w ': 'вверх\n',
    '←w ': 'влево\n',
    '↓w ': 'вниз\n',
    '→w ': 'вправо\n',

    '↑ ': 'вверх\nзакрасить\n',
    '← ': 'влево\nзакрасить\n',
    '↓ ': 'вниз\nзакрасить\n',
    '→ ': 'вправо\nзакрасить\n',

    'wd ': 'вверх\n',
    'ad ': 'влево\n',
    'sd ': 'вниз\n',
    'dd ': 'вправо\n',

    'ww ': 'вверх\n',
    'aw ': 'влево\n',
    'sw ': 'вниз\n',
    'dw ': 'вправо\n',

    'w ': 'вверх\nзакрасить\n',
    'a ': 'влево\nзакрасить\n',
    's ': 'вниз\nзакрасить\n',
    'd ': 'вправо\nзакрасить\n',

    'cooldown:': '|',
    'cd:': '|',

    'scale:': '|',
    'sc:': '|',

    'color:': '|',
    'col:': '|',
    'c:': '|',
}

def copy():
    root.clipboard_clear()
    root.clipboard_append(code.get('1.0',tk.END))
    print(code.get('1.0',tk.END))

def save(text):
    global path
    if path != None:
        with open(path, "w", encoding="utf-8") as f:
            f.write(code.get("1.0", tk.END))
        return


    file_path = filedialog.asksaveasfilename(
            initialfile="main.kmx",
            defaultextension=".kmx",
            title="Save file",
            filetypes=[("KumirX file", "*.kmx"), ("Kumir file", "*.kum"), ("Text file", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        path = file_path
        with open(file_path, "w", encoding="utf-8") as f:
            if file_path.endswith('kum'):
                text = text.replace('\n',' ')
                for i in keywords.keys():
                    text = text.replace(i, keywords[i])
                    print(i, keywords[i])
                text = f'использовать Робот\nалг\nнач\n{text}\nкон'

            f.write(text)
            root.title(f'KumirX {__ver__} - {file_path.split("/")[-1]}')

def openfile():
    global path
    confirm = True
    if path != None:
        confirm = messagebox.askyesnocancel(root.title(), "Unsaved changes detected. Do you want to save?", icon='warning')
    file_path = filedialog.askopenfilename(

    )

    if file_path:
        if confirm:
            save(code.get('1.0', tk.END))
        elif confirm is None:
            return
        path = file_path
        with open(file_path, "r", encoding="utf-8") as f:
            code.delete('1.0', tk.END)
            code.insert('1.0', f.read())
            root.title(f'KumirX {__ver__} - {file_path.split("/")[-1]}')

def placeBtns():
    tk.Button(root,text='Run', bg='#1b1b1b', fg='white', command=lambda: run(code.get('1.0',tk.END))).place(x=10,y=770)
    tk.Button(root,text='Copy', bg='#1b1b1b', fg='white', command=copy).place(x=50,y=770)
    tk.Button(root,text='Save', bg='#1b1b1b', fg='white', command=lambda: save(code.get('1.0',tk.END))).place(x=100,y=770)
    tk.Button(root,text='Open', bg='#1b1b1b', fg='white', command=openfile).place(x=150,y=770)

placeBtns()
code = tk.Text(root, width=32, height=50, bg='#1b1b1b', fg='white', insertbackground='white')
code.place(x=740,y=0)

# ← ↑ → ↓

def run(code):
    global scale, pointer, pos, cooldown, color
    tk.Canvas(root, width=740, height=760, bg='#1b1b1b', highlightthickness=0).place(x=0,y=0)
    pointer = tk.Canvas(root, bg='red', highlightthickness=0, borderwidth=0, width=scale, height=scale)
    pointer.place(x = pos[0] * 20, y = pos[1] * 20)
    pos = [0] * 2
    x = 0
    y = 0
    fill = False
    for command in ' '.join(code.split('\n')).split():
        if command.split(':')[0].lower() in ('scale', 'sc'):
            scale = float(command.split(':')[-1])
            pointer.place(x = pos[0] * scale, y = pos[1] * scale)
            pointer['width'] = scale
            pointer['height'] = scale

        if command.split(':')[0].lower() in ('color', 'col', 'c'):
            color = command.split(':')[-1]
            continue

        if command.split(':')[0].lower() in ('cooldown', 'cd'):
            cooldown = int(command.split(':')[-1])

        if command.split(':')[0].lower() in ('w', 'up', '↑'):
            x, y, fill = 0, -1, True
        elif command.split(':')[0].lower() in ('a', 'left', '←'):
            x, y, fill = -1, 0, True
        elif command.split(':')[0].lower() in ('s', 'down', '↓'):
            x, y, fill = 0, 1, True
        elif command.split(':')[0].lower() in ('d', 'right', '→'):
            x, y, fill = 1, 0, True

        if command.split(':')[0].lower() in ('ww', 'wwithout', 'upw', 'upwithout', '↑w'):
            x, y, fill = 0, -1, None
        elif command.split(':')[0].lower() in ('aw', 'awithout', 'leftw', 'leftwithout', '←w'):
            x, y, fill = -1, 0, None
        elif command.split(':')[0].lower() in ('sw', 'swithout', 'downw', 'downwithout', '↓w'):
            x, y, fill = 0, 1, None
        elif command.split(':')[0].lower() in ('dw', 'dwithout', 'rightw', 'rightwithout', '→w'):
            x, y, fill = 1, 0, None

        if command.split(':')[0].lower() in ('wd', 'wdelete', 'upd', 'updelete', '↑d'):
            x, y, fill = 0, -1, False
        elif command.split(':')[0].lower() in ('ad', 'adelete', 'leftd', 'leftdelete', '←d'):
            x, y, fill = -1, 0, False
        elif command.split(':')[0].lower() in ('sd', 'sdelete', 'downd', 'downdelete', '↓d'):
            x, y, fill = 0, 1, False
        elif command.split(':')[0].lower() in ('dd', 'ddelete', 'rightd', 'rightdelete', '→d'):
            x, y, fill = 1, 0, False

        if ':' in command:
            print(x, y, fill)
            for i in range(int(command.split(':')[-1])):
                wait(x, y, fill, color)
        else:
            wait(x, y, fill, color)
    placeBtns()

def move(x, y, fill, color):
    global pos
    if fill:
        tk.Canvas(root, bg=color, highlightthickness=0, borderwidth=0, width=scale, height=scale).place(x = pos[0] * scale, y = pos[1] * scale)
    elif fill == False:
        tk.Canvas(root, bg='#1b1b1b', highlightthickness=0, borderwidth=0, width=scale, height=scale).place(x = pos[0] * scale, y = pos[1] * scale)
    pos[0] += x
    pos[1] += y
    pointer.place(x = pos[0] * scale, y = pos[1] * scale)

    print(pos[0], pos[1])

def wait(x, y, fill, color):
    root.after(cooldown, lambda: move(x, y, fill, color))

root.mainloop()