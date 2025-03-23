import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('KumirX')
root.geometry('1000x800')
photo = tk.PhotoImage(file = 'icon.ico')
root.iconphoto(True,photo)
root.config(background='#1b1b1b')

keywords = {
    'kumir': {
        'kumirx letters': {
            'закрасить\nвверх\n': 'w ',
            'закрасить\nвлево\n': 'a ',
            'закрасить\nвниз\n': 's ',
            'закрасить\nвправо\n': 'd ',

            'вверх\n': 'w ',
            'влево\n': 'a ',
            'вниз\n': 's ',
            'вправо\n': 'd ',

            'использовать Робот\nалг\nнач\n': '',
            'кон': '',
        },         
        'kumirx fullwords': {
            'закрасить\nвверх\n': 'up ',
            'закрасить\nвлево\n': 'left ',
            'закрасить\nвниз\n': 'down ',
            'закрасить\nвправо\n': 'right ',

            'вверх\n': 'upwithout ',
            'влево\n': 'leftwithout ',
            'вниз\n': 'downwithout ',
            'вправо\n': 'rightwithout ',

            'использовать Робот\nалг\nнач\n': '',
            'кон': '',
        }, 
        'kumirx words': {
            'акрасить\nвверх\nз': 'up ',
            'закрасить\nвлево\n': 'left ',
            'закрасить\nвниз\n': 'down ',
            'закрасить\nвправо\n': 'right ',

            'вверх\n': 'upw ',
            'влево\n': 'leftw ',
            'вниз\n': 'downw ',
            'вправо\n': 'rightw ',

            'использовать Робот\nалг\nнач\n': '',
            'кон': '',
        }, 
        'kumirx arrows': {
            'закрасить\nвверх\n': '↑ ',
            'закрасить\nвлево\n': '← ',
            'закрасить\nвниз\n': '↓ ',
            'закрасить\nвправо\n': '→ ',

            'вверх\n': '↑w ',
            'влево\n': '←w ',
            'вниз\n': '↓w ',
            'вправо\n': '→w ',

            'использовать Робот\nалг\nнач\n': '',
            'кон': '',
        }, 
    },
    'kumirx letters': {
        'kumir': {
            'w ': 'закрасить\nвверх\n',
            'a ': 'закрасить\nвлево\n',
            's ': 'закрасить\nвниз\n',
            'd ': 'закрасить\nвправо\n',

            'ww ': 'вверх\n',
            'aw ': 'влево\n',
            'sw ': 'вниз\n',
            'dw ': 'вправо\n',

            'wd ': 'вверх\n',
            'ad ': 'влево\n',
            'sd ': 'вниз\n',
            'dd ': 'вправо\n',

        },         
        'kumirx fullwords': {
            'w ': 'up ',
            'a ': 'left ',
            's ': 'down ',
            'd ': 'right ',

            'ww ': 'upwithout ',
            'aw ': 'leftwithout ',
            'sw ': 'downwithout ',
            'dw ': 'rightwithout ',

            'wd ': 'updelete ',
            'ad ': 'leftdelete ',
            'sd ': 'downdelete ',
            'dd ': 'rightdelete ',
        }, 
        'kumirx words': {
            'w ': 'up ',
            'a ': 'left ',
            's ': 'down ',
            'd ': 'right ',

            'ww ': 'upw ',
            'aw ': 'leftw ',
            'sw ': 'downw ',
            'dw ': 'rightw ',

            'wd ': 'upd ',
            'ad ': 'leftd ',
            'sd ': 'downd ',
            'dd ': 'rightd ',
        }, 
        'kumirx arrows': {
            'w ': '↑ ',
            'a ': '← ',
            's ': '↓ ',
            'd ': '→ ',

            'ww ': '↑w ',
            'aw ': '←w ',
            'sw ': '↓w ',
            'dw ': '→w ',

            'wd ': '↑d ',
            'ad ': '←d ',
            'sd ': '↓d ',
            'dd ': '→d ',
        }, 
    },
    'kumirx fullwords': {
        'kumir': {
            'up ': 'закрасить\nвверх\n',
            'left ': 'закрасить\nвлево\n',
            'down ': 'закрасить\nвниз\n',
            'right ': 'закрасить\nвправо\n',

            'upwithout ': 'вверх\n',
            'leftwithout ': 'влево\n',
            'downwithout ': 'вниз\n',
            'rightwithout ': 'вправо\n',

            'updelete ': 'вверх\n',
            'leftdelete ': 'влево\n',
            'downdelete ': 'вниз\n',
            'rightdelete ': 'вправо\n',

        },         
        'kumirx letters': {
            'up ': 'w ',
            'left ': 'a ',
            'down ': 's ',
            'right ': 'd ',

            'upwithout ': 'ww ',
            'leftwithout ': 'aw ',
            'downwithout ': 'sw ',
            'rightwithout ': 'dw ',

            'updelete ': 'wd ',
            'leftdelete ': 'aw ',
            'downdelete ': 'sw ',
            'rightdelete ': 'dw ',
        }, 
        'kumirx words': {
            'up ': 'up ',
            'left ': 'left ',
            'down ': 'down ',
            'right ': 'right ',

            'upwithout ': 'upw ',
            'leftwithout ': 'leftw ',
            'downwithout ': 'downw ',
            'rightwithout ': 'rightw ',

            'updelete ': 'upd ',
            'leftdelete ': 'leftd ',
            'downdelete ': 'downd ',
            'rightdelete ': 'rightd ',
        }, 
        'kumirx arrows': {
            'up ': '↑ ',
            'left ': '← ',
            'down ': '↓ ',
            'right ': '→ ',

            'upwithout ': '↑w ',
            'leftwithout ': '←w ',
            'downwithout ': '↓w ',
            'rightwithout ': '→w ',

            'updelete ': '↑d ',
            'leftdelete': '←d ',
            'downdelete ': '↓d ',
            'rightdelete ': '→d ',
        }, 
    },
    'kumirx words': {
        'kumir': {
            'up ': 'закрасить\nвверх\n',
            'left ': 'закрасить\nвлево\n',
            'down ': 'закрасить\nвниз\n',
            'right ': 'закрасить\nвправо\n',

            'upw ': 'вверх\n',
            'leftw ': 'влево\n',
            'downw ': 'вниз\n',
            'rightw ': 'вправо\n',

            'upd ': 'вверх\n',
            'leftd ': 'влево\n',
            'downd ': 'вниз\n',
            'rightd ': 'вправо\n',

        },         
        'kumirx letters': {
            'up ': 'w ',
            'left ': 'a ',
            'down ': 's ',
            'right ': 'd ',

            'upw ': 'ww ',
            'leftw ': 'aw ',
            'downw ': 'sw ',
            'rightw ': 'dw ',

            'upd ': 'wd ',
            'leftd ': 'aw ',
            'downd ': 'sw ',
            'rightd ': 'dw ',
        }, 
        'kumirx fullwords': {
            'up ': 'up ',
            'left ': 'left ',
            'down ': 'down ',
            'right ': 'right ',

            'upw ': 'upwithout ',
            'leftw ': 'leftwithout ',
            'downw ': 'downwithout ',
            'rightw ': 'rightwithout ',

            'upd ': 'updelete ',
            'leftd ': 'leftdelete ',
            'downd ': 'downdelete ',
            'rightd ': 'rightdelete ',
        }, 
        'kumirx arrows': {
            'up ': '↑ ',
            'left ': '← ',
            'down ': '↓ ',
            'right ': '→ ',

            'upw ': '↑w ',
            'leftw ': '←w ',
            'downw ': '↓w ',
            'rightw ': '→w ',

            'upd ': '↑d ',
            'leftd ': '←d ',
            'downd ': '↓d ',
            'rightd ': '→d ',
        }, 
    },
    'kumirx arrows': {
        'kumir': {
            '↑ ': 'вверх\nзакрасить\n',
            '← ': 'влево\nзакрасить\n',
            '↓ ': 'вниз\nзакрасить\n',
            '→ ': 'вправо\nзакрасить\n',

            '↑w ': 'вверх\n',
            '←w ': 'влево\n',
            '↓w ': 'вниз\n',
            '→w ': 'вправо\n',

            '↑d ': 'вверх\n',
            '←d ': 'влево\n',
            '↓d ': 'вниз\n',
            '→d ': 'вправо\n',

        },         
        'kumirx letters': {
            '↑ ': 'w ',
            '← ': 'a ',
            '↓ ': 's ',
            '→ ': 'd ',

            '↑w ': 'ww ',
            '←w ': 'aw ',
            '↓w ': 'sw ',
            '→w ': 'dw ',

            '↑d ': 'wd ',
            '←d ': 'aw ',
            '↓d ': 'sw ',
            '→d ': 'dw ',
        }, 
        'kumirx fullwords': {
            '↑ ': 'up ',
            '← ': 'left ',
            '↓ ': 'down ',
            '→ ': 'right ',

            '↑w ': 'upwithout ',
            '←w ': 'leftwithout ',
            '↓w ': 'downwithout ',
            '→w ': 'rightwithout ',

            '↑d ': 'updelete ',
            '←d ': 'leftdelete ',
            '↓d ': 'downdelete ',
            '→d ': 'rightdelete ',
        }, 
        'kumirx words': {
            '↑ ': 'up ',
            '← ': 'left ',
            '↓ ': 'down ',
            '→ ': 'right ',

            '↑w ': 'upw ',
            '←w ': 'leftw ',
            '↓w ': 'downw ',
            '→w ': 'rightw ',

            '↑d ': 'upd ',
            '←d': 'leftd ',
            '↓d ': 'downd ',
            '→d ': 'rightd ',
        }, 
    },
}

