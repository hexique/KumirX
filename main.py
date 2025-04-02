import tkinter as tk
from tkinter import filedialog, messagebox
from time import time
import math, random

__ver__ = '1.5.1'
__date__ = '02.04.2025'

if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'KumirX {__ver__}')
    root.geometry('1000x800')
    photo = tk.PhotoImage(file = 'icon.ico')
    root.iconphoto(True,photo)
    root.config(background='#1b1b1b')
    langvar = tk.BooleanVar()

    scale = 20
    cooldown = 0
    path = None
    color = 'white'
    colorbg = '#1b1b1b'
    start = time()
    item = 0
    pos = [0, 0]

    keywords = {
        ':': '|',

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

        'fill ': 'закрасить\n',
        'paint ': 'закрасить\n',

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

        'f ': 'закрасить\n',
        'p ': 'закрасить\n',

        'cd': '|',
        'sc': '|',

        'pointercolor': '|',
        'pointercol': '|',
        'pcol': '|',
        'pc': '|',

        'scale': '|',
        'cooldown': '|',

        'color': '|',
        'col': '|',

        'c': '|',

    }
    letters = {
        'a': 's:4 d ww:2 w ww d s:5 dw:2 ww:5 ',
        'b': 's:4 d:2 ww w aw w dw w aw d dw:2 ',
        'c': 's:4 d:2 w ww:3 a d dw:2 ',
        'd': 's:4 d d ww w:2 w aw d dw:2 ',
        'e': 's:4 d:2 w ww a w ww d:2 dw ',
        'f': 's:4 d ww:2 d w aw ww d:2 dw ',
        'g': 's:4 d:2 w:3 ww a d dw:2 ',
        'h': 's:4 d ww:2 w ww dw s:5 ww:5 dw:2 ',
        'i': 's:4 d ww:4 dw ',
        'j': 'd:2 s aw s:3 a p dw:4 ww:4 ',
        'k': 's:4 p dw:2 w:2 aw d ww w p dw:2 ',
        'l': 's:4 d:3 dw ww:4 ',
        'm': 's:4 d ww:3 d sw d ww d ww s:4 p dw:2 ww:4 ',
        'n': 's:4 p dw ww:3 d sw d s:2 w:4 p dw:2 ',
        'o': 's:4 d:2 w:4 a p dw:3 ',
        'p': 's:4 d ww:2 d w:2 a p dw:3 ',
        'q': 's:4 d:2 s d a ww:2 w:3 a p dw:4 ',
        'r': 's:4 p dw:2 w:2 aw d ww w aw p dw:3 ',
        's': 's:2 d:2 s:2 a:2 p ww:4 dw d:2 dw ',
        't': 'd:2 a sw s:3 p dw:3 ww:4 ',
        'u': 's:4 d:2 w:4 p dw:2 ',
        'v': 's:4 dw d ww w:3 p dw:2 ',
        'w': 's:4 dw d ww w:3 d sw:4 d ww w:3 p dw:2 ',
        'x': 's:2 sw s d ww:2 w ww dw s:2 sw s p dw:2 ww:4 ',
        'y': 's:3 sw d:2 w:2 a w dw w p dw:2 ',
        'z': 'd:2 s a sw a sw s d:3 dw ww:4 ',

        '0': 's:4 d:2 w:4 a p dw:3 ',
        '1': 's:4 p dw:2 ww:4 ',
        '2': 'd:2 s:2 a:2 s:2 d:2 p dw:2 ww:4 ',
        '3': 'd:2 s:2 a:2 s sw d:2 w d dw ww:3 ',
        '4': 's:2 d:2 w:2 w sw:4 s d dw ww:4 ',
        '5': 'd:2 s sw s:2 a:2 w ww d a ww p dw:4 ww ',
        '6': 's:4 d:2 w:2 a w ww d:2 dw ',
        '7': 'd:2 s:2 a d sw s d dw ww:4 ',
        '8': 's:4 d:2 w:4 a s sw s dw:3 ww:3 ',
        '9': 's:2 d:2 s:2 a:2 w ww:3 dw d s d dw ww ',

        '-': 'dw:4 ',
        '?': 'd:2 s:2 a:2 s sw p dw:4 ww:4 ',


    }
    functions = {

    }

