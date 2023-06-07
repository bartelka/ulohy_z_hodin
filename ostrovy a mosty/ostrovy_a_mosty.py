import random
import tkinter as tk

count_w = random.randrange(4,7)
count_h = random.randrange(3,10)
pw = 50
ph = 50
w = 300
h = 450

text = ""
coins = 0
field_status = True

win = tk.Tk()

canvas = tk.Canvas(win,width=count_w*pw+100,height=count_h*ph,bg="grey")
canvas.pack()

img = tk.PhotoImage(file="images/ostrov3.png") #biela
img1 = tk.PhotoImage(file="images/ostrov0.png") #hneda
img2 = tk.PhotoImage(file="images/ostrov1.png") #vodorovny ostrov
img3 = tk.PhotoImage(file="images/ostrov2.png") #zvisly pstrov
img4 = tk.PhotoImage(file="images/ostrov_kruh0.png") #modry kruh
img5 = tk.PhotoImage(file="images/ostrov_kruh1.png") #hnedy kruh

water = []
islands = []

def changer(e):
    global water, coins, text
    click = canvas.find_overlapping(e.x,e.y,e.x+1,e.y+1)
    if (len(click) != 0 and click[0] in water): # len(click) != 0 -> ci som klikol na obrazok
        nx = e.x // pw *pw
        ny = e.y // ph * ph
        canvas.delete(click[0])
        water.remove(click[0])
        if field_status == True:
            canvas.create_image(nx, ny, image=img2, anchor=tk.NW,tag="bridge")
            coins += 10
        if field_status == False:
            canvas.create_image(nx, ny, image=img1, anchor=tk.NW)
            coins += 50
    canvas.itemconfig(text, text=str(coins))

def spinner(e):
    click = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y +1)
    image = canvas.itemcget(click[0],"image")
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
    canvas.create_image(count_w*pw+50,0,image=img4, anchor=tk.NW, tag="switcher")


def switcher(e):
    global field_status
    click = canvas.find_overlapping(e.x, e.y, e.x + 1, e.y + 1)
    image = canvas.itemcget(click[0], "image")
    print(image,field_status)
    if image == "pyimage5":
        canvas.itemconfig(click[0], image=img5)
        field_status = False
    if image == "pyimage6":
        canvas.itemconfig(click[0], image=img4)
        field_status = True

set_up()
text = canvas.create_text(count_w * pw + 25, 25, text=str(coins), font="arial100")

canvas.bind("<Button-1>",changer)
canvas.tag_bind("bridge","<Button-1>",spinner)
canvas.tag_bind("switcher","<Button-1>",switcher)
win.mainloop()
