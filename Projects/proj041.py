#    Section 10
#    Computer Project #4
#****************************************************************************/

#This program uses a procedure called the 196-algorithm to create palindromic
#integer.  A palindromic integer is an integer that has the same value backwards
#and forwards.  Numbers that do not converge to be a palindromic integer are 
#Lychrel numbers and they are primted when they occur.
#
#Algorithm
#   1. Prompt for the range by asking for two integers
#   2. Initialize the count variables for the palindrome number count, the non-
#       lychrel number count, and the lychrel number count
#   3. For the number in the range:
#       i. Change the integer to a string
#       ii. If the string is the same forwards and backwards, add one to
#           palindrome count
#       iii. Else, add one to the non-Lychrel count
#           a. Reinitialize the newNumIterations count
#           b. While the numberStr is not the same forwards and backwards
#               1. Change the numberStr to an integer and add the reverse
#               2. Add one to the newNumIterations count
#               3. If the newNumIterations count is more than 60
#                   i. Print the number and add one to the l the lychrel count
#                   ii. Subtract one from the non-Lycrel count
#                   iii. Break (stops the program after 60 iterations)
#   4. Print the range, the palindrome count, the non-Lychrel count, and the
#      Lychrel count

intRange1 = int(raw_input('Give me the first integer: '))
#Prompts for the beginning of the range
while intRange1 <=0:
    print 'Error, order is not a positive number, try again'
    intRange1 = int(raw_input('Give me the first integer: '))
    #Reprompts user for positive number if initial input was zero or negative

intRange2 = int(raw_input('Give me the second integer: ')) + 1
#Prompts for the end of the range
while intRange2 < intRange1:
    print 'Error, the end of the range is smaller than the start of the range'
    intRange2 = int(raw_input('Give me the second integer: ')) + 1
    #Reprompts user for a number larger than the start of the range
    
count = 0
newNumCount = 0
lychrelCount = 0
numInt = 0
numStr = ''
#Initializes variables

for num in range(intRange1, intRange2): 
    numStr = str(num) 
    if numStr==numStr[::-1]: #determines if the num is a palindrome
        count = count + 1 #if num is a palindrome, +1 to palindrome count
    else: 
        newNumCount = newNumCount + 1 #adds to the Non-Lychrel number count
        newNumIterations = 1  #Reinitializes newNumIterations for every number
        while numStr!=numStr[::-1]:
            numInt = int(numStr) + int(numStr[::-1])
            #change numStr into an integer and add the reverse
            numStr = str(numInt)
            newNumIterations = newNumIterations + 1
            #adds one to the iteration count
            if newNumIterations > 60: #if iteration count is more than 60
                lychrelCount = lychrelCount + 1
                #num is determined Lychrel number, add one to Lychrel count
                newNumCount = newNumCount - 1
                #subtract one from non-Lychrel count as it is now Lychrel
                print num, 'is looking like a lychrel number'
                break #break from while loop as num is a Lychrel
        
print 'In the range', intRange1, 'to', (intRange2 - 1)
print 'Palendrome Number Count: ', count
print 'Non-Lychrel Number Count: ', newNumCount
print 'Lychrel Count: ', lychrelCount

