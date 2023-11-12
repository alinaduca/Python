import math
# 1. Create a class hierarchy for shapes, starting with a base class Shape. Then, create subclasses like Circle,
# Rectangle, and Triangle. Implement methods to calculate area and perimeter for each shape.

#Ex 1
class Shape:
    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_perimeter(self):
        return self.a + self.b + self.c

    def calculate_area(self):
        #Am folosit formula lui Heron:
        #A = radical(p(p-a)(p-b)(p-c)), unde p este semiperimetrul
        semiperimeter = self.calculate_perimeter() / 2
        return math.sqrt(semiperimeter * (semiperimeter - self.a) * (semiperimeter - self.b) * (semiperimeter - self.c))

def ex1():
    circle = Circle(5)
    print("Cerc - Area:", circle.calculate_area())
    print("Cerc - Perimeter:", circle.calculate_perimeter())

    rectangle = Rectangle(4, 6)
    print("Dreptunghi - Area:", rectangle.calculate_area())
    print("Dreptunghi - Perimeter:", rectangle.calculate_perimeter())

    triangle = Triangle(3, 4, 5.3)
    print("Triunghi - Area:", triangle.calculate_area())
    print("Triunghi - Perimeter:", triangle.calculate_perimeter())
# ex1()



# 2. Design a bank account system with a base class Account and subclasses SavingsAccount and CheckingAccount. Implement methods
# for deposit, withdrawal, and interest calculation.

#Ex 2
class Account:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds.")

    def interest(self):
        pass


class SavingsAccount(Account):
    def __init__(self, account_holder, balance=0, interest_rate=0.02):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest calculated: ${interest}")


class CheckingAccount(Account):
    def __init__(self, account_holder, balance=0, overdraft_limit=100):
        super().__init__(account_holder, balance)
        self.overdraft_limit = overdraft_limit

    def withdrawal(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrawal ${amount}. New balance: ${self.balance}")
        else:
            print("Transaction declined. Overdraft limit exceeded.")

def ex2():
    savings_account = SavingsAccount("Alina Duca", balance=1000)
    savings_account.deposit(500)
    savings_account.interest()
    savings_account.withdrawal(200)

    checking_account = CheckingAccount("Duca Alina", balance=500, overdraft_limit=200)
    checking_account.deposit(100)
    checking_account.withdrawal(700)
# ex2()



# 3. Create a base class Vehicle with attributes like make, model, and year, and then create subclasses for specific types of
# vehicles like Car, Motorcycle and Truck. Add methods to calculate mileage or towing capacity based on the vehicle type.

#Ex 3
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self):
        pass

    def calculate_towing_capacity(self):
        pass

    def __str__(self):
        return self.make + " " + self.model + " " + str(self.year)


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self):
        mileage = (2023 - self.year) * 568 + ord(self.model[1]) * 2 + ord(self.make[0]) * 3
        return mileage

    def calculate_towing_capacity(self):
        return ord(self.make[0]) * 1.5 + (2023 - self.year) * 1.25


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self):
        mileage = (2023 - self.year) * 284 + ord(self.model[0]) * 4
        return mileage

    def calculate_towing_capacity(self):
        return ord(self.make[0]) / 3 + (2023 - self.year) * 0.75


class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self):
        mileage = (2023 - self.year) * 1000
        return mileage

    def calculate_towing_capacity(self):
        towing_capacity = (2023 - self.year) * 10
        return towing_capacity


def ex3():
    car = Car("Toyota", "Camry", 2022)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021)
    truck = Truck("Ford", "F-150", 2020)

    print(car)
    print("Maximum towing capacity:", car.calculate_towing_capacity())
    print("Car mileage:", car.calculate_mileage())
    print()

    print(motorcycle)
    print("Maximum towing capacity:", motorcycle.calculate_towing_capacity())
    print("Motorcycle mileage:", motorcycle.calculate_mileage())
    print()

    print(truck)
    print("Maximum towing capacity:", truck.calculate_towing_capacity())
    print(f"Truck mileage:", truck.calculate_mileage())
# ex3()



# 4. Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like Manager,
# Engineer and Salesperson. Each subclass should have attributes like salary and methods related to their roles.

#Ex 4
class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def display_info(self):
        print(f"Employee name: {self.name} with ID: {self.employee_id}")

    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, employee_id, salary, bonus):
        super().__init__(name, employee_id, salary)
        self.bonus = bonus

    def display_info(self):
        super().display_info()
        print(f"Position: Manager\nSalary: ${self.salary}\nBonus: ${self.bonus}")

    def calculate_salary(self):
        return self.salary + self.bonus


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, level):
        super().__init__(name, employee_id, salary)
        self.level = level

    def display_info(self):
        super().display_info()
        print(f"Position: Engineer\nSalary: ${self.salary}\nLevel: {self.level}")

    def calculate_salary(self):
        return self.salary


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary):
        super().__init__(name, employee_id, salary)

    def display_info(self):
        super().display_info()
        print(f"Position: Salesperson\nSalary: ${self.salary}")

    def calculate_salary(self):
        return self.salary


