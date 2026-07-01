# Q1.
# class Animal:
#     def __init__(self, name, sound):
#         self.name = name
#         self.sound = sound

#     def speak(self):
#         print(f"{self.name} says {self.sound}!")


# class Dog(Animal):
#     def fetch(self):
#         print(f"{self.name} fetches the ball!")


# dog = Dog("Rex", "Woof")
# dog.speak()
# dog.fetch()

# Q2.
# class Vehicle:
#     def __init__(self, brand, speed):
#         self.brand = brand
#         self.speed = speed
# class ElectricCar(Vehicle):
#     def __init__(self, brand, speed, battery):
#         super().__init__(brand, speed)
#         self.battery = battery
#     def describe(self):
#         print(f"Brand: {self.brand}")
#         print(f"Speed: {self.speed} km/h")
#         print(f"Battery: {self.battery} kWh")
# car = ElectricCar("BMW", 450, 750)
# car.describe()

# Q3.
# class Employee:
#     def __init__(self, salary):
#         self.salary = salary
#     def get_bonus(self):
#         return self.salary * 0.10
    
# class Manager(Employee):
#     def get_bonus(self):
#         return self.salary * 0.25
    
# class Intern(Employee):
#     def get_bonus(self):
#         return 500
# e = Employee(40000)
# m = Manager(60000)
# i = Intern(10000)

# print("Employee",e.get_bonus())
# print( "Manager",m.get_bonus())
# print("intern", i.get_bonus())

# Q4.

# class Shape:
#     def area(self):
#         return 0

#     def info(self):
#         print("Area:", self.area())

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius * self.radius

# r = Rectangle(5, 6)
# c = Circle(6)

# r.info()
# c.info()

# Q5.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def area(self):
#         return self.width * self.height


# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)


# sq = Square(10)
# print("Area of Square:", sq.area())

# Q6.

# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount
#         print(f"Deposited: {amount}")
#         print(f"Current Balance: {self.balance}")

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")
#             print(f"Current Balance: {self.balance}")
#         else:
#             print("Insufficient balance")


# class SavingsAccount(BankAccount):
#     def __init__(self, balance, min_balance):
#         super().__init__(balance)
#         self.min_balance = min_balance

#     def withdraw(self, amount):
#         if self.balance - amount >= self.min_balance:
#             self.balance -= amount
#             print(f"Withdrawn: {amount}")
#             print(f"Current Balance: {self.balance}")
#         else:
#             print("Withdrawal denied! Minimum balance must be maintained.")

# acc = SavingsAccount(5000, 1000)

# acc.deposit(2000)
# acc.withdraw(3000)
# acc.deposit(1000)
# acc.withdraw(3500)

# Q7.

# from datetime import datetime

# class Logger:
#     def log(self, msg):
#         print(msg)


# class TimestampLogger(Logger):
#     def log(self, msg):
#         current_time = datetime.now().strftime("%H:%M:%S")
#         new_msg = f"[{current_time}] {msg}"
#         super().log(new_msg)  

# logger = Logger()
# logger.log("System started")

# logger = TimestampLogger()
# logger.log("User logged in")

# Q8.

# class Flyable:
#     def fly(self):
#         print("Duck can fly")

# class Swimmable:
#     def swim(self):
#         print("Duck can swim")

# class Duck(Flyable, Swimmable):
#     def quack(self):
#         print("Duck says Quack!")

# d = Duck()
# d.fly()
# d.swim()
# d.quack()

# Q9.

# class A:
#     def hello(self):
#         print("Hello from A")

# class B(A):
#     def hello(self):
#         print("Hello from B")

# class C(A):
#     def hello(self):
#         print("Hello from C")

# class D(B, C):
#     pass

# obj = D()
# obj.hello()

# print(D.__mro__)

# Q10.
# import json

# class JSONMixin:
#     def to_json(self):
#         return json.dumps(self.__dict__)


# class User(JSONMixin):
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email


# user = User("Nikhil", "nikhil@gmail.com")
# print(user.to_json())

# Q11.
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_id = student_id

#     def __str__(self):
#         return f"Name: {self.name}, Age: {self.age}, ID: {self.student_id}"


# s = Student("Nikhil", 22, 808)
# print(s)

# Q12





# Q13

# class Account:
#     pass


# class PremiumAccount(Account):
#     pass


# print(issubclass(PremiumAccount, Account))
# print(issubclass(Account, PremiumAccount))

# Q14

# class Shape:
#     def area(self):
#         return 0


# class Rectangle(Shape):
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w

#     def area(self):
#         return self.l * self.w


# class Triangle(Shape):
#     def __init__(self, b, h):
#         self.b = b
#         self.h = h

#     def area(self):
#         return 0.5 * self.b * self.h


# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * self.r


# shapes = [Rectangle(4, 5), Triangle(6, 3), Circle(2)]

# for shape in shapes:
#     print(shape.area())

# Q15

# class Counter:
#     count = 0

#     def __init__(self):
#         Counter.count += 1


# class NamedCounter(Counter):
#     pass


# c1 = Counter()
# c2 = NamedCounter()
# c3 = NamedCounter()

# print( Counter.count)

# Q16

# class Employee:
#     def __init__(self, salary):
#         self.salary = salary

#     def raise_salary(self, pct):
#         self.salary += self.salary * pct / 100


# class Manager(Employee):
#     def raise_salary(self, pct):
#         super().raise_salary(pct)
#         self.salary += 1000


# m = Manager(50000)
# m.raise_salary(10)
# print(m.salary)

# Q17

# class Payment:
#     def pay(self, amount):
#         raise NotImplementedError


# class CreditCard(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card")


# class PayPal(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal")


# c = CreditCard()
# p = PayPal()

# c.pay(5000)
# p.pay(1000)

# Q18

# class Vehicle:
#     def start(self):
#         print("Vehicle started")


# class Car(Vehicle):
#     pass


# class Motorcycle(Vehicle):
#     pass


# def test_drive(vehicle):
#     if isinstance(vehicle, Vehicle):
#         vehicle.start()
#     else:
#         raise TypeError


# test_drive(Car())

# Q19