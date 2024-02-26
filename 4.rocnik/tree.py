class Tree:
    def __init__(self, value):
        self.value = value
        self.right_side = None
        self.left_side = None

    def add_right(self, value):
        if self.right_side is None:
            temp = Tree(value)
            self.right_side = temp
        else:
            temp = Tree(value)
            temp.right_side = self.right_side
            self.right_side = temp

    def add_left(self, value):
        if self.left_side is None:
            temp = Tree(value)
            self.left_side = temp
        else:
            temp = Tree(value)
            temp.left_side = self.left_side
            self.left_side = temp

    def get_root_value(self):
        return self.value

    def get_right_tree(self):
        return self.right_side

    def get_left_tree(self):
        return self.left_side


t = Tree(5)
t.add_left(8)
t.add_right(7)
t.get_right_tree().add_left(5)
t.get_right_tree().add_right(2)
t.get_left_tree().add_right(6)

#preorder
#vypise hodnotu
#rekurzivne na lavo if left_tree
#rekurzivne doprava if right_tree


import requests, re

fr = open("hrany.txt", "r", encoding="utf-8")
hrany = [i.strip().split(";") for i in fr]
print(hrany)

page = requests.get("http://www.kolko-km-je.ubytovaniesr.sk")
page.encoding = "windows-1250"

text = page.text
text = re.split("<option value=''>|</select>", text)
text = text[1].split("</option>")[1:-1]

obce = {}

for i in text:
    cislo = re.findall(r"(\d+)", i)
    obec = i.split(">")[1]
    obce[obec] = obce.get(obec, int(cislo[0]))

for i in hrany:
    data = {"ob1":obce[i[0]], "ob2":obce[i[1]]}
    vzdialenost = requests.post("http://www.kolko-km-je.ubytovaniesr.sk", data=data)
    print(re.split("Odpoveď:>|km", vzdialenost.text))
print(obce)
