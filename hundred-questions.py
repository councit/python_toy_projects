# # Question: 1
# # Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# for number in range(2000, 3201):
#     if (number % 7 == 0 and number % 5 != 0):
#         print(number, end=', ')

# # Question: 2
# # Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320


# def print_factorial(number):
#     li = list(range(number))
#     result = 1
#     for num in li:
#         result *= (num + 1)
#     return print(result)


# print_factorial(8)

# # Question: 3
# # With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

# # Then, the output should be:

# # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# def make_dict(number):
#     key_list = []
#     value_list = []
#     master_list = zip(key_list, value_list)

#     for index in range(number):
#         key_list.append(index + 1)
#         value_list.append((index+1)**2)
#     print(dict(master_list))


# make_dict(8)

# # Question 4
# # Question:
# # Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# # 34,67,55,33,12,98
# # Then, the output should be:

# # ['34', '67', '55', '33', '12', '98']
# # ('34', '67', '55', '33', '12', '98')

# user_numbers = input("Please enter numbers to add to a list and tuple.")
# li = user_numbers.split(',')
# tupe = tuple(li)

# print(li, tupe)

# # Question 5
# # Question:
# # Define a class which has at least two methods:

# # getString: to get a string from console input
# # printString: to print the string in upper case.
# # Also please include simple test function to test the class methods.

# class StringTalker():
#     def _init_(self):
#         pass

#     def getString(self):
#         self.user_string = input("Please enter a string.")

#     def printString(self):
#         print(self.user_string.upper())


# myTest = StringTalker()
# myTest.getString()
# myTest.printString()

# Question 6
# Question:
# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 * C * D)/H]

# Following are the fixed values of C and H:

# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180
# The output of the program should be:

# 18,22,24