def ex4():
    manager = Manager("Alina Duca", 1, salary=8000, bonus=2000)
    manager.display_info()
    print(f"Total Salary: ${manager.calculate_salary()}\n")

    engineer = Engineer("Alina Luca", 2, salary=7000, level="Senior")
    engineer.display_info()
    print(f"Total Salary: ${engineer.calculate_salary()}\n")

    salesperson = Salesperson("Alice Duca", 3, salary=6000)
    salesperson.display_info()
    print(f"Total Salary: ${salesperson.calculate_salary()}")
# ex4()



# 5. Create a class hierarchy for animals, starting with a base class Animal. Then, create subclasses like Mammal, Bird and Fish.
# Add properties and methods to represent characteristics unique to each animal group.

#Ex 5
class Animal:
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def display_info(self):
        print(f"Name: {self.name}\nHabitat: {self.habitat}")


class Mammal(Animal):
    def __init__(self, name, habitat, fur_color, nr_legs):
        super().__init__(name, habitat)
        self.fur_color = fur_color
        self.nr_legs = nr_legs

    def display_info(self):
        super().display_info()
        print(f"Type: Mammal\nFur Color: {self.fur_color}\nNr. of legs: {self.nr_legs}")

    def get_nr_legs(self):
        return self.nr_legs


class Bird(Animal):
    def __init__(self, name, habitat, can_fly=True):
        super().__init__(name, habitat)
        self.can_fly = can_fly

    def display_info(self):
        super().display_info()
        print(f"Type: Bird\nCan fly: {self.can_fly}")

    def get_can_fly(self):
        return self.can_fly


class Fish(Animal):
    def __init__(self, name, habitat, water_type):
        super().__init__(name, habitat)
        self.water_type = water_type

    def display_info(self):
        super().display_info()
        print(f"Type: Fish\nWater Type: {self.water_type}")

    def get_water_type(self):
        return self.water_type


def ex5():
    mammal = Mammal("Lion", "Grasslands", "Golden", nr_legs=4)
    mammal.display_info()
    print(mammal.get_nr_legs())

    bird = Bird("Penguin", "Antarctica", can_fly=False)
    bird.display_info()
    print(bird.get_can_fly())

    fish = Fish("Pollack", "Ocean", water_type="Saltwater")  # cod negru
    fish.display_info()
    print(fish.get_water_type())
# ex5()



# 6. Design a library catalog system with a base class LibraryItem and subclasses for different types of items like Book, DVD
# and Magazine. Include methods to check out, return and display information about each item.

#Ex 6
class LibraryItem:
    def __init__(self, title, item_id, available=True):
        self.title = title
        self.item_id = item_id
        self.available = available

    def display_info(self):
        print(f"Item ID: {self.item_id}, title: {self.title}, available: {'Yes' if self.available else 'No'}")

    def check_out(self):
        if self.available:
            print(f"{self.title} checked out successfully.")
            self.available = False
        else:
            print(f"{self.title} is not available for checkout.")

    def return_item(self):
        if not self.available:
            print(f"{self.title} returned successfully.")
            self.available = True
        else:
            print(f"{self.title} was not checked out.")


class Book(LibraryItem):
    def __init__(self, title, item_id, author, nr_pages, available=True):
        super().__init__(title, item_id, available)
        self.author = author
        self.nr_pages = nr_pages

    def display_info(self):
        super().display_info()
        print(f"Author: {self.author}, number of Pages: {self.nr_pages}\n")


class DVD(LibraryItem):
    def __init__(self, title, item_id, running_time, available=True):
        super().__init__(title, item_id, available)
        self.running_time = running_time

    def display_info(self):
        super().display_info()
        print(f"Running time: {self.running_time} minutes\n")


class Magazine(LibraryItem):
    def __init__(self, title, item_id, issue_date, available=True):
        super().__init__(title, item_id, available)
        self.issue_date = issue_date

    def display_info(self):
        super().display_info()
        print(f"Issue date: {self.issue_date}\n")


def ex6():
    book = Book("The Great Gatsby", 101, "F. Scott Fitzgerald", 180)
    dvd = DVD("Inception", 201, 148)
    magazine = Magazine("National Geographic", 301, "October 2023")

    book.display_info()
    dvd.display_info()
    magazine.display_info()
    print()

    book.check_out()
    dvd.check_out()
    magazine.check_out()
    print()

    book.return_item()
    dvd.return_item()
    magazine.return_item()
ex6()