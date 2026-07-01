#class Animal:
#     pass

# class Dog(Animal):
#     pass

#class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

# d = Dog("Tom")
# print(d.name)



# class Animal:
#     def sound(self):
#         print("Animal Sound")

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# Dog().sound()

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def get_bonus(self):
#         return self.salary * 0.10

# class Intern(Employee):
#     def get_bonus(self):
#         return 500

# print(Intern("Carol", 30000).get_bonus())

# class Animal:
#     def speak(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def speak(self):
#         super().speak()
#         print("Dog barks")

# Dog().speak()

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side ,side)

# s = Square(5)
# print(s.length, s.width)

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass


# class A:
#     def hello(self):
#         print("A")

# class B(A):
#     def hello(self):
#         print("B")

# class C(A):
#     def hello(self):
#         print("C")

# class D(C,B):
#     pass

# D().hello()


# class Rectangle:
#     def __init__(self, l, w):
#         self.l = l
#         self.w = w

#     def area(self):
#         return self.l * self.w

# class Square(Rectangle):
#     def __init__(self, side):
#         super().__init__(side, side)

# def print_area(shape):
#     if isinstance(shape, Rectangle):
#         print(shape.area())
#     else:
#         print("Unknown shape")

# r = Rectangle(5, 7)
# s = Square(6)

# print_area(r)
# print_area(s)
# print_area("Hello")