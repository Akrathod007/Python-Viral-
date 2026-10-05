# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks

#     def display(self):
#         print("Name : ", self.name)
#         print("Marks : ", self.__marks)

#     def setMarks(self, marks):
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invalid Marks")


# s1 = Student("Ram", 89)
# s2 = Student("Shyam", 70)

# s1.display()
# s2.display()

# # print(s1.__marks)
# # s1.setMarks(94)
# s1.setMarks(914)
# s1.display()


class Student:
    def __init__(self):
        self.__roll = 0
        self.__name = ""
        self.__marks = 0

    def setRoll(self, roll):
        self.__roll = roll

    def getRoll(self):
        return self.__roll

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setMarks(self, marks):
        self.__marks = marks

    def getMarks(self):
        return self.__marks


s1 = Student()
s1.setRoll(101)
s1.setName("Ram")
s1.setMarks(98)
print(s1.getRoll())
print(s1.getName())
print(s1.getMarks())
s2 = Student()
s2.setRoll(102)
s2.setName("Shyam")
s2.setMarks(78)
print(s2.getRoll())
print(s2.getName())
print(s2.getMarks())
