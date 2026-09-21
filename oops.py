# class Student:
#     name = ""
#     age = 0

#     def display(self):
#         print(f"Name : {self.name} and Age : {self.age}")


# s1 = Student()
# s1.name = "Ram"
# s1.age = 22
# s1.display()

# s2 = Student()
# s2.name = "Shyam"
# s2.age = 24
# s2.display()

# s3 = Student()
# s3.name = "Manan"
# s3.age = 20
# s3.display()


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name : {self.name} and Age : {self.age}")


# p1 = Person("Shyam", 23)
# p1.display()
# p2 = Person("Manan", 21)
# p2.display()
# p3 = Person("Ram", 22)
# p3.display()


# class Person:
#     def __init__(self, name, age=18):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name : {self.name} and Age : {self.age}")


# p1 = Person("Shyam", 23)
# p1.display()
# p2 = Person("Manan")
# p2.display()
# p3 = Person("Ram", 22)
# p3.display()


# class Person:
#     def __init__(self, name, age, city, country):
#         self.name = name
#         self.age = age
#         self.city = city
#         self.country = country


# p1 = Person("Ram", 30, "Ahm", "India")

# print(p1.name)
# print(p1.age)
# print(p1.city)
# print(p1.country)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)


p1 = Person("Shinchan", 5)
p1.greet()


class Person:
    def __init__(self, name):
        self.name = name

    def printname(self):
        print(self.name)


p1 = Person("Doremon")
p2 = Person("Shinchan")

p1.printname()
p2.printname()


class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def greet(abc):
        print("Hello, my name is " + abc.name)


p1 = Person("Emil", 36)
p1.greet()


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")


car1 = Car("BenZ", "Maybec", 2020)
car1.display_info()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return "Hello, " + self.name

    def welcome(self):
        message = self.greet()
        print(message + "! Welcome")


p1 = Person("Tilak")
p1.welcome()
