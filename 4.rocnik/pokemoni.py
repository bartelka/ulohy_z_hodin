import json
# Opening JSON file
fr = open('pokemoni.json')

# returns JSON object as
# a dictionary
data = json.load(fr)

data1 = {}
for j,i in data.items():
    #print(j)
    for x,y in i.items():
        #print(x,y)
        if j == "super effective":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],2)
            #print(slov)
            data1[x] = data1.get(x,slov)
        if j == "normal effective":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],1)
            #print(slov)
            data1[x].update(slov)
        if j == "not very effective":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],0.5)
            #print(slov)
            data1[x].update(slov)
        if j == "no effect":
            slov = {}
            for z in range(len(y)):
                slov[y[z]] = slov.get(y[z],0)
            #print(slov)
            data1[x].update(slov)
print(data)
print(data1)
print(data1["Normal"]["Ghost"])