sachovnica= []
for i in range(8):
    riadok = []
    for j in range(8):
        riadok.append(0)
    sachovnica.append(riadok)

#je mozne to nahradit
#riadok1 = [0] * 8

def check(x:int,y:int) -> bool:
    for j in range(8):
        for i in range(8):
            if i == x or j == y or i + j == x + y or i - j == x - y:
                if sachovnica[j][i] == 1:
                    return False
    return True
pocet = 0
def drticka(dama:int):
    global sachovnica, pocet
    if dama == 8 :
        print(sachovnica)
        pocet += 1
    for i in range(8):
        if check(i,dama):
            sachovnica[dama][i] = 1
            drticka(dama+1)
            sachovnica[dama][i] = 0

drticka(0)
print(pocet)