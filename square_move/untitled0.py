from tkinter import *
from tkinter.ttk import *

tk = Tk() 
tk.title('Модели танков')
tk.geometry('750x750+25+25')
tk.configure(bg = '#ffffff')
canvas = Canvas(tk, width = 750, height = 750, bg = '#ff0000')
canvas.pack()
id = canvas.create_rectangle(50, 50, 700, 700, fill = '#000000')
id2 = canvas.create_rectangle(48, 48, 698, 698, fill = '#ffffff')





def to(event):
    global id
    global id2
    pos = canvas.coords(id)
    pos1 = canvas.coords(id2)
    if pos[1] == 0:
        id = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0], pos1[1], pos1[2], pos1[3], fill = '#ffffff')
    elif pos[0] == 0: 
        id = canvas.create_rectangle(pos[0], pos[1]-2, pos[2]+2, pos[3]+2, fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0], pos1[1]-2, pos1[2]+2, pos1[3]+2, fill = '#ffffff')
    elif pos[2] == 750:
        id = canvas.create_rectangle(pos[0]-2, pos[1]-2, pos[2], pos[3]+2, fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0]-2, pos1[1]-2, pos1[2], pos1[3]+2, fill = '#ffffff')
    else:
        id = canvas.create_rectangle(pos[0]-2, pos[1]-2, pos[2]+2, pos[3]+2, fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0]-2, pos1[1]-2, pos1[2]+2, pos1[3]+2, fill = '#ffffff')
    
def out(event):
    global id
    global id2
    pos = canvas.coords(id)
    pos1 = canvas.coords(id2)
    canvas.create_rectangle(0, 0, 750, 750, fill = '#ff0000')
    id = canvas.create_rectangle(pos[0]+2, pos[1]+2, pos[2]-2, pos[3]-2, fill = '#000000')
    id2 = canvas.create_rectangle(pos1[0]+2, pos1[1]+2, pos1[2]-2, pos1[3]-2, fill = '#ffffff')

def left(event):
    global id
    global id2
    pos = canvas.coords(id)
    pos1 = canvas.coords(id2)
    canvas.create_rectangle(0, 0, 750, 750, fill = '#ff0000')
    if pos[2] == 750:
        id = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0], pos1[1], pos1[2], pos1[3], fill = '#ffffff')
    else:
        id = canvas.create_rectangle(pos[0]+2, pos[1], pos[2]+2, pos[3], fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0]+2, pos1[1], pos1[2]+2, pos1[3], fill = '#ffffff')

def right(event):
    global id
    global id2
    pos = canvas.coords(id)
    pos1 = canvas.coords(id2)
    canvas.create_rectangle(0, 0, 750, 750, fill = '#ff0000')
    if pos[0] == 0:
        id = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0], pos1[1], pos1[2], pos1[3], fill = '#ffffff')
    else:
        id = canvas.create_rectangle(pos[0]-2, pos[1], pos[2]-2, pos[3], fill = '#000000')
        id2 = canvas.create_rectangle(pos1[0]-2, pos1[1], pos1[2]-2, pos1[3], fill = '#ffffff')

if __name__ == "__main__":
    tk.bind("<KeyPress-Up>", lambda e: to(e))
    tk.bind("<KeyPress-Down>", lambda e: out(e))
    tk.bind("<KeyPress-Left>", lambda e: left(e))
    tk.bind("<KeyPress-Right>", lambda e: right(e))
    tk.mainloop()