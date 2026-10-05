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


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def greet(self):
#         print("Hello, my name is " + self.name)


# p1 = Person("Shinchan", 5)
# p1.greet()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def printname(self):
#         print(self.name)


# p1 = Person("Doremon")
# p2 = Person("Shinchan")

# p1.printname()
# p2.printname()


# class Person:
#     def __init__(myobject, name, age):
#         myobject.name = name
#         myobject.age = age

#     def greet(abc):
#         print("Hello, my name is " + abc.name)


# p1 = Person("Emil", 36)
# p1.greet()


# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print(f"{self.year} {self.brand} {self.model}")


# car1 = Car("BenZ", "Maybec", 2020)
# car1.display_info()


# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return "Hello, " + self.name

#     def welcome(self):
#         message = self.greet()
#         print(message + "! Welcome")


# p1 = Person("Tilak")
# p1.welcome()


# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f"Name : {self.name} and Age : {self.age}")


# s1 = Student("Ram", 23)
# s2 = Student("Shyam", 25)
# s1.display()
# s1.age = 25
# s1.display()

# del s1.age
# # s1.display()
# s2.display()


# class Person:
#     species = "Human"  # Class property

#     def __init__(self, name):
#         self.name = name  # Instance property


# p1 = Person("Hatori")
# p2 = Person("Doremee")

# print(p1.name)
# print(p2.name)
# print(p1.species)
# print(p2.species)

# Person.species = "Cartoon"
# print(p1.species)
# print(p2.species)


# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def multiply(self, a, b):
#         return a * b


# calc = Calculator()
# print(calc.add(5, 3))
# print(calc.multiply(4, 7))


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def celebrate_birthday(self):
#         self.age += 1
#         print(f"Happy birthday! You are now {self.age}")


# p1 = Person("Ram", 25)
# p1.celebrate_birthday()
# p1.celebrate_birthday()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Name : {self.name} and age : {self.age}"


s1 = Student("Ram", 22)
print(s1)

s2 = Student("Shyam", 25)
print(s2)


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)
        print(f"Added: {song}")

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)
            print(f"Removed: {song}")

    def show_songs(self):
        print(f"Playlist '{self.name}':")
        for song in self.songs:
            print(f"- {song}")


my_playlist = Playlist("Favorites")
my_playlist.add_song("Bohemian Rhapsody")
my_playlist.add_song("Stairway to Heaven")
my_playlist.show_songs()

party = Playlist("Party")
party.add_song("Party 1 Song")
party.add_song("Party 2 Song")
party.show_songs()
party.remove_song("Party 1 Song")
party.show_songs()


class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")


p1 = Person("Emil")

del Person.greet

# p1.greet()
