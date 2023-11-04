class Floare:
    def __init__(self, culoare, tip):
        self.culoare = culoare
        self.tip = tip
        self.inaltime = 1
    
    def __str__(self):
        return f"Floarea cu culoare {self.culoare} si tipul de floare {self.tip} si inaltimea {self.inaltime}"
    
    def Grow(self, how_much):
        self.inaltime += how_much

f1 = Floare("verde", "lalea")
print(f1)
f1.Grow(10)
print(f1)

f2 = Floare('rosu', 'trandafir')
f3 = Floare('albastru', 'orhidee')
f2.Grow(15)
f3.Grow(21)

print(f2)
print(f3)