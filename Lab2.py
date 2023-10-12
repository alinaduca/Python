# pot sa reprezint seturi (ca un fel de liste, dar cu elemente unice), liste [], tuple, array-uri, dictionare si strings

# l=[] este o lista; l+=[7]; l+=[10] => [7, 10]

# concatenare de liste: l=[7, 10]+[3,4]=>[7, 10, 3, 4]

# l=[7]*10 => lista cu 10 elemente

# slice => pot sa tai lista in tot felul de forme (pot obtine subliste)

# p=l[2:] => de la 2 pana la sf

# q=l[:2]

# t=l[1:3]

# str1 = 'abcdef' => pot aplica slice

# str2 = str1[::-1]

# se comporta ca niste structuri de date



# Tuple

# t1 = (1, 6, 'a')
# ca niste liste, dar nu pot fi modificate (nu le pot reasigna)
# q = (x, y)
# x, y = (10, 20)
# MAP-uri: BST (AVL si R&B)

# d1 = {   //dictionar
#     "k1": 16,
#     "nume": "Alex",
#     'b': True
# }

# range(7) / range(4, 9)
# L = [n for n in range(100)]
# L = []

# 00000000
# 00001001
# hex(n) - '0x9' / bin(n) - '0b1001'
# x = 0x61
# y = 0b1001

# c = " ".join(bin(n)[2:].rjust(8, '0') for n in range(10))
# l = [bin(n)[2:].rjust(8, '0') for n in range(256)]
# print(c)
# print(l)



# Ex1
def ex1():
    n = int(input("Dati n: "))
    S = n * (n + 1) / 2
    # for i in range(n + 1):
    #     S += i
    print(S)

# ex1()

# Ex2
def ex2():
    z = 'abcdefghijkl'
    L = []
    for i in z:
        x = hex(ord(i))[2:]
        L += [x]
    print(" ".join(L))

# ex2()

import re

#Ex 3
def ex3():
    L = [0, 1, 2, 3, 4]
    l = [bin(n)[2:].rjust(8, '0') for n in L]
    print(" ".join(l) + " " + str(len(re.findall("0", " ".join(l)))) + " " + str(len(re.findall("1", " ".join(l)))))
    #l.count(2)/'0'
ex3()

#Ex 4
def ex4():
    p = 10 ** 100
    n1 = 5
    n2 = 3
    rez = n1 * p // n2
    print(rez)

ex4()

#!!! Acest fișier conține numai rezolvările realizate în cadrul laboratorului 2. Pentru vizualizarea tuturor rezolvărilor puteți accesa Tema2.py !!!
