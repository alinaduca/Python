# 1. Write a Python class that simulates a Stack. The class should implement methods like push, pop, peek (the last two methods should
# return None if no element is present in the stack).

# Ex1
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def ex1():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.peek())  #3
    print(stack.pop())   #3
    print(stack.pop())   #2
    print(stack.pop())   #1
    print(stack.pop())   #None
# ex1()



# 2. Write a Python class that simulates a Queue. The class should implement methods like push, pop, peek (the last two methods should
# return None if no element is present in the queue).

# Ex2
class Queue:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
    
def ex2():
    queue = Queue()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    print(queue.peek())  #1
    print(queue.pop())   #1
    print(queue.pop())   #2
    print(queue.pop())   #3
    print(queue.pop())   #None
# ex2()



# 3. Write a Python class that simulates a matrix of size NxM, with N and M provided at initialization. The class should provide methods
# to access elements (get and set methods) and some methematical functions such as transpose, matrix multiplication and a method that
# allows iterating through all elements form a matrix an apply a transformation over them (via a lambda function).

# Ex3
class Matrix:
    def __init__(self, n, m):
        self.rows = n
        self.cols = m
        self.data = [[0 for _ in range(m)] for _ in range(n)]

    def get(self, i, j):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            return self.data[i][j]
        else:
            return None

    def set(self, i, j, value):
        if 0 <= i < self.rows and 0 <= j < self.cols:
            self.data[i][j] = value

    def transpose(self):
        transposed = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                transposed.data[j][i] = self.data[i][j]
        return transposed

    def matrix_multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Dimensiuni incorecte.")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                for k in range(self.cols):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    # method that allows iterating through all elements an apply a transformation over them
    def apply(self, func):
        for i in range(self.rows):
            for j in range(self.cols):
                self.data[i][j] = func(self.data[i][j])

    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.data])

def ex3():
    matrix1 = Matrix(2, 2)
    matrix2 = Matrix(2, 2)
    matrix1.set(0, 0, 1)
    matrix1.set(0, 1, 2)
    matrix1.set(1, 0, 3)
    matrix1.set(1, 1, 4)
    matrix2.set(0, 0, 7)
    matrix2.set(0, 1, 8)
    matrix2.set(1, 0, 11)
    matrix2.set(1, 1, 12)
    print("Exemplu inmultire:")
    result = matrix1.matrix_multiply(matrix2)
    print(result)
    matrix1.apply(lambda x: x * 2)
    print("\nExemplu aplicare functie lambda:")
    print(matrix1)
    print("\nExemplu transpusa:")
    print(matrix1.transpose())
ex3()