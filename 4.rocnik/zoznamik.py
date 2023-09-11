vysledok = []

def flat_list(l:list):
    global vysledok
    for i in l:
        if type(i) == int:
            vysledok.append(i)
        else:
            flat_list(i)
    return vysledok

print(flat_list([1,[2,2,2],4]))