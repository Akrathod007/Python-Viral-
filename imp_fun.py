def sayHi():
    print("Hello Hi")


def mul(a, b):
    return a * b


def maxOfList(li):
    max = li[0]

    for i in li:
        if i > max:
            max = i

    return max


def prime(n):
    f = 0
    for i in range(1, n + 1):
        if n % i == 0:
            f += 1

    if f == 2:
        print("Prime")
    else:
        print("Not Prime")