def copy():
    root.clipboard_clear()
    root.clipboard_append(code.get('1.0',tk.END))
    print(code.get('1.0',tk.END))

def save(text, check):
    global path
    if path != None and check:
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
    if path is not None:
        confirm = messagebox.askyesnocancel(root.title(), "Unsaved changes detected. Do you want to save?", icon='warning')
        if confirm:
            save(code.get('1.0', tk.END), True)
        elif confirm is None:
            return
    file_path = filedialog.askopenfilename(

    )

    if file_path:
        path = file_path
        with open(file_path, "r", encoding="utf-8") as f:
            code.delete('1.0', tk.END)
            code.insert('1.0', f.read())
            root.title(f'KumirX {__ver__} - {file_path.split("/")[-1]}')

def update_settings():
    if langvar.get():
        print('turned on')
    else:
        print('turned off')

def settings():
    global langvar
    settings_root = tk.Toplevel(root)
    settings_root.title(f'KumirX {__ver__}')
    settings_root.geometry('500x500')
    settings_root.config(background='#1b1b1b')

    tk.Label(settings_root, text='Settings', fg='white', bg='#1b1b1b', font=('Arial',30)).place(x=10,y=10)
    tk.Checkbutton(settings_root, text='Hide buttons', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', variable=langvar, command=update_settings).place(x=10,y=60)
    
    settings_root.mainloop()

def placeBtns():
    if not langvar.get():
        if root.winfo_height()-30 <0:
            y = 770
        else: y = root.winfo_height()-30
        tk.Button(root,text='Run', bg='#1b1b1b', fg='white', command=lambda: run(code.get('1.0',tk.END), True)).place(x=10,y=y)
        tk.Button(root,text='Copy', bg='#1b1b1b', fg='white', command=copy).place(x=50,y=y)
        tk.Button(root,text='Save', bg='#1b1b1b', fg='white', command=lambda: save(code.get('1.0',tk.END), True)).place(x=100,y=y)
        tk.Button(root,text='Save as', bg='#1b1b1b', fg='white', command=lambda: save(code.get('1.0',tk.END), False)).place(x=145,y=y)

        tk.Button(root,text='Open', bg='#1b1b1b', fg='white', command=openfile).place(x=200,y=y)
        tk.Button(root,text='Settings', bg='#1b1b1b', fg='white', command=settings).place(x=250,y=y)

def update_widjets(event):
    code['height'] = root.winfo_height() / 16
    code['width'] = round((root.winfo_width()-740)/8.125)

if __name__ == '__main__':
    placeBtns()
    code = tk.Text(root, width=32, height=50, bg='#1b1b1b', fg='white', insertbackground='white')
    code.place(x=740,y=0)

# ←↑→↓

def run(code, resetpos):
    global scale, pointer, pos, cooldown, color, start, item, functions, colorbg
    if resetpos: 
        start = time()
        tk.Canvas(root, width=740, height=root.winfo_height(), bg=colorbg, highlightthickness=0).place(x=0,y=0)
        placeBtns()
        functions = {}
        pos = [0] * 2
        color = 'white'
        scale = 20
        x = 0
        y = 0
        pointer = tk.Canvas(root, bg='red', highlightthickness=0, borderwidth=0, width=scale, height=scale)
        pointer.place(x = pos[0] * 20, y = pos[1] * 20)
        fill = False
    for command in ' '.join(code.split('\n')).split():

        if command.split(':')[0].lower() in ('loop', 'for', 'l'):
            for item in range(int(command.split(':')[1])):
                print(item)
                for j in ':'.join(command.split(':')[2::]).split('_'):
                    print(j)
                    run(j.replace('%',':'), False)
            continue

        if command.split(':')[0].lower() in ('func', 'fun', 'f'):
            if command.split(':')[1].lower() in functions:
                run(functions[command.split(':')[1].lower()], False)
            else:
                functions[command.split(':')[1].lower()] = ':'.join(command.split(':')[2::]).replace('_',' ')
                print(functions)
            continue

        if command.split(':')[0].lower() in ('word', 'wo'):
            temp_code = ''
            for i in command.split(':')[-1]:
                if i in letters:
                    temp_code += letters[i]
                    print(i, temp_code)
                else:
                    temp_code += letters['?']
                    print('unknown letter:', i, temp_code)
            run(temp_code, False)
            print(f'run {command}')
            continue

        if command.split(':')[0].lower() in ('scale', 'sc'):
            scale = float(command.split(':')[-1])
            pointer.place(x = pos[0] * scale, y = pos[1] * scale)
            pointer['width'] = scale
            pointer['height'] = scale
            continue

        if command.split(':')[0].lower() in ('color', 'col', 'c'):
            color = command.split(':')[-1].replace('item',str(item))
            continue

        if command.split(':')[0].lower() in ('cooldown', 'cd'):
            cooldown = int(command.split(':')[-1])
            continue

        if command.split(':')[0].lower() in ('set', 'setpos', 'pos', 'sp'):
            # pos = [int(command.split(':')[1]), int(command.split(':')[-1])]
            pos = [eval(command.split(':')[1], globals()), eval(command.split(':')[-1], globals())]
            x, y, fill = 0, 0, False

        if command.split(':')[0].lower() in ('pointercolor', 'pointercol', 'pcol', 'pc'):
            pointer['bg'] = command.split(':')[-1]
            continue

        if command.split(':')[0].lower() in ('backgroundcolor', 'backgroundcol', 'bgcol', 'bgcolor', 'bc'):
            tk.Canvas(root, width=740, height=root.winfo_height(), bg=command.split(':')[-1], highlightthickness=0).place(x=0,y=0)
            placeBtns()
            pointercol = pointer['bg']
            pointer = tk.Canvas(root, bg=pointercol, highlightthickness=0, borderwidth=0, width=scale, height=scale)
            pointer.place(x = pos[0] * scale, y = pos[1] * scale)
            continue
        
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

        elif command.split(':')[0].lower() in ('fill', 'paint', 'p'):
            x, y, fill = 0, 0, True

        if ':' in command and not (command.startswith('set') or command.startswith('pos') or command.startswith('sp')):
            for i in range(int(command.split(':')[-1])):
                root.after(cooldown, move(x, y, fill, color), i+1)
        else:
            move(x, y, fill, color)
    if resetpos:
        placeBtns()
        print(f"Program was executed in {round(time() - start, 4)}s")

def move(x, y, fill, color):
    global pos
    if fill:
        root.after(cooldown, tk.Canvas(root, bg=color, highlightthickness=0, borderwidth=0, width=scale, height=scale).place(x = pos[0] * scale, y = pos[1] * scale))
    elif fill == False:
        tk.Canvas(root, bg='#1b1b1b', highlightthickness=0, borderwidth=0, width=scale, height=scale).place(x = pos[0] * scale, y = pos[1] * scale)
    pos[0] += x
    pos[1] += y
    pointer.place(x = pos[0] * scale, y = pos[1] * scale)

    # print(pos[0], pos[1])

def wait(x, y, fill, color):
    root.after(cooldown, lambda: move(x, y, fill, color))

if __name__ == '__main__':
    root.bind("<F5>", lambda event: run(code.get('1.0', tk.END), True))
    root.bind("<Control-s>", lambda event: save(code.get('1.0', tk.END), True))
    root.bind("<Control-Alt-s>", lambda event: save(code.get('1.0', tk.END), False))
    root.bind("<Control-Shift-s>", lambda event: save(code.get('1.0', tk.END), False))
    root.bind("<Control-o>", lambda event: openfile())
    root.bind("<Control-p>", lambda event: settings())

    root.bind("<Configure>", update_widjets)

    root.mainloop()