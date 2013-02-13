#/****************************************************************************
#    Section ?
#    Computer Project #1
#****************************************************************************/

#Program to estimate the population in a number of years in the future

import math

year = int (raw_input('Please enter the number of years in the future: '))
second = year*365*24*60*60 #convert years into seconds

births = int(second/7) #finding number of births
death = int(second/13) #finding number of deaths
immigrant = int(second/35) #finding number of immigrants

myvar = 307357870 #current population
popch = int(births - death + immigrant) #population change
newpop = int(myvar + popch) #new population

print 'Current population is', myvar, '. '
print 'New population in', year, 'years will change by', popch, 'to ', newpop
