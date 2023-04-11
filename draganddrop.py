import tkinter as tk
win = tk.Tk()

h, w = 500, 500

def clicker(e):
    #ak som klikol na objekt, zaamata si suradnice
    global x, y
    zoz = canvas.find_overlapping(e.x, e.y, e.x+1, e.y+1)
    if ob1 in zoz:
        x = e.x
        y = e.y

def mover(e):
    global x, y
    if x != 0 and y != 0:
        dx = e.x - x
        dy = e.y - y
        canvas.move(ob1, dx, dy)
        x = e.x
        y = e.y

def releaser(e):
    global x, y
    x, y = 0, 0

canvas = tk.Canvas(win, height=h , width=w, bg="white")
canvas.pack()

ob1 = canvas.create_polygon(10,20,40,40,150,200, fill="magenta")

canvas.bind("<Button-1>", clicker)
canvas.bind("<B1-Motion>", mover)
canvas.bind("<ButtonRelease>", releaser)

win.mainloop()
