import math
import re

#Ex 1
def cmmdc(number_list):
    if len(number_list) < 2:
        return None
    result = number_list[0]
    for num in number_list[1:]:
        # result = math.gcd(result, num) OR
        while num:
            result, num = num, result % num
    return result

def ex1():
    numbers = []
    x = int(input('Input a number\n'))
    while x > 1:
        if x <= 1:
            break
        numbers.append(x)
        x = int(input('Input a number\n'))
    print("Cmmdc pentru ", numbers, " = ", cmmdc(numbers))



#Ex 2
def ex2():
    str = input("Enter a string\n")
    vowel_count = 0
    for char in str:
        for vowel in "aeiouAEIOU":
            if char == vowel:
                vowel_count += 1
    print("String ", str, " has ", vowel_count, " vowels.")


#Ex 3
def ex3():
    str1 = "dadada"
    str2 = "da"
    # print(s_1.count(s_2)) OR

    count = 0
    start = 0
    while True:
        start = str1.find(str2, start)
        if start == -1:
            break
        count += 1
        start += 1
    return count


#Ex 4
def ex4():
    upperCamelCaseString = "UpperCaseString"
    lowercase_with_underscores_string = ""
    if upperCamelCaseString[0].isupper():
        lowercase_with_underscores_string += upperCamelCaseString[0].lower()
        upperCamelCaseString = upperCamelCaseString[1:]
    for char in upperCamelCaseString:
        if char.isupper():
            lowercase_with_underscores_string += "_" + char.lower()
        else:
            lowercase_with_underscores_string += char
    else:
        print(lowercase_with_underscores_string)

#Ex 5
def get_spiral_string(target_matrix):
    spiral_string = ""
    while len(target_matrix) > 0:
        for i in target_matrix[0]:
            spiral_string += str(i)
        else:
            target_matrix = target_matrix[1:]
        # print(spiral_string, "1")
        if len(target_matrix) == 0:
            break
        for i in target_matrix:
            spiral_string += str((i[-1:])[0])
        else:
            target_matrix = [row[:-1] for row in target_matrix]
        # print(spiral_string, "2")
        if len(target_matrix) == 0:
            break
        reversed_last_line = ((target_matrix[-1:])[0])[::-1]
        for i in reversed_last_line:
            spiral_string += str(i)
        else:
            target_matrix = target_matrix[:-1]
        # print(spiral_string, "3")
        if len(target_matrix) == 0:
            break
        for i in target_matrix[::-1]:
            spiral_string += str(i[0])
        else:
            target_matrix = [row[1:] for row in target_matrix]
        # print(spiral_string, "4")
    return spiral_string


def ex5():
    rows = 4
    cols = 4
    mat = [["" for _ in range(cols)] for _ in range(rows)]  # Initialize with empty strings
    mat[0][0], mat[0][1], mat[0][2], mat[0][3] = "f", "i", "r", "s"
    mat[1][0], mat[1][1], mat[1][2], mat[1][3] = "n", "_", "l", "t"
    mat[2][0], mat[2][1], mat[2][2], mat[2][3] = "o", "b", "a", "_"
    mat[3][0], mat[3][1], mat[3][2], mat[3][3] = "h", "t", "y", "p"
    print(get_spiral_string(mat))


#Ex 6
def is_palindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    return False

def ex6():
    input_number = input("Enter a number\n")
    input_number = int(input_number)
    if is_palindrome(input_number):
        print(input_number, " is palindrome")
    else:
        print(input_number, " is not palindrome")


#Ex 7
def ex7():
    input_text = input('Enter a text with numbers inside\n')
    i = 0
    str_len = len(input_text)
    while i < str_len:
        if input_text[i].isdigit():
            first_number = ""
            while i < str_len and input_text[i].isdigit():
                first_number += input_text[i]
                i += 1
            else:
                print(int(first_number))
            break
        i += 1
    else:
        print(input_text + "\nhas no numbers")


#Ex 8
def ex8():
    input_number = input("Enter a number\n")
    input_number = int(input_number)
    set_bits = bin(input_number).count("1")
    print(input_number, " has ", set_bits, " bits with value 1")


#Ex 9
def ex9():
    input_text = input("Enter a text\n")
    most_common_letter = ""
    no_of_apparitions = 0
    for i in input_text:
        if i.isalpha() and input_text.count(i) > no_of_apparitions:
            no_of_apparitions = input_text.count(i)
            most_common_letter = i
    if len(most_common_letter) == 1:
        print("\"", most_common_letter[0], "\"", " was found ", no_of_apparitions, " times")
    else:
        print("Hello there")


#Ex 10
def ex10():
    input_text = input("Enter a text\n")
    word_count = re.findall(r'\w+', input_text)
    print("There are ", len(word_count), " words")

ex10()