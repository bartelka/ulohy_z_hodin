import random
import tkinter as tk

count_w = random.randrange(4,7)
count_h = random.randrange(3,10)
pw = 50
ph = 50
w = 300
h = 450

win = tk.Tk()

canvas = tk.Canvas(win,width=w,height=h,bg="grey")
canvas.pack()

img = tk.PhotoImage(file="images/ostrov3.png") #biela
img1 = tk.PhotoImage(file="images/ostrov0.png") #hneda
img2 = tk.PhotoImage(file="images/ostrov1.png") #vodorovny ostrov
img3 = tk.PhotoImage(file="images/ostrov2.png") #zvisly pstrov

water = []
islands = []

def changer(e):
    global water
    click = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if (len(click) != 0 and click[0] in water): # len(click) != 0 -> ci som klikol na obrazok
        nx = e.x // pw *pw
        ny = e.y // ph * ph
        canvas.delete(click[0])
        water.remove(click[0])
        canvas.create_image(nx, ny, image=img2, anchor=tk.NW,tag="bridge")

def spinner(e):
    click = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y +1)
    image = canvas.itemcget(click[0],"image")
    print(image)
    if image == "pyimage3":
        canvas.itemconfig(click[0],image=img3)
    if image == "pyimage4":
        canvas.itemconfig(click[0], image=img2)

def set_up():
    global water, islands
    for y in range(count_h):
        for x in range(count_w):
            result = random.random()
            print(result)
            if result >= 0.2:
                water.append(canvas.create_image(pw * x, ph * y, image=img, anchor=tk.NW))
            else:
                islands.append(canvas.create_image(pw * x, ph * y, image=img1, anchor=tk.NW))

set_up()

canvas.bind("<Button-1>",changer)
canvas.tag_bind("bridge","<Button-1>",spinner)

win.mainloop()
