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
def generate_ascii_code(first_char, nr):
    z = [chr(cod_ascii) for cod_ascii in range(ord(first_char), ord(first_char) + nr)]
    L = []
    for i in z:
        x = hex(ord(i))[2:]
        L += [x]
    return L

def ex1():
    # pentru exemplul {'a'....'z'}    
    print(" ".join(generate_ascii_code('a', 26)))
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
# ex4()


#Ex 4 varianta 2
def rezolva_sistem(a, b, c, d, e):
    for x in range(-10**3, 10**3):
        for y in range(-10**3, 10**3):
            for z in range(-10**3, 10**3):
                for w in range(-10**3, 10**3):
                    if a * x + b * y + c * z + d * w == e:
                        return x, y, z, w
    return None

def ex4_var2():
    # Pentru sistemul 2x + 3y + 4z + 5w = 10:
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    solutie = rezolva_sistem(a, b, c, d, e)
    if solutie is not None:
        print("Solutia sistemului este:")
        print(f"x = {solutie[0]}")
        print(f'y = {solutie[1]}')
        print(f'z = {solutie[2]}')
        print(f'w = {solutie[3]}')
    else:
        print("Sistemul nu are solutie sau nu a fost gasita in intervalul dat.")
# ex4_var2()

#Ex4 varianta3
def gauss_elimination(coefficients, constants):
    n = len(constants)
    for i in range(n): #transformare in matrice superior triunghiulara
        max_row = i
        for k in range(i + 1, n):
            if abs(coefficients[k][i]) > abs(coefficients[max_row][i]):
                max_row = k
        coefficients[i], coefficients[max_row] = coefficients[max_row], coefficients[i]
        constants[i], constants[max_row] = constants[max_row], constants[i]
        pivot = coefficients[i][i]
        if pivot == 0:
            raise ValueError("Sistemul este incompatibil sau are solutii infinite.")
        for j in range(i, n):
            coefficients[i][j] /= pivot
        constants[i] /= pivot
        for k in range(n):
            if k != i:
                factor = coefficients[k][i]
                for j in range(i, n):
                    coefficients[k][j] -= factor * coefficients[i][j]
                constants[k] -= factor * constants[i]
    solutions = [0] * n
    for i in range(n):
        solutions[i] = constants[i]
    return solutions

def ex4_var3():
    coefficients = [[2, 1, -1, 3],
                    [1, 1, 1, 6],
                    [1, -1, 2, 2],
                    [2, 2, 1, 3]]
    constants = [4, 7, 0, 5]

    solutions = gauss_elimination(coefficients, constants)
    print("Solutiile sunt:", solutions)
ex4_var3()

# Transformarea matricei coeficienților într-o matrice superior triunghiulară:
# Găsim rândul cu cel mai mare element în coloană și schimbăm rândurile astfel încât acest element să fie în rândul curent.
# Facem coeficientul de pe coloana curentă și rândul curent să fie 1, împărțind întreg rând la
# valoarea pivot (elementul de pe diagonala principală).
# Eliminăm coeficienții sub și deasupra pivotului facându-i să fie 0. Asta se face prin scăderea unor linii din
# altele, astfel încât matricea devine treptat superior triunghiulară.
# După ce matricea coeficienților a fost transformată într-o matrice superior triunghiulară,
# se pot calcula soluțiile sistemului. De la ultima ecuație la prima, se calculează valorile necunoscute folosind valorile deja calculate. 
# Pentru fiecare coloană, programul găsește pivotul, care este primul element diferit de zero pe acea coloană. 
# Dacă se găsește un pivot zero în timpul procesului de eliminare Gauss, programul va ridica o excepție pentru a indica că sistemul
# este incompatibil sau are soluții infinite.


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
# ex5()


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
# ex6()


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


#Ex 7 varianta 2
def calculate_matrixes(matrix_list):
    matrixes = []
    for matrix in matrix_list:
        new_mat = []
        for row in matrix:
            new_mat.append([int(bit) for bit in bin(row)[2:].rjust(8, '0')])
        matrixes.append(new_mat)
    return matrixes

def ex7_var2():
    matrix_list = [
                    [0x00, 0x00, 0xFC, 0x66, 0x66, 0x66, 0x7C, 0x60, 0x60, 0x60, 0x60, 0xF0, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0x00, 0x00, 0x00, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7E, 0x06, 0x0C, 0xF8, 0x00],
                    [0x00, 0x00, 0x10, 0x30, 0x30, 0xFC, 0x30, 0x30, 0x30, 0x30, 0x36, 0x1C, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0xE0, 0x60, 0x60, 0x6C, 0x76, 0x66, 0x66, 0x66, 0x66, 0xE6, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0x00, 0x00, 0x00, 0x7C, 0xC6, 0xC6, 0xC6, 0xC6, 0xC6, 0x7C, 0x00, 0x00, 0x00, 0x00],
                    [0x00, 0x00, 0x00, 0x00, 0x00, 0xDC, 0x66, 0x66, 0x66, 0x66, 0x66, 0x66, 0x00, 0x00, 0x00, 0x00]
                  ]
    for matrix in calculate_matrixes(matrix_list):
        for line in matrix:
            for element in line:
                print(element, end="")
            print(end="\n")
        print(end="\n")
ex7_var2()


#Ex 8
def ex8():
    # Plec de la premisa ca fiecare punct y se gaseste la distanta egala pe axa Ox
    y = [1, 3, 2, 5, 7] #secventa de valori y
    suprafata = 0
    # Calculez aria aplicand metoda trapezului:
    for i in range(len(y) - 1):
        suprafata += (y[i] + y[i + 1]) * 1 / 2
        # aria = (baza mica + baza mare) * inaltime / 2, unde "inaltimea" (distanta dintre x1 si x2) este 1
    print(suprafata)
# ex8()