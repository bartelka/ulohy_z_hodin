from string import ascii_lowercase

hlbka = 3
vysledok = []
for i in range(hlbka):
    vysledok.append("a")


def genhesla(h):
    if h == -1:
        print(vysledok)
    else:
        for pis in ascii_lowercase:
            vysledok[h-1] = pis
            genhesla(h-1)

genhesla(hlbka)
#du dorobit aby to slo odpredu
