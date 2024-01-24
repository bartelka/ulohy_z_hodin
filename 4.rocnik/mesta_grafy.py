fr_1 = open("vrcholy.txt", "r", encoding="utf-8")
vrcholy = [i.strip().split(";") for i in fr_1]

fr_2 = open("hrany.txt", "r", encoding="utf-8")
hrany = [i.strip().split(";") for i in fr_2]

def kresli_mesto(vrcholy):
    global mestecka
    for i in vrcholy:
        canvas.create_oval(int(i[1]) - 2, int(i[2]) - 2, int(i[1]) + 2, int(i[2]) + 2, fill="hotpink")
        canvas.create_text(int(i[1]), int(i[2]) + 8, fill="black", text=i[0])
        mestecka[i[0]] = mestecka.get(i[0], (int(i[1]), int(i[2])))

def kresli_hrany():
    for mesto, susedia in mesta.items():
        for i in range(len(susedia)):
            canvas.create_line(mestecka[mesto][0], mestecka[mesto][1], mestecka[susedia[i]][0], mestecka[susedia[i]][1], fill="magenta")
def priradenie_miest(hrany):
    global mesta
    for i in hrany:
        mesta[i[0]] = mesta.get(i[0], [])
    for i in hrany:
        mesta[i[0]].append(i[1])

def priradenie_hodnot(hrany):
    global mesta_hodnoty
    for i in hrany:
        mesta_hodnoty[i[0]] = mesta_hodnoty.get(i[0], {})
    for i in hrany:
        mesta_hodnoty[i[0]].get(i[0], i[1],0)


import tkinter as tk

win = tk.Tk()

w = 1200
h = 900

#mestecka = mesta so suradnicami
mestecka = {}
#mesta = k mestam su priradene susedne mesta
mesta = {}

mesta_hodnoty = {}

canvas = tk.Canvas(width=w, height=h, bg="white")
canvas.pack()

priradenie_miest(hrany)
priradenie_hodnot(hrany)
kresli_mesto(vrcholy)
kresli_hrany()
print(mestecka)
print(mesta)
print(mesta_hodnoty)
win.mainloop()
#dudo.gvpt.sk zadanie -> grafy(hrany.txt, vrcholy.txt)