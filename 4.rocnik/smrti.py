fr = open("WHO-COVID-19-global-data.csv","r",encoding="utf-8")

rad = fr.readline()
subor = fr.readlines()

data = [riadok.strip().split(",")[-1] for riadok in subor]
relat_pocetnost = {}
znaky = {}
riadky = len(data)

for i in data:
    znaky[i[0]] = znaky.get(i[0],0)+1

for znak, pocet in znaky.items():
    if znak != "0":
        x = round(pocet / riadky * 100, 2)
        relat_pocetnost[znak] = relat_pocetnost.get(znak,x)

print(relat_pocetnost)