from tkinter import *
from tkinter.ttk import *

tk = Tk() 
tk.title('3d')
tk.geometry('750x750+25+25')
tk.configure(bg = '#ffffff')
canvas = Canvas(tk, width = 750, height = 750, bg = '#ff0000')
canvas.pack()
id = canvas.create_rectangle(50, 50, 700, 700, fill = '#000000')
id_1 = canvas.create_rectangle(52, 52, 698, 698, fill = '#ffffff')
id2 = canvas.create_polygon(0, 0, 50, 50, 700, 50, 750, 0, fill = '#000000')
id2_1 = canvas.create_polygon(2, 0, 52, 50, 698, 50, 748, 0, fill = '#ffffff')
id3 = canvas.create_polygon(750, 0, 700, 50, 700, 700, 750, 750, fill = '#000000')
id3_1 = canvas.create_polygon(750, 2, 700, 52, 700, 698, 750, 748, fill = '#ffffff')
id4 = canvas.create_polygon(750, 750, 700, 700, 50, 700, 0, 750, fill = '#000000')
id4_1 = canvas.create_polygon(748, 750, 698, 700, 52, 700, 2, 750, fill = '#ffffff')
id5 = canvas.create_polygon(0, 750, 50, 700, 50, 50, 0, 0, fill = '#000000')
id5_1 = canvas.create_polygon(0, 748, 50, 698, 50, 52, 0, 2, fill = '#ffffff')
obj = canvas.create_rectangle(374, 374, 376, 376, fil = '#ff0000')


def to(event):
    global id
    global id_1
    global id2
    global id2_1
    global id3
    global id3_1
    global id4
    global id4_1
    global id5
    global id5_1
    global obj
    pos = canvas.coords(id)
    pos1 = canvas.coords(id_1)
    pos2 = canvas.coords(obj)
    if pos[1] == 0:
        id = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0], pos1[1], pos1[2], pos1[3], fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0], pos2[1], pos2[2], pos2[3], fill = '#ff0000')
    elif pos[0] == 0: 
        id = canvas.create_rectangle(pos[0], pos[1]-2, pos[2]+2, pos[3]+2, fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0], pos1[1]-2, pos1[2]+2, pos1[3]+2, fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0], pos2[1]-1, pos2[2]+1, pos2[3]+1, fill = '#ff0000')
    elif pos[2] == 750:
        id = canvas.create_rectangle(pos[0]-2, pos[1]-2, pos[2], pos[3]+2, fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0]-2, pos1[1]-2, pos1[2], pos1[3]+2, fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0]-1, pos2[1]-1, pos2[2], pos2[3]+1, fill = '#ff0000')
    else:
        id = canvas.create_rectangle(pos[0]-2, pos[1]-2, pos[2]+2, pos[3]+2, fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0]-2, pos1[1]-2, pos1[2]+2, pos1[3]+2, fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+4, pos1[0], pos1[3]+4, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        
        obj = canvas.create_rectangle(pos2[0]-1, pos2[1]-1, pos2[2]+1, pos2[3]+1, fill = '#ff0000')
       
        
        
def out(event):
    global id
    global id_1
    global id2
    global id2_1
    global id3
    global id3_1
    global id4
    global id4_1
    global id5
    global id5_1
    global obj
    pos = canvas.coords(id)
    pos1 = canvas.coords(id_1)
    pos2 = canvas.coords(obj)
    canvas.create_rectangle(0, 0, 750, 750, fill = '#ff0000')
    id = canvas.create_rectangle(pos[0]+2, pos[1]+2, pos[2]-2, pos[3]-2, fill = '#000000')
    id_1 = canvas.create_rectangle(pos1[0]+2, pos1[1]+2, pos1[2]-2, pos1[3]-2, fill = '#ffffff')
    id2 = canvas.create_polygon(0, 0, pos[0], pos[1]+2, pos[2], pos[1]+2, 750, 0, fill = '#000000')
    id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
    id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
    id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
    id4 = canvas.create_polygon(750, 750, pos[2], pos[3]-2, pos[0], pos[3]-2, 0, 750, fill = '#000000')
    id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
    id5 = canvas.create_polygon(0, 750, pos[0]+2, pos[3], pos[0]+2, pos[1], 0, 0, fill = '#000000')
    id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
    if pos2[2]-pos2[0] == 2:
        obj = canvas.create_rectangle(pos2[0], pos2[1], pos2[2], pos2[3], fill = '#ff0000')
    else:
        obj = canvas.create_rectangle(pos2[0]+1, pos2[1]+1, pos2[2]-1, pos2[3]-1, fill = '#ff0000')


