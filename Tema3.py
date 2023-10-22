# 1. Write a function to return a list of the first n numbers in the Fibonacci string.

#Ex 1
def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        L = [1, 1]
        for i in range(2, n):
            L.append(L[i - 1] + L[i - 2])
        return L

def ex1():
    print(fibonacci(10))
# ex1()



# 2. Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

#Ex2
def isPrime(n):
    if n <= 1 or (n % 2 == 0 and n != 2):
        return False
    else:
        d = 3
        while d * d <= n and n % d != 0:
            d += 2
        if d * d > n:
            return True
        else:
            return False

def primeList(L):
    primes = []
    for n in L:
        if isPrime(n):
            primes.append(n)
    return primes

def ex2():
    L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(primeList(L))
# ex2()



# 3. Write a function that receives as parameters two lists a and b and returns: (a intersected with b, a reunited with b, a - b, b - a).

#Ex 3
def operationsOnLists(A, B):
    intersection = []
    union = A.copy()
    A_minus_B = A.copy()
    B_minus_A = B.copy()
    for element in B:
        if A.count(element) != 0:
            intersection.append(element)
            A_minus_B.remove(element)
            B_minus_A.remove(element)
        else:
            union.append(element)
    return (intersection, union, A_minus_B, B_minus_A)

def ex3():
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    B = [2, 4, 6, 8, 10, 12, 14, 16]
    operations = operationsOnLists(A, B)
    intersection = operations[0]
    union = operations[1]
    difference1 = operations[2]
    difference2 = operations[3]
    print("A =", A)
    print("B =", B)
    print("A ∩ B =", intersection)
    print("A U B =", union)
    print("A - B =", difference1)
    print("B - A =", difference2)
# ex3()



# 4. Write a function that receives as a parameters a list of musical notes (strings), a list of moves (integers) and a start position (integer). The function will return the song composed by going though the musical notes beginning with the start position and following the moves given as parameter.
#Example : compose(["do", "re", "mi", "fa", "sol"], [1, -3, 4, 2], 2) will return ["mi", "fa", "do", "sol", "re"]    

#Ex 4
def compose(musical_notes, moves, start_position):
    song = []
    pos = start_position
    for i in range(len(moves)):
        song.append(musical_notes[pos % 5])
        pos += moves[i]
    song.append(musical_notes[pos % 5])
    return song

def ex4():
    musical_notes = ["do", "re", "mi", "fa", "sol"]
    moves = [1, -3, 4, 2]
    start_position = 2
    print(compose(musical_notes, moves, start_position))
# ex4()



# 5. Write a function that receives as parameter a matrix and will return the matrix obtained by replacing all the elements under the main diagonal with 0 (zero).

#Ex 5
def triangularMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j] = 0
    return matrix

def ex5():
    matrix = [
        [2, 3, 8],
        [4, 2, 6],
        [5, 7, 1]
    ]
    print(triangularMatrix(matrix))
# ex5()



# 6. Write a function that receives as a parameter a variable number of lists and a whole number x. Return a list containing the
# items that appear exactly x times in the incoming lists. 
# Example: For the [1,2,3], [2,3,4],[4,5,6], [4,1, "test"] and x = 2 lists [1,2,3 ] # 1 is in list 1 and 4, 2 is in list 1
# and 2, 3 is in lists 1 and 2.

#Ex 6
def appearances(*lists, x):
    L = []
    for li in lists:
        L.extend(li)
    result = []
    for item in set(L):
        if L.count(item) == x:
            result.append(item)
    return result

def ex6():
    print(appearances([1,2,3], [2,3,4], [4,5,6], [4,1, "test"], x = 2))
# ex6()



# 7. Write a function that receives as parameter a list of numbers (integers) and will return a tuple with 2 elements.
# The first element of the tuple will be the number of palindrome numbers found in the list and the second element will be
# the greatest palindrome number.

#Ex 7
def palindrome(L):
    x = [x for x in L if x != 1 and len([y for y in range(2, x // 2 + 1) if x % y == 0]) == 0]
    return (len(x), max(x))

def ex7():
    lungime, maxim = palindrome([1, 2, 3, 4, 101])
    print("Lungimea este:", lungime)
    print("Maximul este:", maxim)
# ex7()

# 8. Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True.
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True,
# otherwise it should contain characters that have the ASCII code not divisible by x.
# Example: x = 2, ["test", "hello", "lab002"], flag = False will return (["e", "s"], ["e" .
# Note: The function must return list of lists.

#Ex 8
def generate(L, x = 1, flag = True):
    T = []
    for word in L:
        letters = []
        for letter in word:
            if (ord(letter) % x == 0 and flag == True) or (ord(letter) % x != 0 and flag == False):
                letters.extend(letter)
        T.append(letters)
    return tuple(T)

def ex8():
    x = 2
    L = ["test", "hello", "lab002"]
    flag = False
    print(generate(L, x, flag))
# ex8()



#Ex 9
def unluckySpectators(stadium):
    L = list()
    for column in range(len(stadium[0])):
        for line in range(1, len(stadium)):
            for manInFront in range(line):
                if stadium[line][column] <= stadium[manInFront][column]:
                    if(L.count((line, column)) == 0):
                        L.append((line, column))
    return L

def ex9():
    stadium = [
        [1, 2, 3, 2, 1, 1],
        [2, 4, 4, 3, 7, 2],
        [5, 5, 2, 5, 6, 4],
        [6, 6, 7, 6, 7, 5]
    ]
    print(unluckySpectators(stadium))
# ex9()



# 10. Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains
# the first items in the lists, the second element contains the items on the position 2 in the lists, etc.
# Ex: for lists [1,2,3], [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 
# Note: If input lists do not have the same number of items, missing items will be replaced with None to be able to generate
# max ([len(x) for x in input_lists]) tuples.

#Ex 10
def generate(*lists):
    result = []
    max_list = 0
    for li in lists:
        if len(li) > max_list:
            max_list = len(li)
    for _ in range(max_list):
        result.append([])
    for li in lists:
        i = 0
        for tup in result:
            try:
                tup.append(li[i])
            except:
                tup.append(None)
            i += 1
    result1 = []
    for tup in result:
        result1.append(tuple(tup))
    return result1

def ex10():
    print(generate([1, 2, 3], [5, 6, 7], ["a", "b", "c"]))
# ex10()



# 11. Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple.
# Example: [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

#Ex 11
def custom_key(item):
        if len(item[1]) >= 3:
            return item[1][1]
        else:
            return item[1]

def ex11():
    L = [('abc', 'bcd'), ('abc', 'zza')]
    sorted_list = sorted(L, key = custom_key)
    print(sorted_list)
# ex11()



# 12. Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme.
# Two words rhyme if both of them end with the same 2 letters.
# Example: group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return
# [['ana', 'banana'], ['carte', 'parte'], ['arme']] 

#Ex 12
def group_of_rhyme(L):
    list_of_lists = []
    list_of_lists.append([L.pop(0)])
    for word in L:
        ok = False
        for li in list_of_lists:
            if li[0][-2:] == word[-2:]:
                ok = True
                li.append(word)
        if ok == False:
            list_of_lists.append([word])
    return list_of_lists

def ex12():
    L = ["ana", "banana","carte","arme","parte"]
    print(group_of_rhyme(L))
# ex12()