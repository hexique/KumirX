# graph.py

import tkinter as tk
from tkinter import filedialog, messagebox
from webbrowser import open as openpage
from time import time, ctime
from json import load as loadjson, dump, dumps, loads

from graphfunc import *
import random
from math import *

with open('version.json') as f:
    __ver__ = loadjson(f)['ver']

def loop(function, **kwargs):
    for item in range(kwargs['start'], kwargs['end']):
        graph(function=function.replace('item', str(item)), looped=True)

if __name__ == '__main__':
    root = tk.Tk()
    root.title(f'KxGraph {__ver__}')
    root.geometry('1000x800')
    photo = tk.PhotoImage(file = 'icon.ico')
    root.iconphoto(True,photo)
    root.config(background='#1b1b1b')
    root.wm_attributes("-transparentcolor", "#0a2b0d")

    step = 'x+1'
    scale = '10'
    offset = {'x': 30, 'y': 40}
    index = -1
    default_graphcol = '#ffffff'
    x = -offset['x']
    audit = []
    key_objs = [[], []]

    switch_color = tk.BooleanVar(value=True)
    error_graph = tk.BooleanVar(value=True)
    one_graph_max = tk.BooleanVar(value=False)
    hide_btn = tk.BooleanVar(value=False)
    hide_dot_info = tk.BooleanVar(value=True)

    colors = ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#00ffff', '#ff00ff', '#ffffff']
    shortcuts = {'Return': 'graph(function=func.get())',
                 'F5': 'graph(function=func.get())',
                 'Delete': 'reset()',
                 'Escape': 'delete(index)',
                 'Control-Escape': 'delete(-1)',
                 'Shift-Escape': 'delete(0)',
                 'Control-p': 'settings()',
                 'Tab': 'settings()',
                 'Control-s': 'save(audit)',
                 'Control-o': 'load()',
                 'Control-g': 'colortable()'}

    def switch(*args):
        if type(args[0]) == list:
            return eval(args[0][int(x) % len(args[0])], globals(), locals())
        return eval(args[int(x) % len(args)], globals(), locals())

def tojson(text):
    return str(text).replace("'", '"').replace("True", "true").replace("False", "true").replace("<", '"<').replace(">", '>"').replace(", ", ",\n")

def format_dictionary(dict):
    result = ''
    for graph in dict:
        result += f'''Function: {graph['function']}\n
Graph: {graph['graphs']}
Scale: {graph['scale']} ({eval(graph['scale'])})
Step: {graph['step']}
Offset X: {graph['offset']['x']}
Offset Y: {graph['offset']['y']}
Color: {graph['color']} ({graph['firstcolor']})
Colors: {' '.join(graph['colors'])}

Different color for every graph: {graph['switch_color']}
Delete graph after error: {graph['error_graph']}
Graph switch: {graph['one_graph_max']}\n\n'''
        for dot in graph['dots']:
            print(dot)
            result += f'    {dot["x"]} : {dot["y"]}\n'
        result += f'''
Dots in graph: {graph['graph_total']}
Total dots of all time: {graph['alltime_total']}

{'-'*20}

'''
    return result
            


def save(text):
    file_path = filedialog.asksaveasfilename(
            initialfile=f"{func.get()}.txt",
            defaultextension=".txt",
            title="Save file",
            filetypes=[("Text file", "*.txt"), ("JSON file", "*.json"), ("Raw file", "*.kxg"), ("All files", "*.*")]
    )

    if file_path:
        if file_path.endswith('.txt'):

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(format_dictionary(audit))
        elif file_path.endswith('.kxg'):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(str(text))
        elif file_path.endswith('.json'):
            with open(file_path, "w", encoding="utf-8") as f:
                temp_audit = audit.copy()
                for graph in temp_audit:
                    for dot in graph['dots']:
                        dot.pop('object', None)
                f.write(dumps(temp_audit))
                # f.write(str(dumps(text)))

def load():
    global audit, colors

    file_path = filedialog.askopenfilename(
            title="Open file",
            filetypes=[("JSON file", "*.json"), ("Raw file", "*.kxg"), ("All files", "*.*")]
    )
    if file_path:
        with open(file_path, 'r') as f:

            jsoned_audit = loadjson(f)
            colors = jsoned_audit[-1]['colors']
            for element in jsoned_audit:
                graph(function=element['function'])
            print(f'File loaded succesfuly')

            

