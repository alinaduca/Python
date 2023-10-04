import time
import random
import json
import math
import tkinter

# print(range(100))
nr = random.choice(range(100))
print(nr)

# x = "".join(str(nr))

n = 1
while True:
    x = input("Dati nr: ")
    dif = abs(nr - int(x))
    if dif >= 50:
        print("rece")

    elif dif >= 10 and dif < 50:
        print("cald")

    elif dif < 10 and dif != 0:
        print("fierbinte")

    else:
        print("Ai ghicit!")
        break
    n += 1


# print(dif, nr, x)