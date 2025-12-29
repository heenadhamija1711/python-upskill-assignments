#
# 1. Define a class Person with attributes name and age. Create an instance of this class and print its attributes.
#

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an instance
person1 = Person("Alice", 25)

# Print attributes
print("Name:", person1.name)
print("Age:", person1.age)

# 2. Problem: Write a Python class named BankAccount with attributes like account_number, balance, and customer_name, and methods like deposit, withdraw, and check_balance.

class BankAccount:
    def __init__(self, account_number, customer_name, balance=0.0):
        self.account_number = account_number
        self.customer_name = customer_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive")
        elif amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        print(f"Account balance: {self.balance}")


#
# 3. Create a class Book with a class method from_string() that creates a Book instance from a string. And print both attributes of the class
#
# book = Book.from_string("Python Programming, John Doe")
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split(", ")
        return cls(title, author)

# Create Book object using class method
book = Book.from_string("Python Programming, John Doe")

# Print attributes
print("Title:", book.title)
print("Author:", book.author)

#
# 4. Create a base class Animal with a method sound(). Create subclasses Dog and Cat that overrides the sound() method and call those methods.

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Create objects
animal = Animal()
dog = Dog()
cat = Cat()

# Call methods
animal.sound()
dog.sound()
cat.sound()

#
# 5. Write a code to perform multiple inheritance.
#
#
#
#
class Father:
    def skills(self):
        print("Father: Driving")

class Mother:
    def skills(self):
        print("Mother: Cooking")

class Child(Father, Mother):
    pass

# Create object of Child
child = Child()

# Call method
child.skills()
