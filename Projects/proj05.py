#/****************************************************************************
#    Section 10
#    Computer Project #3
#****************************************************************************/

#This program can decrypt a message that has been encoded using a Caesar cipher.
#The program finds the shift for the cipher by finding the shift from the most
#common character 'e'.

#Algorithm:
#1. Read the cipher-text
#   a. Create a variable for the words
#   b. For each line in the file:
#       i. add the line to the blank variable
#2. Get a count of each character in the entire cipher-text
#   a. Create a blank list
#   b. Add 26 zero values to the list by iterating through the range from 0-26
#       and appending a 0 value
#   c. For the cipherTextChar in the words variable
#       i. If the cipherTextChar is equal to ' ', then skip the space/continue
#       ii. elif the cipherTextChar is more than or equal to 'a' and less than
#           or equal to 'z':
#           1. cipherIndex is equal to the order of the cipherTextChar minus
#               the order of the letter 'a'.  This causes the letter a to be
#               equal to 0, 'b' equal to 1, and so on for indexing purposes
#           2. Add one to the index value of the letter in letterIndex
#3. Find the most common character, the shift from 'e' to that character, and
#   check that the shift works for the next most common character ('t' and 'a')
#   a. Create a copy of letterIndex called letterIndex2
#   b. Set shift, shift2, and shift3 variables
#   c. Find the maximum value in letterIndex
#   d. The max value is the letter e, the index number for e is 4, subtract
#       4 from the balue to get the shift in letters
#   e. if the shift is a negative number:
#       i. Add 26 so it loops to the end of the alphabet
#   f. Take away the max value from the letterIndex2
#   g. Repeat the process for letters t and a
#4. Using the shift, decode each character of the cipher text and print
#   a. if shift, shift2, and shift3 are equal:
#       i. for cipherTextChar in words:
#           1. if the cipherTextChar is a space, then add a space to newText
#               a. Continue
#           1. if the cipherTextChar is more than or equal to 'a' and less than
#               or equal to 'z':
#               a. cipherTextChar = ord(cipherTextChar) = ord('a') to find index
#               b. if the shift is more than the cipherTextChar index:
#                   i. Add 26 to the cipherTextChar and then subtract the shift
#                       to loop around the alphabet
#                   ii. Add ord('a') and convert back to a character using chr()
#                   iii. Add the new plainTextChar to the newText
#               c. else:
#                   i. subtract the shift from the cipherTextChar
#                   ii. Add ord('a') and then convert back to a character
#                   iii. Add the new plainTextChar to the newText

words = ""
for line in file("cipherText.txt"):
    words = words + line + " "
#Reads the cipherText from file
    
letterIndex = []
for key in range(0,26):
    letterIndex.append(0) #creates a list with 26 zeros

for cipherTextChar in words:
    if cipherTextChar == ' ':
        continue
    #if cipherTextChar is a space, ignore and go to the next character
    elif cipherTextChar >= 'a' and cipherTextChar <= 'z':
    #if cipherTextChar is a letter between a and z
        cipherIndex = ord(cipherTextChar) - ord('a')
        #convert the letter to the index number of the letter (ex. a = 0)
        letterIndex[cipherIndex] += 1
        #add one to the letterIndex everytime the character occurs

letterIndex2 = []
for element in letterIndex:
    letterIndex2.append(element)
#copies letterIndex to a new letterIndex2 in order to make changes to one list

shift = 0
shift2 = 0
shift3 = 0

value = max(letterIndex) #finds the maximum value
shift = letterIndex.index(value) - 4
#the maximum value letter should be 'e', subtract the index of 'e' (4) to find
#actual shift
if shift < 0:
    shift = shift + 26
    #in case the shift is negative, add 26 so it loops to end of alphabet
    
letterIndex2.remove(value) #remove highest value in order to find second highest
value = max(letterIndex2)
shift2 = letterIndex.index(value) - 19
#19 is the index of 't' the second highest character to occur
if shift2 < 0:
    shift2 = shift2 + 26
    
letterIndex2.remove(value)
value = max(letterIndex2)
shift3 = letterIndex.index(value)
#finds the shift for 'a', the third highest character, with an index of 0
if shift3 < 0:
    shift3  = shift3 + 26
    
newText = ''
if shift == shift2 == shift3: #if all three shifts are consistent
    for cipherTextChar in words:
        if cipherTextChar == ' ': 
            newText += ' '
            #for spaces, adds a space in the newText
            continue
        elif cipherTextChar >= 'a' and cipherTextChar <= 'z':
        #if the cipherTextChar is a letter between 'a' and 'z'
            cipherTextChar = ord(cipherTextChar) - ord('a')
            #finds the index of the cipherTextChar
            if shift > cipherTextChar:
                #if shift is more than cipherTextChar index, result will be neg
                plainTextNum = cipherTextChar + 26 - shift
                #subtracts shift from cipherTextChar to get plainTextNum
                #compensates for negative index, add 26 to loop around alphabet
                plainTextNum += ord('a')
                #add the ord('a') to get back to ASCII value
                plainTextChar = chr(plainTextNum)
                #converts ASCII value to character
                newText += plainTextChar
                #appends newText with plainTextChar
            else:
                #for cipherTextChar that is more than the shift
                plainTextNum = cipherTextChar - shift
                plainTextNum += ord('a')
                plainTextChar = chr(plainTextNum)
                newText += plainTextChar
    print newText
else:
    print 'Cipher does not work'

