from tkinter import *
from tkinter.ttk import * 
import random

tk = Tk() 
tk.title('Тетрис')
tk.geometry('550x650+50+50')
tk.configure(bg = '#000000')
tk.resizable(0, 0)
canvas1 = Canvas(tk, width = 330, height = 600, bg = '#ffffff')
canvas1.pack(expand = 1, anchor = W)
canvas2 = Canvas(tk, width = 150, height = 150, bg = '#ffffff')
canvas2.place(x = 365, y = 25)
canvas3 = Canvas(tk, width = 150, height = 100, bg = '#000000')
canvas3.place(x = 365, y = 200)
canvas4 = Canvas(tk)
canvas4.place(x = 365, y = 350)
for l in range(0, 330, 30):
    canvas1.create_line(l, 0, l, 600, fill = "#000000")
for p in range(0, 600, 30):
    canvas1.create_line(0, p, 330, p, fill = "#000000")
for g in range(0, 150, 30):
    canvas2.create_line(g, 0, g, 150, fill = '#000000')
for j in range(0, 150, 30):
    canvas2.create_line(0, j, 150, j, fill = '#000000')
canvas3.create_text(75, 25, text='SCORE:', font=('Courier', 15), fill='red')
ms = Message(canvas4)
ms.configure(text = """Увага!!! Для цієї гри необхідно, аби ви весь час натискали на стрілки. Для запуску гри натисніть будь-яку з означених клавіш""")
ms.pack()

class new_figure:
    W = ('#c46210', '#648c11', '#e97451', '#af002a', '#008000', '#5f9ebb', '#867e36', '#5d8aa8', '#ef9999', '#d755b1', '#8a2be2', '#556b2f', '#df00ff')
    S = random.choice(W)
    block = canvas2.create_rectangle(60, 0, 90, 30, fill = S)
    def newcolor():
        T = random.choice(new_figure.W)
        return T
    def newblock():
        new_figure.block = canvas2.create_rectangle(60, 0, 90, 30, fill = new_figure.newcolor())

