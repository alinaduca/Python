# 1.Write a function that receives as parameters two lists a and b and returns a list of sets containing: (a intersected with b,
# a reunited with b, a - b, b - a).

#Ex 1
def operationsOnLists(A_list, B_list):
    A = set(A_list)
    B = set(B_list)
    intersection = A & B
    union = A | B
    A_minus_B = A - B
    B_minus_A = B - A
    return [intersection, union, A_minus_B, B_minus_A]

def ex1():
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
# ex1()



# 2. Write a function that receives a string as a parameter and returns a dictionary in which the keys are the characters in the
# character string and the values are the number of occurrences of that character in the given text.
# Example: For string "Ana has apples." given as a parameter the function will return the dictionary:
# {'a': 3, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}.

#Ex 2
def appearances(str):
    dict = {}
    for char in str:
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
    return dict

def ex2():
    str = "Ana has apples."
    print(appearances(str))
# ex2()



# 3. Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be
# recursively covered because they can contain other containers, such as dictionaries, lists, sets etc.)

#Ex 3
def are_equal(d_1, d_2, depth):
    if type(d_1) == type(d_2):
        if type(d_1) is dict:
            same = True
            differences = []
            for label_1, label_2 in zip(sorted(d_1.keys()), sorted(d_2.keys())):
                if label_1 != label_2:
                    same = False
                    differences.append((label_1, label_2, "depth = " + str(depth), "different keys"))
                    continue
                verify_equal = are_equal(d_1[label_1], d_2[label_1], depth + 1)
                if not verify_equal[0]:
                    same = False
                    differences += verify_equal[1]
            else:
                return same, differences
        if d_1 != d_2:
            return False, [(d_1, d_2, "depth = " + str(depth), "are not equal")]
        else:
            return True, []
    else:
        return False, [(d_1, d_2, "depth = " + str(depth), "different type")]

def ex3():
    d_1 = {'a': {'b': 0}, 's': 4, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
    d_2 = {'a': {'a': 3}, 's': 2, '.': 1, 'e': 1, 'h': 1, 'l': 1, 'p': 2, ' ': 2, 'A': 1, 'n': 1}
    print(are_equal(d_1, d_2, 0))
# ex3()



# 4. The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters.
# Build and return a string that represents the corresponding XML element.
# Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns the
# string = "<a href=\"http://python.org \ "_class = \" my-link \ "id = \" someid \ "> Hello there </a>"

# Ex 4
def build_xml_element(tag, content, **dict):
    xml = '<' + tag
    for (key, val) in dict.items():
        xml += ' ' + key + '=\\"'+val + '\ "'
    xml += "> " + content + " </" + tag + ">"

    return xml

def ex4():
    print(build_xml_element("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid "))
ex4()



# 5. The validate_dict function that receives as a parameter a set of tuples (that represents validation rules for a dictionary
# that has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix").
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and
# ends with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.
# Example: the rules  s={("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}  and d= {"key1": "come inside,
# it's too cold out", "key3": "this is not valid"} => False because although the rules are respected for "key1" and "key2" "key3"
# that does not appear in the rules.

#Ex 5
def validate_dict(rules, dict):
    for tup in rules:
        if tup[0] not in dict.values():
            return False
        content = dict[tup[0]]
        if not content.startswith(tup[1]):
            return False
        if not content.endwith(tup[3]):
            return False
        if content.startswith(tup[2]) or content.endswith(tup[2]):
            return False
        if content.find(tup[2]) < 1:
            return False
    return True

def ex5():
    s = {("key1", "", "inside", ""), ("key2", "start", "middle", "winter")}
    d = {"key1": "come inside, it's too cold out", "key3": "this is not valid"}
    print(validate_dict(s, d))
# ex5()



# 6. Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements
# in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).

#Ex 6
def unique_elements_and_duplicate(input_list):
    return (len(set(input_list)), len(input_list) - len(set(input_list)))

def ex6():
    input_list = [1, 1, 2, 3]
    print(unique_elements_and_duplicate(input_list))
# ex6()



# 7. Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets
# two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets,
# and op is the applied operator: |, &, -. 
# Ex: {1,2}, {2, 3} =>
# {
#     "{1, 2} | {2, 3}":  {1, 2, 3},
#     "{1, 2} & {2, 3}":  { 2 },
#     "{1, 2} - {2, 3}":  { 1 },
#     ...
# }

#Ex 7
def apply_operation(*sets):
    for singular_set in sets:
        if not isinstance(singular_set, set):
            return "Invalid input"
    result = dict()
    list_of_sets = list()
    for singular_set in sets:
        list_of_sets.append(singular_set)
    for i in range(len(list_of_sets)):
        for j in range(i + 1, len(list_of_sets)):
            if list_of_sets[i] != list_of_sets[j]:
                result[str(list_of_sets[i]) + ' | ' + str(list_of_sets[j])] = \
                    list_of_sets[i].union(list_of_sets[j])
                result[str(list_of_sets[i]) + ' & ' + str(list_of_sets[j])] = \
                    list_of_sets[i].intersection(list_of_sets[j])
                result[str(list_of_sets[i]) + ' - ' + str(list_of_sets[j])] = list_of_sets[i] - list_of_sets[j]
                result[str(list_of_sets[j]) + ' - ' + str(list_of_sets[i])] = list_of_sets[j] - list_of_sets[i]
    return result

def ex7():
    operation_dict = apply_operation({1, 2}, {2, 3}, {2, 9, 20})
    for operation in operation_dict:
        print(operation, ":", operation_dict[operation])
# ex7()



# 8. Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start".
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value
# of the current key is the key for the next value, until you find a loop (a key that was visited before).
# The function must return the list of objects obtained as previously described.
# Ex: loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}) will
# return ['a', '6', 'z', '2'].

#Ex 8
def loop(mapping):
    current = 'start'
    visited = [current]
    values = list()
    while True:
        current = mapping[current]
        if current in visited:
            return values
        visited.append(current)
        values.append(current)

def ex8():
    print(loop({'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}))
# ex8()



# 9. Write a function that receives a variable number of positional arguments and a variable number of keyword arguments and
# will return the number of positional arguments whose values can be found among keyword arguments values.

#Ex 9
def positional_arguments(*positions, **arguments):
    count = 0
    for p in positions:
        if p in arguments.values():
            count += 1
    return count

def ex9():
    print(positional_arguments(1, 2, 3, 4, x=1, y=2, z=3, w=5))

# ex9()