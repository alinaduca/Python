import re
import sympy
from sympy import symbols, Eq, solve


# Ex0
def ex0():
    n = int(input("Dati n: "))
    S = n * (n + 1) / 2         # Rezolvare cu Suma lui Gauss
    # for i in range(n + 1):    # Rezolvare cu un for loop (mai puțin eficient)
    #     S += i
    print(S)
# ex0()


# Ex1
def ex1():
    # pentru exemplul {'a'....'z'}
    z = [chr(cod_ascii) for cod_ascii in range(ord('a'), ord('a') + 26)]
    L = []
    for i in z:
        x = hex(ord(i))[2:]
        L += [x]
    print(" ".join(L))
# ex1()


#Ex 2
def ex2():
    L = [0, 1, 2, 3, 4]
    l = [bin(n)[2:].rjust(8, '0') for n in L]
    # Prima varianta - folosind re.findall:
    # print(" ".join(l) + " " + str(len(re.findall("0", " ".join(l)))) + " " + str(len(re.findall("1", " ".join(l)))))
    
    # A doua varianta - folosind functia count:
    secventa_de_biti = " ".join(l)
    print("'" + secventa_de_biti + "'", secventa_de_biti.count('0'), secventa_de_biti.count('1'))
# ex2()


#Ex 3
def ex3():
    p = 10 ** 100
    n1 = 2
    n2 = 3
    rez = n1 * p // n2
    intreg = n1 // n2
    final_result = str(intreg) + "."
    if(intreg == 0):
        final_result += str(rez).rjust(100, '0')
    else:
        final_result += str(rez)[len(str(intreg)):].rjust(100, '0')
    print(final_result)
# ex3()


#Ex 4
def ex4():
    #necunoscute
    x, y, z, w = symbols('x y z w')

    #coeficienți și termeni liberi
    a1, b1, c1, d1, e1 = 2, 3, 4, 1, 10
    a2, b2, c2, d2, e2 = 1, -1, 1, 1, 5
    a3, b3, c3, d3, e3 = 3, 2, 2, 3, 15
    a4, b4, c4, d4, e4 = 2, 1, 2, -1, 4

    #ecuațiile
    eq1 = Eq(a1 * x + b1 * y + c1 * z + d1 * w, e1)
    eq2 = Eq(a2 * x + b2 * y + c2 * z + d2 * w, e2)
    eq3 = Eq(a3 * x + b3 * y + c3 * z + d3 * w, e3)
    eq4 = Eq(a4 * x + b4 * y + c4 * z + d4 * w, e4)

    solutions = solve((eq1, eq2, eq3, eq4), (x, y, z, w))

    print("Solutiile sistemului de ecuatii:")
    print(solutions)
ex4()


#Ex 5
def nth_root(x, n, precision=50):
    #radacina = radacina * 10^50  | ridicare la puterea n
    #radacina^n (adica x) = radacina^n * 10^(50*n)
    x = x * (10 ** (precision * n))

    guess = x // 2
    #metoda lui Newton
    while(True):
        old_guess = guess
        #forma comuna, pentru eficienta computationala:
        guess = ((n - 1) * guess + x // (guess**(n - 1))) // n
        if old_guess == guess:
            break

    #transformare în format cu zecimale:
    result = str(guess)
    integer_part = result[:-precision]
    fractional_part = result[-precision:]
    return f"{integer_part}.{fractional_part}"

def ex5():
    x = 1000
    n = 5
    result = nth_root(x, n, precision=50)
    print(f"{n}-radical din {x}: {result}")
ex5()


#Ex 6
def genereaza_permutare(n, p, alfabet):
    if (n >= len(alfabet) ** p or p < 0 ):
        print("Permutarea nu exista")
        return None
    permutare = alfabet[0] * p
    while n > 0:
        # print(permutare)
        p -= 1
        index = int(n % len(alfabet))
        permutare = permutare[:p] + alfabet[index] + permutare[p + 1:]
        n //= len(alfabet)
    return permutare

# Pentru p = 4:
    # n = 0: aaaa
    # n = 1: aaab
    # n = 2: aaac
    # ...
    # n = 25: aaaz
    # n = 26: aaba

def ex6():
    alfabet = 'abcdefghijklmnopqrstuvwxyz'
    n = 265
    p = 4
    print(genereaza_permutare(n, p, alfabet))
ex6()


#Ex 7
def generate_matrixes(matrix_list):
    for matrix in matrix_list:
        for row in matrix:
            print(bin(row)[2:].rjust(8, '0'))
        print()

def ex7():
    matrix_list = [
                    [0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
                    [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]
                  ]
    generate_matrixes(matrix_list)
# ex7()


#Ex 8
def ex8():
    # Plec de la premisa ca fiecare punct y se gaseste la distanta egala pe axa Ox
    Ox = 90 #lungimea intervalului pe axa Ox
    y = [1, 3, 2, 5, 7] #secventa de valori y
    suprafata = 0
    # Calculez aria aplicand metoda trapezului:
    for i in range(len(y) - 1):
        suprafata += (y[i] + y[i + 1]) * (Ox / (len(y) - 1)) / 2
        # aria = (baza mica + baza mare) * inaltime / 2
    print(suprafata)
# ex8()