def save_settings():
    try:
        props = {"step": step, "scale": scale, "offset": offset, "index": index, "switch_color": switch_color.get(), "error_graph": error_graph.get(), "one_graph_max": one_graph_max.get(), "hide_btn": hide_btn.get(),  "hide_dot_info": hide_dot_info.get(), "bg": root.cget("bg"), "graphcol": default_graphcol, "linecol": linex["bg"], "colors": colors}
    except Exception as e:
        print(f'Error occured while settings save {e}')
        return
    with open('props.json', "w", encoding="utf-8") as f:
        print(props)
        dump(props, f, indent=4)
    # with open('props.json', 'w') as f:
    #     try:
    #         props = tojson({"step": step, "scale": scale, "offset": offset, "index": index, "switch_color": switch_color.get(), "error_graph": error_graph.get(), "one_graph_max": one_graph_max.get(), "hide_btn": hide_btn.get(), "bg": root.cget("bg"), "graphcol": default_graphcol, "linecol": linex["bg"], "colors": colors})
    #         props = {"step": step, "scale": scale, "offset": offset, "index": index, "switch_color": switch_color.get(), "error_graph": error_graph.get(), "one_graph_max": one_graph_max.get(), "hide_btn": hide_btn.get(), "bg": root.cget("bg"), "graphcol": default_graphcol, "linecol": linex["bg"], "colors": colors}
    #         # props = tojson({"step": step, "scale": scale, "offset": offset, "index": index, "switch_color": switch_color.get(), "error_graph": error_graph.get(), "one_graph_max": one_graph_max.get(), "hide_btn": hide_btn.get(), "bg": root.cget("bg"), "graphcol": default_graphcol, "linecol": linex["bg"], "colors": colors})
    #         f.write(props)
    #         # print(f'Properties saved succesfuly ({props})')
    #         # f.close()
    #     except Exception as e:
    #         print(e)
        

