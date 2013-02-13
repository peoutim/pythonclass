#/****************************************************************************
#    Section 10
#    Computer Project #6
#****************************************************************************/

import os
import glob
import string

searchQuery = raw_input('Enter your query: ')

def removeStopWords():
    fileObject = open('stopList')
    stopWordsFile = fileObject.read()
    stopWordsFile = stopWordsFile.split()
    return stopWordsFile
#splits the stopWordsFile into strings of words

def StopWordsGoBye(query):
    for word in stopWordsFile:
        if word in query:
            query.remove(word)
    return query
#removes the strings of words from the Stop List from the query input

def splitFiles(theFile):
    fileObject = open(theFile)
    fileObject = fileObject.read()
    fileObject = fileObject.splitlines()
    newFileObject = []
    for line in fileObject:
        newLine = []
        line = line.split()
        for word in line:
            word = word.lower()
            word = word.strip(string.punctuation)
            newLine.append(word)
            newLine = StopWordsGoBye(newLine)
        newFileObject.append(newLine)
    return newFileObject
#opens and reads the file, splits the file into lines, splits the lines into
#words, lowercases the words and strips of punctuation, makes a new list of
#those words, and returns it as a list of list of words

stopWordsFile = removeStopWords()
#calls the removeStopWords function
searchQuery = searchQuery.split()
#splits the searchQuery into strings
searchQuery = StopWordsGoBye(searchQuery)
#calls the SearchQuery function
searchLen = len(searchQuery) + 1
textList = []
fileList = glob.glob("*.txt")
#lists the files that are .txt

for theFile in fileList:
    print theFile
    textList = splitFiles(theFile)
    #calls out the splitFiles function
    for line in textList:
        #gets the first line
        for word in line:
            print word
        #iterates through the first word in the line
            if word == searchQuery[0]:
                #finds if the word is the first word in the searchQuery
                wordIndex = 0
                #line.index(word) + 1
                searchCount = 1
                while searchCount < searchLen:
                    wordIndex = line.index(word) + 1
                    print wordIndex
                    print searchCount
                    if searchQuery[1] == line[wordIndex]:
                        print wordIndex
                        wordIndex2 = wordIndex + 1
                        while searchQuery[searchCount] == line[wordIndex]:
                            print textList.index(line)
                            searchCount += 1
                            wordIndex += 1
                        else:
                            wordIndex = 0
                            print 'query not found'
