fr = open("sudoku.txt","r",encoding="utf-8")

sudoku = []

def input_parser(fr,sudoku):
    for riadok in fr:
        pole = []
        for cislo in riadok.strip():
            pole.append(int(cislo))
        sudoku.append(pole)
    return sudoku

input_parser(fr,sudoku)

print(sudoku)

def check(x:int,y:int,n:int) -> bool:
    for j in range(9):
        if sudoku[j][x] == n or sudoku[y][j] == n:
            return False
        #dva malicke cykliky o dlzke 3, skontroluj prislusny stvorec
        y1 = y//3*3
        x1 = x//3*3
        for i in range(y1,y1+3):
            for z in range(x1,x1+3):
                if sudoku[i][z] == n:
                    return False
    return True

def sudoku_solver():
    global sudoku
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1,10):
                    if check(x,y,n):
                        sudoku[y][x] = n
                        sudoku_solver()
                        sudoku[y][x] = 0
                return
    draw_sudoku()

def draw_sudoku():
    a = 50
    for i in range(10):
        if i == 3 or i == 6 or i == 0 or i == 9:
            width = 5
        else:
            width = 2
        canvas.create_line(i * a, 0, i * a, h, fill="black", width=width)
        canvas.create_line(0 , i * a, w, i*a, fill="black", width=width)
    for y in range(9):
        for x in range(9):
            canvas.create_text(x*50+25,y*50+25,text=sudoku[y][x],font = ("arial",40), anchor = tk.CENTER)


import tkinter as tk

w = 450
h = 450

win = tk.Tk()
canvas = tk.Canvas(win,height=h,width=w,bg="white")
canvas.pack()
sudoku_solver()

win.mainloop()
