#/****************************************************************************
#    Section 10
#    Computer Project #7
#****************************************************************************/

#This program creates a spell checker.  It reads each word in a file and  
#compares it against a reference list of words.  If the word is not found in the
#reference list, the word goes through four functions that create a candidate
#list with possible words with the correct spelling.  The user then decides
#to either keep the original word, input a new replacement, or choose from the
#list of candidate words.  The corrected spelling of all words is written into
#a new file with the '-chk' to the end of the file name.

#Algorithm
#1. print out directions, ask user for file to spell check and reference file
#   a. if no reference file given, default to ref.txt
#2. open the file to spell check by running function openFile
#   a. open theFile, read theFile to allText, then close theFile
#   b. split allText based on white space
#   c. for the word in allText
#       i. lowercase the word, strip the word of punctuation
#       ii. append the word to newLine (empty list)
#   d. return newLine
#3. open the reference file by running function openRefFile
#   a. open theFile, read theFile to allText, then close theFile
#   b. split allText based on white space
#   d. return allWordList
#4. if the word is not in the reference file list called allWordlist
#   a. Then, run it through five functions to create a candidate list of
#       potentially correctly spelled words
#5. after user decides which words to use
#   a. make a new file with the '-chk' at the end
#   b. write the string of correctly spelled words

import os
import string

print 'Commands:'
print '-1 take the word as is'
print '-2 prompt for the replacement'
print '0 to len(w)-1: the selected replacement'

checkFile = raw_input('Please input the name of the file to spell check: ')
refFile = raw_input('Please input the name of the file of the reference list: ')
if not refFile:
    refFile = 'ref.txt'
#Defaults to ref.txt if user does not give a file name for the reference file

def openFile(theFile):
    text = open(theFile)
    allText = text.read()
    text.close()
    #opens theFile, reads theFile, then closes theFile
    allText = allText.split()
    #splits allText based on white space into a list of words
    newLine = []
    for word in allText:
        word = word.lower()
        word = word.strip(string.punctuation)
        newLine.append(word)
        #lowercases word, strips the word of punctuation, and appends the word
        #into a new list
    return newLine

def openRefFile(aFile):
    text = open(aFile)
    allWordText = text.read()
    allWordList = allWordText.split()
    text.close()
    #opens the reference file, reads the file, makes a list of the words in the
    #file based on splitting by whitespace, then closes the file
    return allWordList


fileText = openFile(checkFile)
refText = openRefFile(refFile)
#performs the functions of on the file names given by the user

newFileName = checkFile.split('.')
newFileName[0] += '-chk'
newFileName = newFileName[0] + '.' + newFileName[1]
#splits the file name on the period, adds -chk to the file name, puts the file
#name back together
#This creates a new file for the corrected spelling text to go to

correctedSpellingList = []

def wordSeek():
    for word in fileText:
        #iterates through the words in the fileText
        candidateList = []
        newWordIndex = ''
        if word not in refText:
        #if the word is not in the reference list
            print word
            candidateList = size(word,candidateList)
            candidateList = beginningLetters(word,candidateList)
            candidateList = commonLetters(word, candidateList)
            candidateList = sameLocation(word, candidateList)
            candidateList = sameLocation1(word, candidateList)
            #creates the candidateList by running through four funtions
            for candidateWord in candidateList:
                print candidateList.index(candidateWord),candidateWord
            newWordIndex = raw_input('Action: ')
            newWordIndex = int(newWordIndex)
            #prompts the user for their action
            while newWordIndex > len(candidateList) or newWordIndex < -2:
                newWordIndex = raw_input('Action: ')
                newWordIndex = int(newWordIndex)
                #error checking for the user if they imput the wrong index
            if newWordIndex == -1:
                newWord = word
                #if -1 is input, the word is not replaced
            elif newWordIndex == -2:
                replacement = raw_input('Replacement: ')
                newWord = replacement
                #if -2 is input, the user inputs a replacement word
            else:
                newWordIndex = int(newWordIndex)
                newWord = candidateList[newWordIndex]
                #the index that the user input corresponds to a word in the
                #corrected list, this word will be the replacement word
            correctedSpellingList.append(newWord)
            #appends newWord to the correctedSpellingList
        else:
            correctedSpellingList.append(word)
            #word was found in reference text, has correct spelling
            #word is appended to correctedSpellingList