langvar = tk.StringVar(value='Kumir')
lang = 'kumir'
pos = [0, 0]
result = '''использовать Робот
алг
нач
'''

def copy():
    root.clipboard_clear()
    root.clipboard_append(code.get('1.0',tk.END))
    print(code.get('1.0',tk.END))

def update_settings():
    global lang, result
    code_og = code.get('1.0',tk.END)
    lang_og = langvar.get()
    code.delete('1.0',tk.END)
    for i in keywords[lang][lang_og].keys():
        code_og = code_og.replace(i, keywords[lang][lang_og][i])
        print(i, keywords[lang][lang_og][i])

    if langvar.get() == 'kumir':
        result = f'использовать Робот\nалг\nнач\n{code_og}\nкон'
        code.insert('1.0',f'{result}')
    elif langvar.get() == 'kumirx letters':
        result = code_og
        code.insert('1.0',f'{code_og}')
    elif langvar.get() == 'kumirx fullwords':
        result = code_og
        code.insert('1.0',f'{code_og}')
    elif langvar.get() == 'kumirx words':
        result = code_og
        code.insert('1.0',f'{code_og}')
    elif langvar.get() == 'kumirx arrows':
        result = code_og
        code.insert('1.0',f'{code_og}')
    lang = langvar.get()

def settings():
    global langvar
    settings_root = tk.Toplevel(root)
    settings_root.title('Settings')
    settings_root.geometry('500x500')
    settings_root.config(background='#1b1b1b')

    tk.Label(settings_root, text='Programming system', font=('Arial',15), background='#1b1b1b', foreground='white').place(x=10,y=10)

    tk.Radiobutton(settings_root, text='Kumir', background='#1b1b1b', foreground='white', value='kumir', variable=langvar, selectcolor='#1b1b1b', command=update_settings).place(x=10,y=40)
    tk.Radiobutton(settings_root, text='KumirX (letters)', background='#1b1b1b', foreground='white', value='kumirx letters', variable=langvar, selectcolor='#1b1b1b', command=update_settings).place(x=10,y=60)
    tk.Radiobutton(settings_root, text='KumirX (fullwords)', background='#1b1b1b', foreground='white', value='kumirx fullwords', variable=langvar, selectcolor='#1b1b1b', command=update_settings).place(x=10,y=80)
    tk.Radiobutton(settings_root, text='KumirX (words)', background='#1b1b1b', foreground='white', value='kumirx words', variable=langvar, selectcolor='#1b1b1b', command=update_settings).place(x=10,y=100)
    tk.Radiobutton(settings_root, text='KumirX (arrows)', background='#1b1b1b', foreground='white', value='kumirx arrows', variable=langvar, selectcolor='#1b1b1b', command=update_settings).place(x=10,y=120)

    settings_root.mainloop()

