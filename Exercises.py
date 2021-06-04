# Exercise 1: Given two integer numbers return their product.
# If the product is greater than 1000, then return their sum
def exercise1():
    while True:
        try:
            number1 = int(input("Enter first number: "))
            number2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Try again.\n")
            continue
        else:
            break
    product = number1 * number2
    sum = number1 + number2
    if product > 1000:
        return sum
    else:
        return product
# Remove comment below to run exercise1
# print("The results is", exercise1())

# Exercise 2: Given a range of the first 10 numbers, Iterate from the
# start number to the end number, and In each iteration print
# the sum of the current number and previous number
def exercise2(number):
    print("Printing current and previous number sum in a range(", number, ")")
    previous_number = 0
    for index in range(number):
        sum = index + previous_number
        print("Current Number", index, "Previous Number", previous_number, "Sum:", sum)
        previous_number = index

# Remove comment below to run exercise2
# exercise2(10)

# Exercise 3: Given a string, display only those characters
# which are present at an even index number.
def exercise3(word):
    for index in range(0, len(word), 2):
        print(word[index])

# Remove comment below to run exercise3
# exercise3("pynative")

# Exercise 4: Given a string and an integer number n, remove characters from
# a string starting from zero up to n and return a new string
# Note: n must be less than the length of the string.
def exercise4(word, num):
    # Slice string in python: https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
    return word[num:]

# Remove comment below to run exercise4
# print(exercise4("pynative", 4))

# Exercise 5: Given a list of numbers,
# return True if first and last number of a list is same
def exercise5():
    list_of_numbers = [10, 20, 30, 40, 10]
    if list_of_numbers[0] != list_of_numbers[-1]:
        return False
    return True

# Remove comment below to run exercise5
# print(exercise5())

#Exercise 6: Given a list of numbers, Iterate it and print
# only those numbers which are divisible of 5
def exercise6():
    list_of_numbers = [10, 20, 33, 46, 55]
    print("Given list is", list_of_numbers, "\nDivisible of 5 in a list")
    for value in list_of_numbers:
        if value % 5 == 0:
            print(value)
# Remove comment below to run exercise6
# exercise6()

#Exercise 7: Return the count of sub-string “Emma”
# appears in the given string
def exercise7():
    str = "Emma is good developer. Emma is a writer"
    print("Emma appeared", str.count("Emma"), "times")

# Remove comment below to run exercise7
# exercise7()

# Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
def exercise8(num):
    for index in range(num):
        for i in range(index):
            print(index, end=" ") # print number end= "" means no next line
        print("\n", end=" ") # print new line for next index pattern
    # remove comment for alternative solution
    #for i in range(num):
     #   i = str(i) * i
      #  print(i)

# Remove comment below to run exercise8
#exercise8(6)

# Exercise 9: Reverse a given number and return true
# if it is the same as the original number
def exercise9(num):
    if str(num) != str(num)[::-1]: #original string compared to reversed string
        return False
    return True
# Remove comment below to run exercise9
#print(exercise9(121))

#Exercise 10: Given a two list of numbers create a new list such that
# new list should contain only odd numbers from the first list
# and even numbers from the second list
def exercise10():
    list1 = [10, 20, 23, 11, 17]
    list2 = [13, 43, 24, 36, 12]
    new_list = []
    for num in list1:
        if (num % 2) != 0:
            new_list.append(num)
    for num in list2:
        if (num % 2) == 0:
            new_list.append(num)
    return new_list
# Remove comment below to run exercise10
#print(exercise10())

#Exercise 11: Write a code to extract each digit from an integer,
# in the reverse order with a space separating the digits.
def exercise11(num):
    # print in reverse
    # print(str(num)[::-1])

    # print in reverse with spaces in between
    #value = str(num)
    #length = len(value)
    #reverse = -1
    #for index in range(length):
    #    print(value[reverse], end=" ")
    #    reverse -= 1

    #shorter code
    reverse = -1
    for index in range(len(str(num))):  # loop in range of string length
        print(str(num)[reverse], end=" ")  # print using negative index
        reverse -= 1  # decrement to next negative index
# Remove comment below to run exercise11
#exercise11(7536)

# Exercise 12: Calculate income tax for the given income
# by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20
def exercise12(salary):
    tax = 0  # default tax is 0 for salary 10K and below
    if salary > 20000:  # salary more than 20K is 1000 + 20% of salary exceeding 20K
        tax = (salary-20000) * 0.2 + 1000  # 1000 is 10% of 10000
    elif salary > 10000:  # salary more than 10K is 10% of salary exceeding 10K
        tax = (salary-10000) * 0.1
    return tax

# Remove comment to run exercise12
#print(exercise12(45000))

# Exercise 13: Print multiplication table form 1 to 10
def exercise13(num):
    for index in range(1, num+1):
        for i in range(1, 11):
            print(index * i, end=" ")
        print("\t\t")

# Remove comment to run exercise13
#exercise13(10)

# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
def exercise14(num):
    for index in reversed(range(num+1)):
        for i in range(index):
            print("*", end=" ")
        print("\n", end="")

# Remove comment below to run exercise14
#exercise14(5)

# Exercise 15: Write a function called exponent(base, exp) that returns
# an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.
def exponent(base, exp):
    # built-in by python exponent function
    #base = base**exp

    # own logic
    old_base = base
    for index in range(exp-1):
        base = base * old_base
    return base
# Remove comment below to run exponent function
#print(exponent(2, 5))