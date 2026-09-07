# print("Start")
# print(10 / 0)
# print("End")


# print("Start")

# try:
#     print(10 / 0)
#     #
#     #
# except:
#     print("Error")

# print("End")


# try:
#     print("Start")
#     print(10 / 0)
#     print("End")
# except:
#     print("Error Found")

# print("Program Continues")


# try:
#     num = int(input("Enter Number: "))
#     print(10 / num)

# except ZeroDivisionError:
#     print("Cannot divide by zero")

# except ValueError:
#     print("Enter valid integer")

try:
    num = int(input("Enter Number: "))
    print(10 / num)

except (ValueError, ZeroDivisionError):
    print("Invalid Input")
