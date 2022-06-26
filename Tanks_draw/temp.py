from tkinter import *
from tkinter.ttk import *

tk = Tk() 
tk.title('Модели танков')
tk.geometry('1350x750+25+25')
tk.configure(bg = '#ffffff')
canvas = Canvas(tk, width = 1350, height = 750)
canvas.pack(expand = 1, anchor = W)
id = canvas.create_rectangle(10, 10, 20, 20, fill = '#000000')
b=0
def white(event):
    global b
    b = 0
def green(event):
    global b
    b = 1
def grey(event):
    global b
    b = 2
def red(event):
    global b
    b = 3
    

def up(event):
    pos = canvas.coords(id)
    if b == 0:
        H = '#ffffff'
    elif b == 1:
        H = '#007f00'
    elif b == 2:
        H = '#7f7f7f'
    elif b == 3:
        H = '#ff0000'
    if (pos[1]) == 0:
        canvas.move(id, 0, 0)
    else:
        canvas.move(id, 0, -10)
        canvas.create_rectangle(pos[0], pos[1]-10, pos[2], pos[3]-10, fill = '#000000')
        canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = H)
def down(event):
    pos = canvas.coords(id)
    if b == 0:
        H = '#ffffff'
    elif b == 1:
        H = '#007f00'
    elif b == 2:
        H = '#7f7f7f'
    elif b == 3:
        H = '#ff0000'
    if pos[3] == 750:
        canvas.move(id, 0, 0)
    else:
        canvas.move(id, 0, 10)
        canvas.create_rectangle(pos[0], pos[1]+10, pos[2], pos[3]+10, fill = '#000000')
        canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = H)
def left(event):
    pos = canvas.coords(id)
    if b == 0:
        H = '#ffffff'
    elif b == 1:
        H = '#007f00'
    elif b == 2:
        H = '#7f7f7f'
    elif b == 3:
        H = '#ff0000'
    if pos[0] == 0:
        canvas.move(id, 0, 0)
    else:
        canvas.move(id, -10, 0)
        canvas.create_rectangle(pos[0]-10, pos[1], pos[2]-10, pos[3], fill = '#000000')
        canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = H)
def right(event):
    pos = canvas.coords(id)
    if b == 0:
        H = '#ffffff'
    elif b == 1:
        H = '#007f00'
    elif b == 2:
        H = '#7f7f7f'
    elif b == 3:
        H = '#ff0000'
    if pos[2] == 1350:
        canvas.move(id, 0, 0)
    else:
        canvas.move(id, 10, 0)
        canvas.create_rectangle(pos[0]+10, pos[1], pos[2]+10, pos[3], fill = '#000000')
        canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = H)


if __name__ == "__main__":
    tk.bind("<KeyPress-Up>", lambda e: up(e))
    tk.bind("<KeyPress-Left>", lambda e: left(e)) 
    tk.bind("<KeyPress-Right>", lambda e: right(e))
    tk.bind("<KeyPress-Down>", lambda e: down(e))
    tk.bind("q", lambda e: white(e))
    tk.bind("w", lambda e: green(e))
    tk.bind("e", lambda e: grey(e))
    tk.bind("r", lambda e: red(e)) 
    tk.mainloop()