pointer = tk.Canvas(root, bg='red', highlightthickness=0, borderwidth=0, width=20, height=20)
pointer.place(x = pos[0] * 20, y = pos[1] * 20)

code = tk.Text(root, width=32, height=50, bg='#1b1b1b', fg='white')
code.place(x=740,y=0)

tk.Button(root,text='Copy', bg='#1b1b1b', fg='white', command=copy).place(x=10,y=770)
tk.Button(root,text='Settings', bg='#1b1b1b', fg='white', command=settings).place(x=60,y=770)

def move(x, y, fill):
    global pos, result
    if fill:
        tk.Canvas(root, bg='white', highlightthickness=0, borderwidth=0, width=20, height=20).place(x = pos[0] * 20, y = pos[1] * 20)
    elif fill == False:
        tk.Canvas(root, bg='#1b1b1b', highlightthickness=0, borderwidth=0, width=20, height=20).place(x = pos[0] * 20, y = pos[1] * 20)
    pos[0] += x
    pos[1] += y
    pointer.place(x = pos[0] * 20, y = pos[1] * 20)

    code.delete('1.0',tk.END)
    if lang == 'kumir':
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
        code.insert('1.0',f'{result}\nкон')
        return
    elif lang == 'kumirx letters':
        if y == -1:
            result += 'w'
        elif y == 1:
            result += 's'
        elif x == -1:
            result += 'a'
        elif x == 1:
            result += 'd'
        if fill:
            result += ' '
        elif fill is None:
            result += 'w '
        elif fill is False:
            result += 'd '
    elif lang == 'kumirx fullwords':
        if y == -1:
            result += 'up'
        elif y == 1:
            result += 'down'
        elif x == -1:
            result += 'left'
        elif x == 1:
            result += 'right'
        if fill:
            result += ' '
        elif fill is None:
            result += 'without '
        elif fill is False:
            result += 'delete '
    elif lang == 'kumirx words':
        if y == -1:
            result += 'up'
        elif y == 1:
            result += 'down'
        elif x == -1:
            result += 'right'
        elif x == 1:
            result += 'left'
        if fill:
            result += ' '
        elif fill is None:
            result += 'w '
        elif fill is False:
            result += 'd '
    elif lang == 'kumirx arrows':
        if y == -1:
            result += '↑'
        elif y == 1:
            result += '↓'
        elif x == -1:
            result += '←'
        elif x == 1:
            result += '→'
        if fill:
            result += ' '
        elif fill is None:
            result += 'w '
        elif fill is False:
            result += 'd '
    code.insert('1.0',f'{result}')

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

root.bind("<Alt-w>", lambda event: move(0, -1, False))
root.bind("<Alt-a>", lambda event: move(-1, 0, False))
root.bind("<Alt-s>", lambda event: move(0, 1, False))
root.bind("<Alt-d>", lambda event: move(1, 0, False))



root.mainloop()