def left(event):
    global id
    global id_1
    global id2
    global id2_1
    global id3
    global id3_1
    global id4
    global id4_1
    global id5
    global id5_1
    global obj
    pos = canvas.coords(id)
    pos1 = canvas.coords(id_1)
    pos2 = canvas.coords(obj)
    canvas.create_rectangle(0, 0, 750, 750, fill = '#ff0000')
    if pos[2] == 750:
        id = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0], pos1[1], pos1[2], pos1[3], fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0], pos2[1], pos2[2], pos2[3], fill = '#ff0000')
    else:
        id = canvas.create_rectangle(pos[0]+2, pos[1], pos[2]+2, pos[3], fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0]+2, pos1[1], pos1[2]+2, pos1[3], fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0], pos1[3], pos1[0], pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0]+2, pos2[1], pos2[2]+2, pos2[3], fill = '#ff0000')

def right(event):
    global id
    global id_1
    global id2
    global id2_1
    global id3
    global id3_1
    global id4
    global id4_1
    global id5
    global id5_1
    global obj
    pos = canvas.coords(id)
    pos1 = canvas.coords(id_1)
    pos2 = canvas.coords(obj)
    canvas.create_rectangle(0, 0, 750, 750, fill = '#ff0000')
    if pos[0] == 0:
        id = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0], pos1[1], pos1[2], pos1[3], fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0], pos2[1], pos2[2], pos2[3], fill = '#ff0000')
    else:
        id = canvas.create_rectangle(pos[0]-2, pos[1], pos[2]-2, pos[3], fill = '#000000')
        id_1 = canvas.create_rectangle(pos1[0]-2, pos1[1], pos1[2]-2, pos1[3], fill = '#ffffff')
        id2 = canvas.create_polygon(0, 0, pos[0]-2, pos[1], pos[2]-2, pos[1], 750, 0, fill = '#000000')
        id2_1 = canvas.create_polygon(2, 0, pos1[0], pos1[1] - 2, pos1[2], pos1[1]-2, 748, 0, fill = '#ffffff')
        id3 = canvas.create_polygon(750, 0, pos[2]-2, pos[1], pos[2]-2, pos[3], 750, 750, fill = '#000000')
        id3_1 = canvas.create_polygon(750, 2, pos1[2]+2, pos1[1], pos1[2]+2, pos1[3], 750, 748, fill = '#ffffff')
        id4 = canvas.create_polygon(750, 750, pos[2]-2, pos[3], pos[0]-2, pos[3], 0, 750, fill = '#000000')
        id4_1 = canvas.create_polygon(748, 750, pos1[2], pos1[3]+2, pos1[0], pos1[3]+2, 2, 750, fill = '#ffffff')
        id5 = canvas.create_polygon(0, 750, pos[0]-2, pos[3], pos[0]-2, pos[1], 0, 0, fill = '#000000')
        id5_1 = canvas.create_polygon(0, 748, pos1[0]-2, pos1[3], pos1[0]-2, pos1[1], 0, 2, fill = '#ffffff')
        obj = canvas.create_rectangle(pos2[0]-2, pos2[1], pos2[2]-2, pos2[3], fill = '#ff0000')

if __name__ == "__main__":
    tk.bind("<KeyPress-Up>", lambda e: to(e))
    tk.bind("<KeyPress-Down>", lambda e: out(e))
    tk.bind("<KeyPress-Left>", lambda e: left(e))
    tk.bind("<KeyPress-Right>", lambda e: right(e))
    tk.mainloop()