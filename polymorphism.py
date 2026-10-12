class Math:
    def add(self, a, b, c=0, d=0):
        return a + b + c + d


m = Math()
print(m.add(10, 20))
print(m.add(10, 20, 30))
print(m.add(10, 20, 30, 40))


class Animal:

    def sound(self):
        print("Animals make sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


class Cat(Animal):

    def sound(self):
        print("Cat meows")


d = Dog()
c = Cat()

d.sound()
c.sound()


class Dog:
    def sound(self):
        print("Dog barks")


class Cat:
    def sound(self):
        print("Cat meows")


def make_sound(animal):
    animal.sound()


d = Dog()
c = Cat()

make_sound(d)
make_sound(c)


class Circle:
    def area(self):
        print("Area of Circle")


class Rectangle:
    def area(self):
        print("Area of Rectangle")


class Triangle:
    def area(self):
        print("Area of Triangle")


shapes = [Circle(), Rectangle(), Triangle()]

for s in shapes:
    s.area()
