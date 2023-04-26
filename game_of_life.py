fr = open("gol.txt", "r", encoding="utf-8")

def create2Dmatrix(width, height):
    matrix = []
    for y in range(height):
        temp = []
        for x in range(width):
            temp.append(0)
        matrix.append(temp)
    return matrix

def processfile(matrix):
    x, y = 0, 0
    for row in fr:
        x = 0
        for char in row:
            if char == "1":
                matrix[y][x]=1
            x += 1
        y += 1

def return_friends(x,y,matrix):
    count = 0
    #matrix [y][x]
    #navrhnem seriu ifov aby to fungovalo
    if x<width-1 and matrix[y][x+1] == 1:
        count += 1
    if x<width-1 and y<height-1 and matrix[y+1][x+1] == 1:
        count += 1
    if y<height-1 and matrix[y+1][x] == 1:
        count += 1
    if x>0 and y<height-1 and matrix[y+1][x-1] == 1:
        count += 1
    if x>0 and matrix[y][x-1] == 1:
        count += 1
    if x>0 and y>0 and matrix[y-1][x-1] == 1:
        count += 1
    if y>0 and matrix[y-1][x] == 1:
        count += 1
    if x<width-1 and y>0 and matrix[y-1][x+1] == 1:
        count += 1
    return count

def rewrite(oldfield, newfield):
    for x in range(width):
        for y in range(height):
            if old_field[y][x] == 1:
                friends = return_friends(x,y,old_field)
                if friends == 2 or friends == 3:
                    new_field[y][x] = 1
                elif friends < 2:
                    new_field[y][x] = 0
                elif friends > 3:
                    new_field[y][x] = 0
            elif old_field[y][x] == 0:
                friends = return_friends(x, y, old_field)
                if friends == 3:
                    new_field[y][x] = 1

width, height = fr.readline().split(" ")
width = int(width)
height = int(height)

#vytvori 2rozmerny zoz plny 0
old_field = create2Dmatrix(width,height)
#vytvori iny 2rozmerny zoz plny 0
new_field = create2Dmatrix(width,height)
#do 1.zoz nahodime 1 zo suboru
processfile(old_field)
while True:
    #printnes stary matrix
    #vypocitas novy matrix
    #novy hodime do stareho
    #novy vynulujeme
    print(old_field)
    rewrite(old_field, new_field)
    old_field = new_field.copy()
    new_field = create2Dmatrix(width, height)
    input()
# 1. ak je v bunke organizmus a ten má práve 2 alebo 3 susedov, tak táto bunka prežije aj
# # do ďalšej generácie
# 2. ak je v bunke organizmus a má menej ako 2 susedov, organizmus do ďalšej generácie
# # neprežije (umiera na samotu)
# 3. ak je v bunke organizmus a má viac ako 3 susedov, organizmus do ďalšej generácie
# # neprežije (umiera na premnoženie)
# 4. ak v bunke nie je organizmus a zároveň má za susedov práve tri organizmy, tak sa tu v
# # ďalšej generácii narodí nový organizmus.

