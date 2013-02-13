#/****************************************************************************
#    Section 10
#    Computer Project #8
#****************************************************************************/
#
#This is a program that plots the engine size versus the average MPG.  It uses
#functions to parse the data in the given file to two variable lists.  After
#that, the data is then summed in various ways and then input into a slope,
#intercept, and correlation equations.  Afterwards, the program plots the
#engine size versus the average MPG of the data and a regression line using
#Pylab.
#
#Algorithm
##1. Open the file using a function called openFile.  This creates a list of all
##of the lines in the file.
##2. Obtain the engine size and store it in a list for every car.  This is done
##by using the function findXvalues.  This is stored as xList.
##3. Obtain the average MPG and store in in a list for every car.  This is done
##by using the function findYvalues.  This is stored as yList
##4. Find the length of the xList by using the len operator
##5. Find the sum of all of the numbers in the xList and the sum of all of the
##numbers in the yList by calling the sumVariable function
##6. Find the sum of the product of X and Y values and store as sumXY
##7. Find the sum of all of the x and y values squared using the
##sumVariableSquared function
##8. Using the slopeXandY function, find the slope of the regression line
##9. Using the interceptXY function, find the intercept of the regression line
##10. Using the correlation function, find the correlation of the regression
##line with the data
##11. Create two lists with x and y values for the regression line
##12. Use pylab to plot the data in xList and yList and the regression line
##from plotting the lists generated in step 11

import pylab
import numpy
import math
import os

def openFile(theFile):
    '''opens the file, reads the file, and then closes the file'''
    text = open(theFile)
    #opens the file
    allText = text.readlines()
    #makes a list of each of the lines in the file
    text.close()
    #closes the file
    return allText

def findXvalues(textList):
    '''finds the x values for the graph, these are the engine size values'''
    xList = []
    for numberList in textList:
    #iterates through each line the list of lines called textList
        if numberList[76] != '*' and numberList[86] != '*' \
           and numberList[89] != '*':
        #checks that there are values there instead of a '*'
            xValue = float(numberList[74] + numberList[75] + numberList[76])
            #concatenates the characters in index 74, 75, and 76 which
            #correspond to the average engine size
            #then takes the string and turns it into a float
            xList.append(xValue)
            #appends the float vale to the xList which is all of the x values
    return xList

def findYvalues(textList):
    '''finds the y values for the graph, these are the average MPG'''
    yList = []
    for numberList in textList:
    #iterates through each line of the list of lines called textList
        if numberList[76] != '*' and numberList[86] != '*' \
           and numberList[89] != '*':
        #checks that there are values there instead of a 'a'
            cityMPG = float(numberList[85] + numberList[86])
            #concatenates the index value 85 and 86 to get the cityMPG
            #and then turns it into a float value
            highwayMPG = float(numberList[88] + numberList[89])
            #concatenates the index value 88 and 89 to get the highwayMPG
            #and then turns it into a float value
            yValue = (cityMPG + highwayMPG)/2
            #finds the average of the cityMPG and the highwayMPG
            yList.append(yValue)
            #appends the final yValue to the yList of y variables
    return yList

def sumVariable(variableList):
    '''Sums the numbers in the variable list and returns the sum'''
    sumNum = 0
    for num in variableList:
        sumNum += num
        #for each number in the variableList, it adds it to the 'sumNum' to
        #find the final sum of all the num in the variableList
    return sumNum

def sumXandY(xList, yList):
    '''sums the product of each corresponding x, y pair'''
    sumXY = 0
    count = 0
    while count < len(xList):
        sumXY += xList[count] * yList[count]
        #finds the product of x and y and adds it to sumXY
        count += 1
    return sumXY

def sumVariableSquared(variableList):
    '''sums the square of every number in the variable list and returns sum'''
    variableSquared = 0
    for num in variableList:
        variableSquared += num**2
        #for each num in variableList, the num is squared and then summed
        #together to make variableSquared
    return variableSquared

def slopeXandY(sumXY, sumX, sumY, sumXsquared, n):
    '''calculates the slope of the x and y values'''
    slope = (n*sumXY - (sumX*sumY))/(n*sumXsquared - (sumX)**2)
    #uses the slope formula to find the slope
    return slope

def interceptXY(sumY, slope, sumX, n):
    '''calculates the intercept from the x and y values'''
    intercept = (sumY - (slope*sumX))/n
    #uses the intercept formala to find the intercept
    return intercept

def correlation(n, sumXY, sumX, sumY, sumXsquared, sumYsquared):
    '''calculates the correlation from the x and y values'''
    corrNumerator = n*sumXY - (sumX*sumY)
    #calculates the numerator from the correlation equation
    corrDenominator = math.sqrt((n*sumXsquared - (sumX)**2) * \
                                     (n*sumYsquared - (sumY)**2))
    #calculates the denominator from the correlation equation
    corr = corrNumerator/corrDenominator
    #calculates the correlation from the corrNumerator and the corrDenominator
    return corr

def regressionLine(slope, intercept, xRegression):
    '''creates a list of y values based on the slope and intercept \
        to draw the regression line'''
    yRegression = []
    for x in xRegression:
        yValue = slope*x + intercept
        #for each x value, it calculates a y value using the slope and intercept
        #these values will be used to draw a regression line
        yRegression.append(yValue)
        #appends the yValue to the yRegression list
    return yRegression

textList = openFile('04cars.dat')
xList = findXvalues(textList)
yList = findYvalues(textList)
n = len(xList)
sumX = sumVariable(xList)
sumY = sumVariable(yList)
sumXY = sumXandY(xList, yList)
sumXsquared = sumVariableSquared(xList)
sumYsquared = sumVariableSquared(yList)
slope = slopeXandY(sumXY, sumX, sumY, sumXsquared, n)
intercept = interceptXY(sumY, slope, sumX, n)
corr = correlation(n, sumXY, sumX, sumY, sumXsquared, sumYsquared)
#calls the functions

xRegression = [1,2,3,4,5,6]
yRegression = regressionLine(slope, intercept, xRegression)
#creates two lists to draw a regression line

print 'The slope is: ',slope
print 'The intercept is: ', intercept
print 'The correlation is: ', corr

pylab.plot(xList, yList, 'ro')
#plots the x and y values on a graph
pylab.plot(xRegression, yRegression, 'b')
#plots the regression line
pylab.xlabel('Type of engine')
pylab.ylabel('Average MPG')
pylab.title('Graph of type of engine vs. average mpg')
#labels axes
pylab.show()
#shows the graph
