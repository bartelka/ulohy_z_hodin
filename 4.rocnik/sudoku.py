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
    print(sudoku)
sudoku_solver()