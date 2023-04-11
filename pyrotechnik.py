#zapamatam si id vybusneho kabla alebo to dam do tag
import random
import tkinter as tk

win = tk.Tk()
colors = ["magenta", "turquoise", "yellow", "orange", "red"]

#ux a uy == lave horne rohy
ux = 70
uy = 100

width = 300
height = 10

wires = []
explosion = 0

def DrawWires():
    global wires, explosion
    for i in range(5):
        wires.append(canvas.create_rectangle(ux, uy + height*i, ux+width, uy+height*(i+1), fill=colors[i]))
    explosion = random.choice(wires)

def clicker(e):
    #zistim ci som klikla na habel ak ano zistim ci id objektu je rovnake s explosion ak ano vypisem vyhral si


h, w = 200, 500
canvas = tk.Canvas(win, height=h, width=w, bg="white")
canvas.pack()

DrawWires()

canvas.bind("<Button-1>", clicker)

win.mainloop()
