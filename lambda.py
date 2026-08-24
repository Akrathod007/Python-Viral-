# def add(x, y):
#     return x + y


# print(add(10, 20))
"""
add = lambda x, y: x + y
print(add(10, 20))

evenOdd = lambda x: "Even" if x % 2 == 0 else "Odd"

print(evenOdd(10))
print(evenOdd(11))

check = lambda n: "Positive" if n > 0 else "Negative" if n < 0 else "Zero"
print(check(10))
print(check(-10))
print(check(0))


login = lambda user, pwd: (
    "Admin Login"
    if user == "admin" and pwd == "xyz"
    else "User Login" if user == "user" and pwd == "abc" else "Invalid User"
)

print(login("admin", "xyz"))
print(login("user", "abc"))
print(login("user", "123"))

"""

# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# x = list(map(lambda x: x * 2, li))
# print(x)


# def demo(n):
#     return n * 2


# x = list(map(demo, li))
# print(x)

# l2 = [45, 67, 89, 22, 34, 56, 44, 35, 31]
# evenOdd = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", li))
# evenOdd = list(map(lambda x: "Even" if x % 2 == 0 else "Odd", l2))
# print(evenOdd)
# marks = [98, 78, 68, 56, 86, 79, 92, 40, 58, 68, 72]
# grade = list(
#     map(
#         lambda x: (
#             "Grade A"
#             if x >= 90
#             else (
#                 "Grade B"
#                 if x >= 80
#                 else (
#                     "Grade C"
#                     if x >= 70
#                     else "Grade D" if x >= 60 else "Grade E" if x >= 50 else "Grade F"
#                 )
#             )
#         ),
#         marks,
#     )
# )
# print(grade)


# fruits = ["apple", "banana", "kiwi", "mango", "watermelon"]

# rev = list(map(lambda x: x[::-1], fruits))
# print(rev)


# li = [34, 56, 77, 89, 70, 45, 67, 33, 46, 78]

# even = list(filter(lambda x: x % 2 == 0, li))
# print(even)

# odd = list(filter(lambda x: x % 2 != 0, li))
# print(odd)

# x = list(filter(lambda x: x % 3 == 0, li))
# print(x)


# fruits = ["Apple", "Banana", "Kiwi", "Mango", "Watermelon"]

# x = list(filter(lambda f: len(f) > 5, fruits))
# print(x)

# from functools import reduce

# li2 = [1, 2, 3, 4, 5]

# total = reduce(lambda x, y: x + y, li2)
# print(total)

# total = reduce(lambda x, y: x + y, li2, 100)
# print(total)

# # maximum = reduce(lambda x, y: x if x > y else y, li)
# maximum = reduce(lambda x, y: x if x > y else y, li, li[0])
# print(maximum)

# minimum = reduce(lambda x, y: x if x < y else y, li, li[0])
# print(minimum)

# Find Sum of Square of Even Numbers

from functools import reduce

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, li))
print(even)

square = list(map(lambda x: x * x, even))
print(square)

finalSum = reduce(lambda x, y: x + y, square)
print(finalSum)


# 1. Square Even Numbers and Find Sum

# 2. Sum of Cubes of Positive Numbers

# 3. Find Sum of Squares of Odd Numbers

# 4. Find Largest Square of Even Numbers

# 5. Reverse Long Words and Join
# Filter words whose length is greater than 4.
