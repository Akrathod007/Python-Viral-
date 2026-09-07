"""import math

print(math.pi)
print(math.e)
print(math.pow(3, 3))
print(math.sqrt(36))
print(math.ceil(4.6))
print(math.floor(4.6))
print(math.trunc(4.45345345))
print(round(4.3))
print(round(4.5))
print(round(4.6))
print(round(43.56756))
print(round(43.56756, 2))
print(math.gcd(18, 12))
print(math.lcm(18, 12))
print(math.factorial(10))

# 18 -> 1,2,3,6,9,18
# 12 -> 1,2,3,4,6,12

print(math.fabs(-4.5))
print(math.fmod(4.5, 1.2))

print(math.log(10))
print(math.log10(100))
print(math.log2(10))

x = float("inf")
y = float("-inf")
print(x > 10000000000000000000000000000000000000000000000000000000000000000)

"""

# import math as m

# print(m.pow(2, 10))

# from math import pow, sqrt as s

# print(pow(2, 20))
# print(s(25))

# from math import *

# print(pow(2, 30))


# import random as r

# print(r.random())
# print(r.randint(1, 6))
# print(r.randrange(1, 6, 2))

# colors = ["Red", "Green", "Blue"]
# print(r.choice(colors))
# print(r.choices(colors, k=5))

# numbers = [1, 2, 3, 4, 5]
# print(r.sample(numbers, 3))
# r.shuffle(numbers)
# print(numbers)

# print(round(r.uniform(1.1, 5.5), 2))

"""
1. Write a program to generate a 4-digit OTP.

2. Write a program to make Lottery Game :

Generate 5 random numbers (1 - 50).
li = [34,23,45,12,37]

Ask user to guess numbers.
for i in range(1,16):

    no = 55
    match = 1
Check how many matches.

3. Write a program to generate a random HEX color code like #A3F4C1.

4. Write a program to guess the Number Game

randomNo = 1 to 25 (18)

while True:
    no = 16 -> Too Low
    no -> 20 -> To High
    no = 18 -> Break
 
5. Write a program to make Rock Paper Scissors game

com = rock
user = paper

if com == user:
    draw

if (user == "R" and com == "S") or (user == "P" and com == "R") or (user == "S" and com == "p"):
    user win

"""


import datetime as dt

today = dt.date.today()
print(today)

now = dt.datetime.now()
print(now)

t = dt.date(2030, 12, 1)
print(t)

tm = dt.datetime(2027, 1, 1, 12, 12, 12, 12222)
print(tm)

print(today.year)
print(today.month)
print(today.day)

print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

print("-------------------------------------------")
print(now.strftime("%d"))
print(now.strftime("%m"))
print(now.strftime("%Y"))
print(now.strftime("%y"))
print(now.strftime("%A"))
print(now.strftime("%a"))
print(now.strftime("%B"))
print(now.strftime("%b"))
print(now.strftime("%H"))
print(now.strftime("%I"))
print(now.strftime("%p"))

print(now.strftime("%I:%M:%S.%f"))
print(now.strftime("%j"))
print(now.strftime("%U"))
print(now.strftime("%W"))
print(now.strftime("%c"))
print(now.strftime("%x"))
print(now.strftime("%X"))

new_date = now + dt.timedelta(days=5, hours=10)
print(new_date)


d1 = dt.date(2026, 2, 8)
d2 = dt.date(2026, 2, 1)

diff = d1 - d2
print(diff.days)

time_now = dt.datetime.now().time()
print(time_now)

date_string = "08-02-2026"
date_obj = dt.datetime.strptime(date_string, "%d-%m-%Y")

print(date_obj)
