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


class Person:
    def __init__(self, name, age=18):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name} and Age : {self.age}")


p1 = Person("Shyam", 23)
p1.display()
p2 = Person("Manan")
p2.display()
p3 = Person("Ram", 22)
p3.display()


class Person:
    def __init__(self, name, age, city, country):
        self.name = name
        self.age = age
        self.city = city
        self.country = country


p1 = Person("Ram", 30, "Ahm", "India")

print(p1.name)
print(p1.age)
print(p1.city)
print(p1.country)
