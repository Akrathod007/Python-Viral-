# class Animal:
#     def eat(self):
#         print("Animal eat food")


# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks")


# d = Dog()
# d.bark()
# d.eat()


# 1) Single Inheritance : A child class inherits from one parent class.


# class Person:
#     def display(self):
#         print("This is Person Class")


# class Student(Person):
#     def show(self):
#         print("This is Student Class")


# s1 = Student()
# s1.show()
# s1.display()


# 2) Multiple Inheritance : A child class inherits from more than one parent class.


# class Father:
#     def skill1(self):
#         print("Driving")


# class Mother:
#     def skill2(self):
#         print("Cooking")


# class Child(Father, Mother):
#     def skill3(self):
#         print("Playing")


# c = Child()

# c.skill1()
# c.skill2()
# c.skill3()


# 3) Multilevel Inheritance : A class inherits from a class that already inherited from another class.


# class Grandfather:
#     def house(self):
#         print("Grandfather's house")


# class Father(Grandfather):
#     def car(self):
#         print("Father's car")


# class Son(Father):
#     def bike(self):
#         print("Son's bike")


# s = Son()

# s.house()
# s.car()
# s.bike()

# 4) Hierarchical Inheritance : Multiple child classes inherit from the same parent class.


# class Animal:
#     def eat(self):
#         print("Animal Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Dog's Bark")


# class Cat(Animal):
#     def meow(self):
#         print("Cat's Meow")


# d = Dog()
# c = Cat()

# d.eat()
# d.bark()

# c.eat()
# c.meow()


# 5) Hybrid Inheritance : A combination of multiple types of inheritance.


# class Vehicle:
#     def run(self):
#         print("Vehicle Running")


# class SportsCar(Vehicle):
#     def speed(self):
#         print("SportsCar Speed")


# class NormalCar(Vehicle):
#     def AC_on(self):
#         print("NormalCar AC On")


# class ElectricCar(SportsCar, NormalCar):
#     def charge(self):
#         print("ElectricCar Charge")


# e = ElectricCar()
# e.charge()
# e.AC_on()
# e.speed()
# e.run()


class Animal:
    def sound(self):
        print("Animal make sound")


class Dog(Animal):
    def sound(self):
        # print("Dog Barks")
        super().sound()


d = Dog()
d.sound()


class Person:

    def __init__(self, name):
        self.name = name


class Student(Person):

    def __init__(self, name, marks):
        super().__init__(name)
        self.marks = marks


s = Student("Ansh", 95)

print(s.name)
print(s.marks)