def size(word,candidateList):
    #finds words within two letters in length of original word
    wordLength = len(word)
    for refWord in refText:
        refWordLength = len(refWord)
        #finds the length of the refWord
        if wordLength - 1 <= refWordLength and refWordLength <= wordLength + 1:
            candidateList.append(refWord)
            #if the refWord is within two letters in length of the word length
            #then it appends the word to the candidate list
        else:
            continue
            #if the refWordLength is not within two of wordLength, continue to
            #the next word
    return candidateList
    
def beginningLetters(word,candidateList):
    #finds all words with the same two letters as the original word in the
    #candidate list
    candidateList1 = []
    for candidateWord in candidateList:
        if word[0] == candidateWord[0] and word[1] == candidateWord[1]:
            candidateList1.append(candidateWord)
    #checks the first and second letter of the word is the same as the first
    #and second letter of the candidateWord
    return candidateList1
    
def commonLetters(word, candidateList):
    #this function finds out how many letters are different between the word
    #and the candidateWord
    wordLetter = []
    candidateList1 = []
    for letter in word:
        wordLetter.append(letter)
        #creates a list of all of the letters in the word
        wordLetterSet = set(wordLetter)
        #changes the list into a set
    for candidateWord in candidateList:
        candidateLetter = []
        for letter in candidateWord:
            candidateLetter.append(letter)
            #creates a list of all of the letters in the word
            candidateLetterSet = set(candidateLetter)
            #changes the list into a set
        candidateWordDifference = wordLetterSet.difference(candidateLetterSet)
        #finds the difference in the set
        if len(candidateWordDifference) < 2:
            candidateList1.append(candidateWord)
            #if the length of the letters in the difference set is two or less
            #then it appends the new candidateList1
    return candidateList1       

def sameLocation(word, candidateList):
    #finds out if the most of the letters are in the same place
    candidateList1 = []
    for candidateWord in candidateList:
        if len(word) <= len(candidateWord):
            wordIndex = len(word)
        else:
            wordIndex = len(candidateWord)
        #finds shorter index of either wordIndex or candidateWord
        wordIndex2 = wordIndex * -1
        #gets backwards index
        forwardCount = 0
        backwardCount = 0
        for i in range (0, wordIndex - 1):
            if word[i] == candidateWord[i]:
                forwardCount +=1
                #finds the number of same letters from forwards on
        for i in range (-1, wordIndex2, -1):
            if word[i] == candidateWord[i]:
                backwardCount +=1
                #finds the number of same letters from backwards on
        sameLocationCount = 0
        if forwardCount <= backwardCount:
            sameLocationCount = backwardCount
        else:
            sameLocationCount = forwardCount
        #finds the longer count between backwardsCount and forwardCount
        if wordIndex - 4 <= sameLocationCount <= wordIndex + 4:
            candidateList1.append(candidateWord)
        #adds the word if the sameLocation Count is within 4 of the wordIndex
    return candidateList1

def sameLocation1(word, candidateList):
    #finds out if the most of the letters are in the same place
    candidateList1 = []
    for candidateWord in candidateList:
        if len(word) <= len(candidateWord):
            wordIndex = len(word)
        else:
            wordIndex = len(candidateWord)
        #finds shorter index of either wordIndex or candidateWord
        wordIndex2 = wordIndex * -1
        #gets backwards index
        forwardCount = 0
        backwardCount = 0
        for i in range (0, wordIndex - 1):
            if word[i] == candidateWord[i]:
                forwardCount +=1
                #finds the number of same letters from forwards on
        for i in range (-1, wordIndex2, -1):
            if word[i] == candidateWord[i]:
                backwardCount +=1
                #finds the number of same letters from backwards on
        sameLocationCount = 0
        if forwardCount <= backwardCount:
            sameLocationCount = backwardCount
        else:
            sameLocationCount = forwardCount
        #finds the longer count between backwardsCount and forwardCount
        wordIndexChange = float(wordIndex * .4)
        if wordIndex - wordIndexChange <= sameLocationCount \
           <= wordIndex + wordIndexChange:
            candidateList1.append(candidateWord)
        #adds the word if the sameLocation Count is within 4 of the wordIndex
    return candidateList1


wordSeek()
#runs the function that finds the misspelled words and creates a candidateList
#the user can decide to replace with a word from the candidateList or replace
#with a word of their choice or not change the word at all
#print correctedSpellingList
spaceMaker = ' '
correctedSpellingString = spaceMaker.join(correctedSpellingList)
#joins the list of words from correctedSpellingList into a string with spaces

myFile = open(newFileName, "w")
#creates the newFileName and opens it in the writing mode
myFile.write(correctedSpellingString)
#writes the correctedSpellingString
myFile.close()
