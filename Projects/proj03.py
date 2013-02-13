#/****************************************************************************
#    Section 10
#    Computer Project #3
#****************************************************************************/

#This program creates a Latin Square which is a n*n square with n different 
#numbers.  Each number only appear once in each column and once in each row.
#
#Algorithm
#   1. Prompt for integers for the order and for the top left number
#   2. Check that integers are compatible
#   3. While leftorig is less than order and greater than 0
#       i. Initialize left
#       ii. Print a line of numbers from left to order
#       iii. Print from 1 to left
#       iv. Loop until leftorig equals order
#   4. While leftorig is not 1
#       i. Initialize left2
#       ii. Print a line of numbers from left2 to order
#       iii. Print from 1 to left2
#       iv. Loop until num1 equals left2

orderStr = raw_input('Please input the order of the square: ')
#User input for how many rows and columns of the created square
order = int(orderStr)
#Convert string into an integer
while order <=0:
    print 'Error, order is not a positive number, try again'
    orderStr = raw_input('Please input the order of the square: ')
    order = int(orderStr)
    #Reprompts user for positive number if initial input was zero or negative
leftStr = raw_input('Please input the top left number: ')
#User input for the top left number of the square
left = int(leftStr)
while left > order or left <= 0:
    print 'Error, left number is larger than order, try again'
    leftStr = raw_input('Please input the top left number: ')
    left = int(leftStr)
    #Reprompts user for number between 0 and order
leftorig = int(left)
left2 = int(left)
num = int(1)
num1 = int(1)
num2 = int(1)


while leftorig > 0 and leftorig <= order: #leftorig no higher than order
    left = leftorig #Reinitializes left
    num = 1
    while left <= order: #Prints numbers from left to order
        print left,
        left = left + 1
    while num < leftorig: #Prints numbers from 1 to left
        print num,
        num = num + 1
    print '' #Starts the next line
    leftorig = leftorig + 1 #Adds one to the first number of the line


while left2 != 1 and num1 < left2: #To print all lines starting with < left
    num2 = num1 #Reinitializes num2
    num = 1
    while num2 <= order: #Prints numbers from num2 to order
        print num2,
        num2 = num2 + 1
    while num < left2 and num < num1: #Prints numbers from 1 to left2
        print num,
        num = num + 1
    print '' #Starts the next line
    num1 = num1 + 1 #Adds one to the first number of the line
