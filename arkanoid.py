def destroy_brick():
    global movement
    coord_ball = canvas.coords(kruzok)
    items_list = canvas.find_overlapping(coord_ball[0],coord_ball[1],coord_ball[2],coord_ball[3])
    for i in items_list:
        if i in bricks:
            bricks.remove(i)
            canvas.delete(i)
            movement = [movement[0]*(-1), movement[1]*(-1)]


def ball_move():
    global movement
    canvas.move(kruzok,movement[0],movement[1])
    if canvas.coords(kruzok)[0] < 0:
        movement[0] *= (-1)
    if canvas.coords(kruzok)[1] < 0:
        movement[1] *= (-1)
    if canvas.coords(kruzok)[2] > w:
        movement[0] *= (-1)
    if canvas.coords(kruzok)[3] > h:
        movement[1] *= (-1)
    destroy_brick()
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

def checkkey(e):
    print("stlacil som")
    print(e.char)

def prepare_bricks():
    for y in range(brick_count_y):
        for x in range(w//brick_w):
            bricks.append(canvas.create_rectangle(x*brick_w,y*brick_h,x*brick_w+brick_w, y*brick_h+brick_h, fill = colours[y%brick_count_y],  width=5, outline="black"))

colours = ["white", "purple", "yellow", "turquoise", "blue", "orange"]

import tkinter as tk
import random
win = tk.Tk()

#width, height
w = 650
h = 450

canvas = tk.Canvas(width = w, height = h, bg = "black")
canvas.pack()

d=15
movement = [1*d,1*d]

brick_w = 65
brick_h = 20
brick_count_x = 10
brick_count_y = len(colours)
bricks = []

kruzok = canvas.create_oval(w/2-20,h/2-20,w/2,h/2, fill="white")


desk = canvas.create_rectangle(w/2-50, h-20, w/2+50, h, fill="purple")

prepare_bricks()

canvas.bind("<Button-1>", starter)
canvas.bind("<B1-Motion>", mover)
# canvas.focus_set()
# canvas.bind("<Key>", checkkey)
#win.bind("<Key>", checkkey)

win.mainloop()
#dorobit hru aby bola prekvapujuca