class old_figure:
    Q = ('#c46210', '#648c11', '#e97451', '#af002a', '#008000', '#5f9ebb', '#867e36', '#5d8aa8', '#ef9999', '#d755b1', '#8a2be2', '#556b2f', '#df00ff')
    H = random.choice(Q)
    block = canvas1.create_rectangle(150, 0, 180, 30, fill = H, tags = 'game')
    for el in range(0, 600, 30):
        line = canvas1.create_rectangle(0, el, 330, el + 30)
    t20 = []
    b1 = []
    b11 = []
    score = 0
    score1 = canvas3.create_text(75, 75, text = score, font = ('Courier', 15), fill = 'red')

    def __init__(self, canvas1):  
        self.canvas1 = canvas1
        self.x = 0
        self.y = 0
        self.id = old_figure.block 
        self.canvas1_width = self.canvas1.winfo_width()
        self.canvas1_height = self.canvas1.winfo_height()
        self.canvas1.pack()
        self.movement()
        
    def movement(self):
        self.canvas1.move(self.id, self.x, self.y + 30) 
        self.canvas1.after(1000, self.movement)
        pos = self.canvas1.coords(self.id)
        pos1 = canvas2.coords(new_figure.block)
        for hp in range(0, 330, 30):
            if [hp, 30, hp + 30, 60] in old_figure.b1:
                self.x = 0
                self.y = 0
                self.canvas1.create_text(150, 225, text='Game over', font=('Courier', 15), fill='#000000')
                self.canvas1.create_text(150, 275, text=f'Your score is {old_figure.score}', font=('Courier', 15), fill='#000000')
                self.canvas1.after(1000, tk.destroy)
        if pos[3] == 600:
            old_figure.b1.append(pos)
            old_figure.t20.append(pos[2] - pos[0])
            if sum(old_figure.t20) == 330:
                for i in range(11):
                    self.canvas1.create_rectangle(i * 30, 570, i * 30 + 30, 600, fill = '#ffffff')
                    for i in old_figure.b1:
                        if i[1] == 570:
                            old_figure.b1.remove([i[0], i[1], i[2], i[3]])
                del old_figure.t20[::]
                for g in old_figure.b1:
                    old_figure.b11.append([g[0], g[1] + 30, g[2], g[3] + 30])
                for g1 in old_figure.b1:                   
                    self.canvas1.create_rectangle(g1[0], g1[1], g1[2], g1[3], fill = '#ffffff')
                del old_figure.b1[::]
                for g2 in old_figure.b11:
                    self.canvas1.create_rectangle(g2[0], g2[1], g2[2], g2[3], fill = new_figure.newcolor())
                    old_figure.b1.append([g2[0], g2[1], g2[2], g2[3]])
                    if g2[3] == 600:
                        cout = old_figure.b1.count([g2[0], g2[1], g2[2], g2[3]])
                        old_figure.t20.append(cout * 30)
                del old_figure.b11[::]
                old_figure.score += 1
                canvas3.delete(old_figure.score1)
                old_figure.score1 = canvas3.create_text(75, 75, text = old_figure.score, font = ('Courier', 15), fill = 'red')
            self.x = 0
            self.y = 0
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        elif [pos[0], pos[1] + 30, pos[2], pos[3] + 30] in old_figure.b1:
            old_figure.b1.append(pos)
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 0)
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        
    def left(self, event):
        pos = self.canvas1.coords(self.id)
        pos1 = canvas2.coords(new_figure.block)
        if min(pos[::2]) == 0 or max(pos[1::2]) == 600:
            self.x = 0
            self.y = 0
        elif ([pos[0] - 30, pos[1], pos[2] - 30, pos[3]] in old_figure.b1) and ([pos[0], pos[1] + 30, pos[2], pos[3] + 30] in old_figure.b1):
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 0)
            old_figure.b1.append([pos[0], pos[1], pos[2], pos[3]])
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        elif [pos[0] - 30, pos[1], pos[2] - 30, pos[3]]  in old_figure.b1:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 30)
        elif [pos[0] - 30, pos[1] + 30, pos[2] - 30, pos[3] + 30] in old_figure.b1:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, -30, 0)
            old_figure.b1.append([pos[0] - 30, pos[1], pos[2] - 30, pos[3]])
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        else:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, -30, 30)
            
    def right(self, event):
        pos = self.canvas1.coords(self.id)
        pos1 = canvas2.coords(new_figure.block)
        if max(pos[::2]) == 330 or max(pos[1::2]) == 600:
            self.x = 0
            self.y = 0
        elif ([pos[0] + 30, pos[1], pos[2] + 30, pos[3]] in old_figure.b1) and ([pos[0], pos[1] + 30, pos[2], pos[3] + 30] in old_figure.b1):
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 0)
            old_figure.b1.append(pos)
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        elif [pos[0] + 30, pos[1], pos[2] + 30, pos[3]] in old_figure.b1:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 30)
        elif [pos[0] + 30, pos[1] + 30, pos[2] + 30, pos[3] + 30] in old_figure.b1:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 30, 0)
            old_figure.b1.append([pos[0] + 30, pos[1], pos[2] + 30, pos[3]])
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        else:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 30, 30)
            
    def down(self, event):
        pos = self.canvas1.coords(self.id)
        pos1 = canvas2.coords(new_figure.block)
        for hp in range(0, 330, 30):
            if [hp, 30, hp + 30, 60] in old_figure.b1:
                self.x = 0
                self.y = 0
                self.canvas1.create_text(150, 225, text='Game over', font=('Courier', 15), fill='#000000')
                self.canvas1.create_text(150, 275, text=f'Your score is {old_figure.score}', font=('Courier', 15), fill='#000000')
                self.canvas1.after(1000, tk.destroy)
        if pos[3] == 600:
            old_figure.b1.append(pos)
            old_figure.t20.append(pos[2] - pos[0])
            if sum(old_figure.t20) == 330:
                for i in range(11):
                    self.canvas1.create_rectangle(i * 30, 570, i * 30 + 30, 600, fill = '#ffffff')
                    for i in old_figure.b1:
                        if i[1] == 570:
                            old_figure.b1.remove([i[0], i[1], i[2], i[3]])
                del old_figure.t20[::]
                for g in old_figure.b1:
                    old_figure.b11.append([g[0], g[1] + 30, g[2], g[3] + 30])
                for g1 in old_figure.b1:                   
                    self.canvas1.create_rectangle(g1[0], g1[1], g1[2], g1[3], fill = '#ffffff')
                del old_figure.b1[::]
                for g2 in old_figure.b11:
                    self.canvas1.create_rectangle(g2[0], g2[1], g2[2], g2[3], fill = new_figure.newcolor())
                    old_figure.b1.append([g2[0], g2[1], g2[2], g2[3]])
                    if g2[3] == 600:
                        cout = old_figure.b1.count([g2[0], g2[1], g2[2], g2[3]])
                        old_figure.t20.append(cout * 30)
                del old_figure.b11[::]
                old_figure.score += 1
                canvas3.delete(old_figure.score1)
                old_figure.score1 = canvas3.create_text(75, 75, text = old_figure.score, font = ('Courier', 15), fill = 'red')
            self.x = 0
            self.y = 0
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()
        elif [pos[0], pos[1] + 30, pos[2], pos[3] + 30] in old_figure.b1:
            old_figure.b1.append(pos)
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 0)
            self.id = self.canvas1.create_rectangle(int(pos1[0]) + 90, int(pos1[1]), int(pos1[2]) + 90, int(pos1[3]), fill = new_figure.newcolor())
            new_figure.newblock()

        else:
            self.x = 0
            self.y = 0
            self.canvas1.move(self.id, 0, 30)

if __name__ == "__main__":
    r = old_figure(canvas1) 
    tk.bind("<KeyPress-Left>", lambda e: r.left(e)) 
    tk.bind("<KeyPress-Right>", lambda e: r.right(e))
    tk.bind("<KeyPress-Down>", lambda e: r.down(e)) 
    tk.mainloop()