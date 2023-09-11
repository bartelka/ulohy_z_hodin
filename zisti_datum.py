import math

date = input("datum DD.MM.YYYY: ")
date = date.split(".")

for i in range(3):
    date[i] = int(date[i])

dni_v_tyzdni = ["Sobota", "Nedela", "Pondelok", "Utorok", "Streda", "Stvrtok", "Piatok"]

def najdi_datum():
    K = int(date[2]%100)
    J = int(date[2]/100)
    q = int(date[0])
    m = int(date[1])
    if m == 1:
        m = 13
        K = int((date[2]-1) % 100)
        J = int((date[2]-1) / 100)
    if m == 2:
        m = 14
        K = int((date[2] - 1) % 100)
        J = int((date[2] - 1) / 100)
    h = (q + math.floor((13*(m+1))/5) + K + math.floor(K/4) + math.floor(J/4) - 2*J) % 7
    h = math.floor(h)
    print(dni_v_tyzdni[h])

najdi_datum()