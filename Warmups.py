# 12.4.17
# Write a Python program
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space between them.


# def reverse_order(first_name, last_name):
#     # print("%s %s" % (last_name, first_name))
#     print(last_name + " " + first_name)
#
#     reverse_order("Nancy", "Aguilar")


# def reverse_order():
#     first_name = input("First name")
#     last_name = input("Last name")
#     print("%s, %s" % (last_name, first_name))

# 12.5.17
"""Write a function called add_py
that takes one parameter called "name"
and prints out name.py
example:
add_py("I_eat") == "I_eat.py"
"""

# def add_py(name):
#     print("%s.py" % name)  #Solution 1
#     print(name + ".py")  #Solution 2
#
#
# """Write a function called "add"
# which takes three parameters
# and prints the sum of the numbers
# """
#

# def add(num1, num2, num3):
#     print(num1 + num2 + num3)
#
#
# add(1, 2, 3)


# def repeat(string):
#     print(string)
#     print(string)
#     print(string)
#
#     for times in range(3):
#         print(string)
#
#
# repeat("Hello")

"""
Write a function called "date"
that takes in three parameters
"month", "day", and "year" and
prints out the date, separated by a "/"

example:
date("12, "8", "17" == "12/8/17"
Expert mode:
date(12,8,17) == "12/8/17"
"""


def date(day, month, year):
    print(day + "/" + month + "/" + year)


date("12", "8", "17")


def date(day, month, year):
    print(str(day) + "/" + str(month) + "/" + str(year))


date(12, 8, 17)