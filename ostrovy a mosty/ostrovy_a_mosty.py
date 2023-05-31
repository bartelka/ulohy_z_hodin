import random 
import tkinter as tk

count_w = random.randrange(4,7)
count_h = random.randrange(3,10)
pw = 50
ph = 50
w = 400
h = 550

win = tk.Tk()

canvas = tk.Canvas(win,width=w,height=h,bg="grey")
canvas.pack()
img = tk.PhotoImage(file="images/ostrov3.png")
img1 = tk.PhotoImage(file="images/ostrov0.png")
for y in range(count_h):
    for x in range(count_w):
        result = random.random()
        print(result)
        if result >= 0.2:
            canvas.create_image(pw * x, ph * y, image=img, anchor=tk.NW)
        else:
            canvas.create_image(pw * x, ph * y, image=img1, anchor=tk.NW)

win.mainloop()