move = [0, -1] #vektor pohybu

w=500
h=500
status = True
head = [w//2,h//2]
speed = 100

whole_snake = []

def draw_snake():
    global head, status
    canvas.create_rectangle(head[0],head[1],head[0]+1,head[1]+1,fill="black")
    whole_snake.append(tuple(head))
    if whole_snake.count(tuple(head))>1:
        canvas.delete("all")
        canvas.create_text(w/2,h/2,text="Prehral si", font="arial50",fill="black")
        return
    head[0] += move[0]
    head[1] += move[1]
    canvas.after(100,draw_snake)

def changer(e):
    global move
    if e.char == "w":
        move = [0, -1]
    elif e.char == "a":
        move = [-1, 0]
    elif e.char == "d":
        move = [1, 0]
    elif e.char == "s":
        move = [0, 1]

import tkinter as tk

win = tk.Tk()

canvas = tk.Canvas(width=w,height=h,bg="white")
canvas.pack()

draw_snake()

win.bind("<KeyPress>",changer)

win.mainloop()