def save_settings_file():
    file_path = filedialog.asksaveasfilename(
            initialfile=f"customprops.json",
            defaultextension=".json",
            title="Save file",
            filetypes=[("JSON file", "*.json"), ("Text file", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        if file_path.endswith('.txt'):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f'''
Step: {step}
Offset X: {offset['x']}
Offset Y: {offset['y']}
Index: {index}
Scale: {scale}

Different color for every graph: {switch_color.get()}
Delete graph after error: {error_graph.get()}
Graph switch: {one_graph_max.get()}
Hide buttons: {hide_btn.get()}

Background color: {root.cget('bg')}
Graph color: {default_graphcol}
Offset color: {liney['bg']}

Colors: {' '.join(colors)}
''')

        elif file_path.endswith('.dat'):
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(f'{step} {scale} {offset["x"]} {offset["y"]} {index} {switch_color.get()} {error_graph.get()} {one_graph_max.get()} {hide_btn.get()} {root.cget("bg")} {default_graphcol} {linex["bg"]}')
        elif file_path.endswith('.json'):
            with open(file_path, "w", encoding="utf-8") as f:
                props = {"step": step, "scale": scale, "offset": offset, "index": index, "switch_color": switch_color.get(), "error_graph": error_graph.get(), "one_graph_max": one_graph_max.get(), "hide_btn": hide_btn.get(), "bg": root.cget("bg"), "graphcol": default_graphcol, "linecol": linex["bg"], "colors": colors}
                f.write(f'{dump(props, f, indent=4)}')

def load_settings_file():
    file_path = filedialog.askopenfilename(
            title="Open file",
            filetypes=[("JSON file", "*.json")]
    )
    if file_path:
        load_settings(file_path)

def load_settings(path):
    global step, scale, offset, index, default_graphcol, switch_color, error_graph, hide_dot_info
    with open(path, 'r') as f:
        # file = f.read()
        # file = file.split()

        # step = float(file[0])
        # scale = file[1]
        # offset['x'] = float(file[2])
        # offset['y'] = float(file[3])
        # index = int(file[4])
        
        # switch_color.set(file[5] == 'True')
        # error_graph.set(file[6] == 'True')
        # one_graph_max.set(file[7] == 'True')
        # hide_btn.set(file[8] == 'True')

        # root.config(background=file[9])
        # default_graphcol = file[0]
        # linex['bg'] = file[11]
        # liney['bg'] = file[11]
        file = loadjson(f)

        step = file['step']
        scale = file['scale']
        offset['x'] = file['offset']['x']
        offset['y'] = file['offset']['y']
        index = file['index']
        
        switch_color.set(file['switch_color'])
        error_graph.set(file['error_graph'])
        one_graph_max.set(file['one_graph_max'])
        hide_btn.set(file['hide_btn'])
        hide_dot_info.set(file['hide_dot_info'])

        root.config(background=file['bg'])
        default_graphcol = file['graphcol']
        linex['bg'] = file['linecol']
        liney['bg'] = file['linecol']

    save_settings()

def showinfo(id):
    info_root = tk.Toplevel(root)
    info_root.title(f'KxGraph {__ver__}')
    info_root.config(background='#1b1b1b')

    tk.Label(info_root, text=audit[id]['function'], bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", columnspan=3, row=0, column=0)
    tk.Label(info_root, text='№', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=1,column=0)
    tk.Label(info_root, text='x', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=1,column=1)
    tk.Label(info_root, text='y', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=1,column=2)

    i = 2
    for dot in audit[id]['dots']:
        tk.Label(info_root, text=str(i), bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=0)
        tk.Label(info_root, text=dot['x'], bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=1)
        tk.Label(info_root, text=dot['y'], bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=2)

        i += 1
    info_root.mainloop()

def colortable():
    color_root = tk.Toplevel(root)
    color_root.title(f'KxGraph {__ver__}')
    color_root.config(background='#1b1b1b')
    tk.Label(color_root, text='№', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=0)
    tk.Label(color_root, text='Color', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=1)
    tk.Label(color_root, text='Function', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=2)
    tk.Label(color_root, text='Dots total', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=3)
    tk.Label(color_root, text='Step', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=4)
    tk.Label(color_root, text='Scale', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=5)
    tk.Label(color_root, text='Offset', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=0,column=6)

    i = 1
    for graph in audit:
        try:
            tk.Label(color_root, text=graph['graphs'], bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=0)
            tk.Label(color_root, text=graph['color'].lower(), bg=graph['color'], font=("TkFixedFont"), justify='left', anchor='w').grid(sticky="W", row=i,column=1)
            tk.Label(color_root, text=graph['function'], bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=2)
            tk.Label(color_root, text=len(graph['dots']), bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=3)
            tk.Label(color_root, text=str(graph['step']), bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=4)
            tk.Label(color_root, text=eval(graph['scale']), bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=5)
            tk.Label(color_root, text=graph['offset']['y'], bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w').grid(sticky="W", row=i,column=6)
            tk.Button(color_root, text='More info', bg='#1b1b1b', fg='#ffffff', justify='left', anchor='w', font=('TkDefaultFont', 7), command=lambda i=i: showinfo(i-1)).grid(sticky="W", row=i,column=7)

            i += 1
        except Exception as e:
            print(e)
    tk.Button(color_root, text='Audit', bg='#1b1b1b', fg='#ffffff', command=lambda: show_audit(format_dictionary(audit))).grid(sticky="ew", row=i+1, column=0, columnspan=2)
    tk.Button(color_root, text='Raw dictionary', bg='#1b1b1b', fg='#ffffff', command=lambda: show_audit(str(audit))).grid(sticky="ew", row=i+1, column=2, columnspan=1)

    color_root.mainloop()

def show_audit(text):
    audit_root = tk.Toplevel(root)
    audit_root.title(f'KxGraph {__ver__}')
    audit_root.geometry('500x500')
    audit_root.config(background='#1b1b1b')
    
    audit_display = tk.Text(audit_root, height=20, width=50, bg='#1b1b1b', fg='#ffffff')
    audit_display.insert('1.0', text.replace(', ',',\n'))
    audit_display['state'] = 'disabled'
    audit_display.pack(fill=tk.BOTH, expand=True)


    audit_root.mainloop()

def graph(**kwargs):
    global x, y, audit, colors
    function = kwargs["function"] # i will fix this later
    if '|' in function:
        for i in function.split('|'):
            graph(function=i)
        return
    x = -offset['x']
    if one_graph_max.get():
        delete(-1)
    if 'loop' not in function and 'modify' not in kwargs.keys():
        audit.append({'function': function,
                    'scale': scale,
                    'evalscale': eval(scale),
                    'step': step,
                    'offset': offset,

                    'switch_color': switch_color.get(),
                    'error_graph': error_graph.get(),
                    'one_graph_max': one_graph_max.get(),
                    
                    'dots': []})
    if switch_color.get():
        if len(audit) > len(colors):
            while True:
                color = '#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255))
                if color != "#0a2b0d": break
            colors.append(color)
        else:
            color = colors[len(audit)-1]
    else:
        color = default_graphcol
    # audit += f'Function: {function}\nGraph: {len(graphs)}\nScale: {eval(scale)} ({scale})\nStep: {step}\nOffset: {offset}\nColor: {color}\n\nDifferent color for every graph: {switch_color.get()}\nDelete graph after error: {error_graph.get()}\nGraph switch: {one_graph_max.get()}\n\nDots:\n'
                #       'color': color,
                #   'firstcolor': color,
                #   'colors': colors,

    if 'loop' not in function and 'modify' not in kwargs.keys():
        audit[-1]['color'] = color
        audit[-1]['firstcolor'] = color
        audit[-1]['colors'] = colors

    while True:
        if x > int(root.winfo_width()/eval(scale, globals())):
            break
        try:
            function
            if eval(function, globals())+offset['y'] >= root.winfo_height()/eval(scale)-2 and x-offset['x'] <= 0: 
                print(eval(function, globals())+offset['y'], root.winfo_height()/eval(scale)-2)
                x = eval(step, globals(), locals())
                print('x:', x)
                continue
            
            else:
                y = (eval(function, globals())+offset['y'])*eval(scale, globals())
                dot = tk.Canvas(root, width=eval(scale, globals()), height=eval(scale, globals()), highlightthickness=0, bg=color)
                dot.bind("<Enter>", lambda event, x=x, y=y, function=function, dot=dot: display_dot_info(x, y, function, dot))
                dot.bind("<Leave>", lambda event, x=x, y=y, function=function, dot=dot: display_dot_info(x, y, function, dot, hide=True)) 
                dot.place(x=(x+offset['x'])*eval(scale, globals()),y=(eval(f'-({function})', globals())+offset['y'])*eval(scale, globals()))
                if x == eval(step, globals(), locals()) and len(audit[-1]['dots']) >= root.winfo_width()/eval(scale):
                    break
                print('x:', x)
                if 'loop' not in function and 'modify' not in kwargs.keys():
                    audit[-1]['dots'].append({})
                    audit[-1]['dots'][-1]['x'] = x
                    audit[-1]['dots'][-1]['y'] = eval(function, globals())
                    audit[-1]['dots'][-1]['object'] = dot
        except ZeroDivisionError:
            x = eval(step, globals(), locals())
            continue
        except IndexError:
            pass
        except Exception as e:
            # if 'looped' not in kwargs.keys() and 'sqrt' not in kwargs.keys():
            #     if len(audit) > 0:
            #         messagebox.showerror('KxGraph',f'Error occured while drawing a graph\n\n{e}\nx = {x}\nDots total: {len(audit[-1]["dots"])}')
            #     else:
            #         messagebox.showerror('KxGraph',f'Error occured while drawing a graph\n\n{e}\nx = {x}\nDots total: undefined')
            #     if error_graph.get():
            #         delete(index)
            #     return 
            pass
        x = eval(step, globals(), locals())
    if 'loop' not in function and 'modify' not in kwargs.keys():
        total_dots = 0
        for i in audit:
            total_dots += len(i['dots'])
        audit[-1]['graph_total'] = len(audit[-1]['dots'])
        audit[-1]['alltime_total'] = total_dots
        audit[-1]['graphs'] = len(audit)

    if len(audit) != 0:
        print(f'Total dots: {len(audit[-1]["dots"])}')
            
def display_dot_info(x, y, function, dot_obj, hide=False):
    #0a2b0d
    if hide and hide_dot_info.get():
        dot_info["fg"] = root.cget("bg")
        dot_info["text"] = ""
        return
    elif hide:
        return
    dot_info["fg"] = dot_obj["bg"]
    dot_info["text"] = f"Function: {function}\nx: {x}\ny: {y}"

def reset():
    # tk.Canvas(root, width=root.winfo_width(), height=root.winfo_height()-20, bg='#1b1b1b', highlightthickness=0).place(x=0,y=0)
    global object, audit
    for graph in audit:
        for object in graph['dots']:
            object['object'].destroy()
    audit = []

def delete(index):
    global audit, object
    if len(audit) == 0: return
    if len(audit) != 0:
        for object in audit[index]['dots']:
            object['object'].destroy()
    audit.pop(index)
    
def update_settings():
    cust_btn.place(x=settings_root.winfo_width()-100,y=settings_root.winfo_height()-40)
    keys_btn.place(x=settings_root.winfo_width()-170,y=settings_root.winfo_height()-40)

def update_color(event):
    colors_label.place(x=70,y=color_root.winfo_height()-100)
    colors_entry.place(x=10,y=color_root.winfo_height()-100)
    colors_display.place(x=10,y=color_root.winfo_height()-70)

    addcol_btn.place(x=10,y=color_root.winfo_height()-40)
    deletecol_btn.place(x=50,y=color_root.winfo_height()-40)
    clearcol_btn.place(x=100,y=color_root.winfo_height()-40)

def clearcol():
    global colors
    colors = []
    colors_display['text'] = ' '.join(colors)

def addcol(element):
    global colors
    colors.append(element)
    colors_display['text'] = ' '.join(colors)
    if audit[len(colors)-1]['dots'] and audit[len(colors)-1]['dots'][0]['object']['bg'] != colors[-1]:
        for dot in audit[len(colors)-1]['dots']:
            dot['object']['bg'] = colors[-1]
            print(dot['object']['bg'], ':', dot['object'])
    audit[len(colors)-1]['color'] = colors[-1]

def deletecol(index):
    global colors
    colors.pop(index)
    colors_display['text'] = ' '.join(colors)

def colorsettings():
    global color_root, offsetcol_entry, bgcol_entry, graphcol_entry, colors_entry, colors_display, colors_label
    global addcol_btn, deletecol_btn, clearcol_btn, bgcol_preview, graphcol_preview, offsetcol_preview, colors_preview

    color_root = tk.Toplevel(root)
    color_root.title(f'KxGraph {__ver__}')
    color_root.geometry('500x500')
    color_root.config(background='#1b1b1b')

    tk.Label(color_root, text='Customization', fg='white', bg='#1b1b1b', font=('Arial',30)).place(x=10,y=10)

    tk.Label(color_root, text='Background color', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=95,y=60)
    bgcol_entry = tk.Entry(color_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    bgcol_entry.insert(0, root.cget('bg'))
    bgcol_entry.place(x=35,y=60)
    bgcol_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Label(color_root, text='Graph color', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=95,y=90)
    graphcol_entry = tk.Entry(color_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    graphcol_entry.insert(0, default_graphcol)
    graphcol_entry.place(x=35,y=90)
    graphcol_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Label(color_root, text='Offset color', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=95,y=120)
    offsetcol_entry = tk.Entry(color_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    offsetcol_entry.insert(0, linex['bg'])
    offsetcol_entry.place(x=35,y=120)
    offsetcol_entry.bind("<KeyRelease>", lambda event: apply())

    colors_label = tk.Label(color_root, text='Graph color massive', fg='white', bg='#1b1b1b', font=('Arial',10))
    colors_label.place(x=85,y=130)
    colors_entry = tk.Entry(color_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    colors_entry.place(x=35,y=120)
    colors_entry.bind("<KeyRelease>", lambda event: apply())
    
    colors_display = tk.Label(color_root, text=' '.join(colors), fg='white', bg='#1b1b1b', font=('Arial',10))
    colors_display.place(x=10,y=180)

    addcol_btn = tk.Button(color_root, text='Add', bg='#1b1b1b', fg='white', command=lambda: addcol(colors_entry.get()))
    addcol_btn.place(x=25,y=150)

    deletecol_btn = tk.Button(color_root, text='Delete', bg='#1b1b1b', fg='white', command=lambda: deletecol(index))
    deletecol_btn.place(x=90,y=150)

    clearcol_btn = tk.Button(color_root, text='Clear', bg='#1b1b1b', fg='white', command=clearcol)
    clearcol_btn.place(x=170,y=150)

    try:
        bgcol_preview = tk.Canvas(color_root, height=20, width=20, bg=root.cget('bg'), highlightthickness=0)
        bgcol_preview.place(x=10,y=60)
        graphcol_preview = tk.Canvas(color_root, height=20, width=20, bg=default_graphcol, highlightthickness=0)
        graphcol_preview.place(x=10,y=90)
        colors_preview = tk.Canvas(color_root, height=20, width=20, bg=colors_entry.get(), highlightthickness=0)
        colors_preview.place(x=10,y=120)
        offsetcol_preview = tk.Canvas(color_root, height=20, width=20, bg=offsetcol_entry.get(), highlightthickness=0)
        offsetcol_preview.place(x=10,y=120)
    except:
        pass
    color_root.bind('<Configure>', update_color)
    color_root.mainloop()

def apply_keys():
    global shortcuts
    shortcuts = {} # spaghetti code goes brrrrrr 💀
    for shortcut in range(len(key_objs[0])):
        shortcuts[key_objs[0][shortcut].get()] = key_objs[1][shortcut].get()



def keys_settings():
    global key_entry, action_entry, key_objs
    key_root = tk.Toplevel(root)
    key_root.title(f'KxGraph {__ver__}')
    key_root.geometry('500x500')
    key_root.config(background='#1b1b1b')

    tk.Label(key_root, text='Shortcuts', fg='white', bg='#1b1b1b', font=('Arial',30)).grid(row=0,column=0,padx=10)

    key_objs = [[], []]

    i = 1
    for key in shortcuts:
        key_entry = tk.Entry(key_root, width=10, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
        key_objs[0].append(key_entry)
        key_entry.insert(0, key)
        key_entry.bind("<KeyRelease>", lambda event: apply_keys())
        key_entry.grid(row=i, column=0, pady=5)

        action_entry = tk.Entry(key_root, width=30, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
        key_objs[1].append(action_entry)
        action_entry.insert(0, shortcuts[key])
        action_entry.bind("<KeyRelease>", lambda event: apply_keys())
        action_entry.grid(row=i, column=1, pady=5)
        i += 1

    # tk.Label(key_root, text='Background color', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=95,y=60)
    # bgcol_entry = tk.Entry(key_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    # bgcol_entry.insert(0, root.cget('bg'))
    # bgcol_entry.place(x=35,y=60)
    # bgcol_entry.bind("<KeyRelease>", lambda event: apply())

    #key_root.bind('<Configure>', update_color)
    key_root.mainloop()

def apply():
    global step, offset, index, scale, default_graphcol, linex, liney
    global bgcol_preview, graphcol_entry, offsetx_entry, colors_preview
    try:
        step = step_entry.get()
        offset['x'] = float(offsetx_entry.get())
        offset['y'] = float(offsety_entry.get())
        print('offset', offset)
        index = int(index_entry.get())
        scale = scale_entry.get()

        linex.place(y=0,x=offset['x']*eval(scale, globals()))
        print(0, offset['x']*eval(scale, globals()), eval(scale, globals()))
        linex['width'] = eval(scale, globals())

        liney.place(x=0,y=offset['y']*eval(scale, globals()))
        print(offset['y']*eval(scale, globals()), 0, eval(scale, globals()))
        liney['height'] = eval(scale, globals())
        try:
            liney['bg'] = offsetcol_entry.get()
            linex['bg'] = offsetcol_entry.get()
        except:
            pass

        root.config(background=bgcol_entry.get())
        default_graphcol = graphcol_entry.get()
        if hide_btn.get():
            submit.destroy()
            clear.destroy()
            delete_graph.destroy()
        bgcol_preview['bg'] = root.cget('bg')
        graphcol_preview['bg'] = default_graphcol
        offsetcol_preview['bg'] = offsetcol_entry.get()
        colors_preview['bg'] = colors_entry.get()
        save_settings()
    except: 
        save_settings()

def settings():
    global settings_root, cust_btn, switch_color, error_graph, one_graph_max, step_entry, offsetx_entry, offsety_entry, index_entry, scale_entry, hide_btn, keys_btn
    settings_root = tk.Toplevel(root)
    settings_root.title(f'KxGraph {__ver__}')
    settings_root.geometry('500x500')
    settings_root.config(background='#1b1b1b')

    tk.Label(settings_root, text='Settings', fg='white', bg='#1b1b1b', font=('Arial',30)).place(x=10,y=10)

    tk.Label(settings_root, text='Step', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=60)
    step_entry = tk.Entry(settings_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    step_entry.insert(0, step)
    step_entry.place(x=10,y=60)
    step_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Label(settings_root, text='Scale', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=90)
    scale_entry = tk.Entry(settings_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    scale_entry.insert(0, scale)
    scale_entry.place(x=10,y=90)
    scale_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Label(settings_root, text='Offset X', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=120)
    offsetx_entry = tk.Entry(settings_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    offsetx_entry.insert(0, str(offset['x']))
    offsetx_entry.place(x=10,y=120)
    offsetx_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Label(settings_root, text='Offset Y', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=260,y=120)
    offsety_entry = tk.Entry(settings_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    offsety_entry.insert(0, str(offset['y']))
    offsety_entry.place(x=200,y=120)
    offsety_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Label(settings_root, text='Index', fg='white', bg='#1b1b1b', font=('Arial',10)).place(x=70,y=150)
    index_entry = tk.Entry(settings_root, width=8, bg='#1b1b1b', fg='white', font=('Arial',10), insertbackground='white')
    index_entry.insert(0, str(index))
    index_entry.place(x=10,y=150)
    index_entry.bind("<KeyRelease>", lambda event: apply())

    tk.Checkbutton(settings_root, text='Different color for every graph', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=switch_color, command=apply).place(x=10,y=180)
    tk.Checkbutton(settings_root, text='Delete graph after error', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=error_graph, command=apply).place(x=10,y=210)
    tk.Checkbutton(settings_root, text='Graph switch', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=one_graph_max, command=apply).place(x=10,y=240)
    tk.Checkbutton(settings_root, text='Hide buttons', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=hide_btn, command=apply).place(x=10,y=270)
    tk.Checkbutton(settings_root, text='Hide dot info on leave', fg='white', bg='#1b1b1b', selectcolor='#1b1b1b', font=('Arial',10), variable=hide_dot_info, command=apply).place(x=10,y=270)

    cust_btn = tk.Button(settings_root, text='Customization', fg='white', bg='#1b1b1b', command=colorsettings)
    cust_btn.place(x=420,y=460)
    keys_btn = tk.Button(settings_root, text='Shortcuts', fg='white', bg='#1b1b1b', command=keys_settings)
    keys_btn.place(x=420,y=460)

    settings_root.bind("<Configure>", lambda event: update_settings())
    settings_root.bind("<Return>", lambda event: apply())
    apply()
    settings_root.mainloop()

def update_widjets(event):
    func.place(x=0,y=root.winfo_height()-20,width=root.winfo_width())
    submit.place(x=root.winfo_width()-69,y=root.winfo_height()-27)
    clear.place(x=root.winfo_width()-108,y=root.winfo_height()-27)
    delete_graph.place(x=root.winfo_width()-186,y=root.winfo_height()-27)

def insert_pattern(function):
    func.delete(0, tk.END)
    func.insert(0, function)


if __name__ == '__main__':
    linex = tk.Canvas(root, height=2000, width=eval(scale, globals()), bg='#2d2d2d', highlightthickness=0)
    linex.place(y=0, x=offset['x']*10)
    liney = tk.Canvas(root, width=2000, height=eval(scale, globals()), bg='#2d2d2d', highlightthickness=0)
    liney.place(x=0, y=offset['y']*10)

    func = tk.Entry(root, bg='#1b1b1b', fg='white', insertbackground='white')
    func.place(x=0,y=780,width=root.winfo_width())

    submit = tk.Button(root, text='New graph', bg='#1b1b1b', fg='white', command=lambda: graph(function=func.get()))
    clear = tk.Button(root, text='Reset', bg='#1b1b1b', fg='white', command=reset)
    delete_graph = tk.Button(root, text='Delete graph', bg='#1b1b1b', fg='white', command=lambda: delete(index))

    submit.place(x=0,y=0)

    dot_info = tk.Label(root, text='', bg='#1b1b1b', fg='white', justify="left")
    dot_info.place(x=5, y=5)

    root.bind("<Configure>", update_widjets)

    root.bind("<Return>", lambda event: graph(function=func.get()))
    root.bind("<F5>", lambda event: graph(function=func.get()))
    root.bind("<Delete>", lambda event: reset())
    root.bind("<Escape>", lambda event: delete(index))
    root.bind("<Control-Escape>", lambda event: delete(-1))
    root.bind("<Shift-Escape>", lambda event: delete(0))
    root.bind("<Control-s>", lambda event: save(audit))
    root.bind("<Control-p>", lambda event: settings())
    root.bind("<Control-g>", lambda event: colortable())
    root.bind("<Tab>", lambda event: settings())

    for i in shortcuts:
        root.bind(f"<{i}>", lambda event, i=i: exec(shortcuts[i], globals()))

    menu = tk.Menu(root)  

    fileMenu = tk.Menu(menu, tearoff=0)
    fileMenu.add_command(label="Reset",command=reset)
    fileMenu.add_command(label="Create graph",command=lambda: graph(function=func.get()))
    fileMenu.add_command(label="Reset settings",command=lambda: load_settings('propsdef.json'))
    fileMenu.add_separator()
    fileMenu.add_command(label="Save",command=lambda: save(audit))
    fileMenu.add_command(label="Load",command=load)
    fileMenu.add_separator()
    fileMenu.add_command(label="Save options",command=apply)
    fileMenu.add_command(label="Save options as",command=save_settings_file)
    fileMenu.add_command(label="Load options",command=load_settings_file)

    fileMenu.add_separator()
    fileMenu.add_command(label="Delete",command=lambda: delete(index))
    fileMenu.add_command(label="Delete first",command=lambda: delete(0))
    fileMenu.add_command(label="Delete last",command=lambda: delete(-1))
    menu.add_cascade(label="File", menu=fileMenu)

    helpMenu = tk.Menu(menu, tearoff=0)
    helpMenu.add_command(label="Documentation",command=lambda: openpage('https://github.com/hexique/KumirX?tab=readme-ov-file#kxgraph'))
    helpMenu.add_command(label="Changelog",command=lambda: openpage('https://github.com/hexique/KumirX/blob/main/changelog.md'))
    helpMenu.add_command(label="Our GitHub",command=lambda: openpage('https://github.com/hexique/KumirX'))
    menu.add_cascade(label="Help", menu=helpMenu)

    rootMenu = tk.Menu(menu, tearoff=0)
    rootMenu.add_command(label="Settings",command=settings)
    rootMenu.add_command(label="Customizaton",command=colorsettings)
    rootMenu.add_command(label="Statistics",command=colortable)
    rootMenu.add_command(label="Audit",command=lambda: show_audit(text=format_dictionary(audit)))
    rootMenu.add_command(label="Raw audit",command=lambda: show_audit(text=str(audit)))
    menu.add_cascade(label="Roots", menu=rootMenu)

    patternsMenuUpscaled = tk.Menu(menu, tearoff=0)
    patternsMenuUpscaled.add_command(label="Sine wave",command=lambda: insert_pattern('sin(x/10)*10'))
    patternsMenuUpscaled.add_command(label="Cosine wave",command=lambda: insert_pattern('cos(x/10)*10'))
    patternsMenuUpscaled.add_command(label="Tangent",command=lambda: insert_pattern('tan(x/10)*10'))
    patternsMenuUpscaled.add_command(label="Exponent",command=lambda: insert_pattern('exp(x/10)*10'))
    patternsMenuUpscaled.add_command(label="Parabol",command=lambda: insert_pattern('x/10**2*10'))
    patternsMenuUpscaled.add_command(label="Multiplicative inverse",command=lambda: insert_pattern('10/x'))
    patternsMenuUpscaled.add_command(label="Square root",command=lambda: insert_pattern('sqrt(x/10)*10'))

    patternsMenu = tk.Menu(menu, tearoff=0)
    patternsMenu.add_command(label="Sine wave",command=lambda: insert_pattern('sin(x)'))
    patternsMenu.add_command(label="Cosine wave",command=lambda: insert_pattern('cos(x)'))
    patternsMenu.add_command(label="Tangent",command=lambda: insert_pattern('tan(x)'))
    patternsMenu.add_command(label="Exponent",command=lambda: insert_pattern('exp(x)'))
    patternsMenu.add_command(label="Parabol",command=lambda: insert_pattern('x**2'))
    patternsMenu.add_command(label="Multiplicative inverse",command=lambda: insert_pattern('1/x'))
    patternsMenu.add_command(label="Square root",command=lambda: insert_pattern('sqrt(x)'))
    patternsMenu.add_separator()
    patternsMenu.add_cascade(label="Upscaled",menu=patternsMenuUpscaled)

    menu.add_cascade(label="Patterns", menu=patternsMenu)

    root.config(menu=menu)
    load_settings('props.json')
    settings()
    apply()

    root.mainloop()
