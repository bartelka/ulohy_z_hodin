import tkinter as tk
import random
win = tk.Tk()

#width, height
w = 650
h = 450

#cell_list = []

canvas = tk.Canvas(width = w, height = h, bg = "white")
canvas.pack()

d=15
movement = [1*d,1*d]

farby = ["red", "purple", "orange","yellow","blue","green","black","magenta","turquoise"]
kruzok = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill=random.choice(farby))


desk = canvas.create_rectangle(w/2-50, h-20, w/2+50, h, fill="black")


def ball_move():
    global movement
    canvas.move(kruzok,movement[0],movement[1])
    canvas.itemconfig(kruzok, fill=random.choice(farby))
    if canvas.coords(kruzok)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(kruzok)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(kruzok)[2] > w:
        movement[0] *= (-1)
    if canvas.coords(kruzok)[3] > h:
        movement[1] *= (-1)
    canvas.after(50,ball_move)

def starter(e):
    global x
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if desk in zoz:
        x = e.x
        ball_move()

def mover(e):
    global x
    if x != 0:
        mouse = e.x - x
        canvas.move(desk, mouse, 0)
        x = e.x

canvas.bind("<Button-1>", starter)
canvas.bind("<B1-Motion>", mover)
win.mainloop()
