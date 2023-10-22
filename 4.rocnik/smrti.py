fr = open("WHO-COVID-19-global-data.csv","r",encoding="utf-8")

rad = fr.readline()
subor = fr.readlines()

data = [riadok.strip().split(",")[-1] for riadok in subor]
relat_pocetnost = {}
znaky = {}
riadky = len(data)
ocakavanie = {"1":30.1, "2":17.6, "3":12.5, "4":9.7, "5":7.9, "6":6.7, "7":5.8, "8":5.1, "9":4.6}
for i in data:
    znaky[i[0]] = znaky.get(i[0],0)+1

for znak, pocet in znaky.items():
    if znak != "0":
        x = round(pocet / riadky * 100, 2)
        relat_pocetnost[znak] = relat_pocetnost.get(znak,x)

for i in range(1,10):
    print("Chi-kvadrát test pre",str(i),":",(relat_pocetnost[str(i)]-ocakavanie[str(i)])**2/(ocakavanie[str(i)]))
print(relat_pocetnost)

