fr = open("input.gol", "r", encoding="utf-8")

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
    for zoz in matrix:
        for i in zoz:
            if i == 1:
                if x>0 and y>0:
                    if [x,y-1] == "1":
                        count+=1
                    if [x-1,y-1] == "1":
                        count += 1
                    if [x+1,y-1] == "1":
                        count += 1
                    if [x+1,y] == "1":
                        count += 1
                    if [x-1,y] == "1":
                        count += 1
                    if [x,y+1] == "1":
                        count += 1
                    if [x+1,y+1] == "1":
                        count += 1
                    if [x-1,y+1] == "1":
                        count += 1
                elif x == 0 and y==0:
                    if [x+1,y] == "1":
                        count += 1
                    if [x,y+1] == "1":
                        count += 1
                    if [x+1,y+1] == "1":
                        count += 1
                elif x == 0 and y > 0:
                    if [x+1,y-1] == "1":
                        count += 1
                    if [x+1,y] == "1":
                        count += 1
                    if [x-1,y] == "1":
                        count += 1
                    if [x,y+1] == "1":
                        count += 1
                    if [x+1,y+1] == "1":
                        count += 1
                elif x>0 and y==0:
                    if [x+1,y] == "1":
                        count += 1
                    if [x-1,y] == "1":
                        count += 1
                    if [x,y+1] == "1":
                        count += 1
                    if [x+1,y+1] == "1":
                        count += 1
                    if [x-1,y+1] == "1":
                        count += 1
    return count

width, height = fr.readline().split(" ")
width = int(width)
height = int(height)

#vytvori 2rozmerny zoz plny 0
old_field = create2Dmatrix(width,height)
#vytvori iny 2rozmerny zoz plny 0
new_field = create2Dmatrix(width,height)
#do 1.zoz nahodime 1 zo suboru
processfile(old_field)

# 1. ak je v bunke organizmus a ten má práve 2 alebo 3 susedov, tak táto bunka prežije aj
# # do ďalšej generácie
# # 2. ak je v bunke organizmus a má menej ako 2 susedov, organizmus do ďalšej generácie
# # neprežije (umiera na samotu)
# # 3. ak je v bunke organizmus a má viac ako 3 susedov, organizmus do ďalšej generácie
# # neprežije (umiera na premnoženie)
# # 4. ak v bunke nie je organizmus a zároveň má za susedov práve tri organizmy, tak sa tu v
# # ďalšej generácii narodí nový organizmus.


