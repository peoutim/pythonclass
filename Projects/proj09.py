#/****************************************************************************
#    Section 10
#    Computer Project #9
#****************************************************************************/
#
#This is a program that is blackjack solitaire.  It creates a tableau where
#the user can put dealt cards.  After the tableau is filled, the score is
#calculated based on the values of each column and row.  If a column of two
#cards equals 21, the score is increased by 3 points to 10 because this is
#the elusive blackjack.
#
#Algorithm
##1. Import cards and os
##2. Get the deck from the cards module and shuffle it
##3. Create an empty tableau
##4. Deal one card and ask the user to place it in the tableau
##5. Update the tableau and ask for the user input up until 20 cards are dealt
##or the tableau is full
##6. Calculate the value of each column and row using the valueFinding functions
##    a. if there is an ace, adjust the value accordingly
##    b. if there is two cards in the column and blackjack is scored, adjust
##    the value accordingly
##7. Take the value and score it based on the scoring function
##8. Sum the score and return it at the end of the game

import cards
import os

theDeck = cards.Deck()
#gets theDeck from the cards module
theDeck.shuffle()
#shuffles the deck

cardList = []
count1 = 1
for key in range(0,20):
    cardList.append(count1) #creates a list with numbers 1 to 20
    count1 += 1

def initialBlankTableau(cardList):
    '''creates a blank tableau for initial play'''
    a = cardList[0]
    b = cardList[1]
    c = cardList[2]
    d = cardList[3]
    e = cardList[4]
    f = cardList[5]
    g = cardList[6]
    h = cardList[7]
    i = cardList[8]
    j = cardList[9]
    k = cardList[10]
    l = cardList[11]
    m = cardList[12]
    n = cardList[13]
    o = cardList[14]
    p = cardList[15]
    q = cardList[16]
    r = cardList[17]
    s = cardList[18]
    t = cardList[19]
    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t
    #letters are supposed to correspond with their number (a=1) in the tableau
    #as numbers can not be variable names

def cardLocation(newLocation, cardList, theCard):
    '''replaces the place in the list with the new card location'''
    cardList[newLocation - 1] = theCard
    a = cardList[0]
    b = cardList[1]
    c = cardList[2]
    d = cardList[3]
    e = cardList[4]
    f = cardList[5]
    g = cardList[6]
    h = cardList[7]
    i = cardList[8]
    j = cardList[9]
    k = cardList[10]
    l = cardList[11]
    m = cardList[12]
    n = cardList[13]
    o = cardList[14]
    p = cardList[15]
    q = cardList[16]
    r = cardList[17]
    s = cardList[18]
    t = cardList[19]
    return a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, cardList

def valueFinding2(card1, card2, finalScore):
    '''finds theValue of a column with two cards in it, also calculates
    blackjacks'''
    theValue = 0
    theValue += card1.get_value()
    theValue += card2.get_value()
    #gets the value of card1 and card2
    count = 0
    if card1.get_rank() == 1:
        count = 1
    if card2.get_rank() == 1:
        count = 1
    #if card1 or card2 is an ace (rank == 1), the count is one
    theValue = aces(theValue, count)
    #with the count being one, the aces function changes theValue
    if theValue == 21:
        theValue = 51
    #if two cards make theValue==21, blackjack occurs and theScore is set to 51
    #which scores higher than normal in the scoring function
    #it is set to 51 because the highest bust value is 50
    finalScore1 = scoring(theValue, finalScore)
    #takes theScore of the cards and scores it against the finalScore function
    return finalScore1

def valueFinding3(card1, card2, card3, finalScore):
    '''finds theValue of a row with three cards in it'''
    theValue = 0
    theValue += card1.get_value()
    theValue += card2.get_value()
    theValue += card3.get_value()
    count = 0
    if card1.get_rank() == 1:
        count = 1
    if card2.get_rank() == 1:
        count = 1
    if card3.get_rank() == 1:
        count = 1
    theValue = aces(theValue, count)
    finalScore1 = scoring(theValue, finalScore)
    return finalScore1

def valueFinding4(card1, card2, card3, card4, finalScore):
    '''finds theValue of a column with four cards in it'''
    theValue = 0
    theValue += card1.get_value()
    theValue += card2.get_value()
    theValue += card3.get_value()
    theValue += card4.get_value()
    count = 0
    if card1.get_rank() == 1:
        count = 1
    if card2.get_rank() == 1:
        count = 1
    if card3.get_rank() == 1:
        count = 1
    if card4.get_rank() == 1:
        count = 1
    theValue = aces(theValue, count)
    finalScore1 = scoring(theValue, finalScore)
    return finalScore1

def valueFinding5(card1, card2, card3, card4, card5, finalScore):
    '''finds theValue of a row with five cars'''
    theValue = 0
    theValue += card1.get_value()
    theValue += card2.get_value()
    theValue += card3.get_value()
    theValue += card4.get_value()
    theValue += card5.get_value()
    count = 0
    if card1.get_rank() == 1:
        count = 1
    if card2.get_rank() == 1:
        count = 1
    if card3.get_rank() == 1:
        count = 1
    if card4.get_rank() == 1:
        count = 1
    if card5.get_rank() == 1:
        count = 1
    theValue = aces(theValue, count)
    finalScore1 = scoring(theValue, finalScore)
    return finalScore1

def aces(theValue, count):
    '''Changes the value of aces from 1 to 11 if necessary'''
    if count > 0:
        if theValue < 12:
            theValue += 10
    # if theValue is less than 12, the ace can be changed to an 11 and theValue
    # will not be over 21.  10 is added to change the ace from 1 to 11
    return theValue

def scoring(theValue, finalScore):
    '''calculates the finalscore based on the scoring technique'''
    if theValue == 51:
    #if theValue == 51, blackjack occured, special higher scoring
        finalScore += 10
    if theValue == 21:
        finalScore += 7
    if theValue == 20:
        finalScore += 5
    if theValue == 19:
        finalScore += 4
    if theValue == 18:
        finalScore += 3
    if theValue == 17:
        finalScore += 2
    if theValue <= 16:
        finalScore += 1
    return finalScore

count2 = 0
errorList = []
while count2 == 0:
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t \
       = initialBlankTableau(cardList)
    count2 +=1
#initializes the blank tableau to start the game
    
while 0 < count2 and count2 < 21:
    #only deals 20 cards total
    aCard = theDeck.deal()
    #deals one card
    print 'Deal: ', aCard
    print 'Tabeau: '
    print '%10s %5s %5s %5s %5s'%(str(a), str(b), str(c), str(d), str(e))
    print '%10s %5s %5s %5s %5s'%(str(f), str(g), str(h), str(i), str(j))
    print '%16s %5s %5s'%(str(k), str(l), str(m))
    print '%16s %5s %5s'%(str(n), str(o), str(p))
    print ''
    print 'Discards %1s %5s %5s %5s'%(str(q), str(r), str(s), str(t))
    newLocation = raw_input(
        'Choose location (1-20) to move card to (q to quit): ')
    
    while not newLocation.isdigit():
        if newLocation == 'q':
            exit()
            # exits if user inputs 'q'
        print 'Location is not a number, try again'
        newLocation = raw_input(
            'Choose location (1-20) to move card to (q to quit): ')
        #error checking if newLocation is not a number
        
    newLocation = int(newLocation)
    # changes newLocation from a string to an integer
    
    while newLocation not in range(1, 21):
        print 'Location not in range'
        newLocation = int(raw_input(
            'Choose location (1-20) to move card to (q to quit): '))
        #error checking for numbers not in the card tableau range
        
    for num in errorList:
        while num == newLocation:
            print 'Location already full, try again'
            newLocation = int(raw_input(
                'Choose location (1-20) to move card to (q to quit): '))
    errorList.append(newLocation)
    #checks against errorList to see if newLocation was already chosen
    #and therefore, already has a card in it
    #also, appends the newLocation to the errorList
    
    a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, cardList = \
       cardLocation(newLocation, cardList, aCard)
        #calls the function cardLocation and generates new tableau values
        #as aCard is added to the cardList
    
    if count2 > 15:
        count3 = 0
        for num in range (1, 17):
            if num in errorList:
                count3 += 1
                if count3 == 16:
                    print 'Tableau: '
                    print '%10s %5s %5s %5s %5s'%(str(a), str(b), str(c), \
                                                  str(d), str(e))
                    print '%10s %5s %5s %5s %5s'%(str(f), str(g), str(h), \
                                                  str(i), str(j))
                    print '%16s %5s %5s'%(str(k), str(l), str(m))
                    print '%16s %5s %5s'%(str(n), str(o), str(p))
                    print ''
                    print 'Discards %1s %5s %5s %5s'%(str(q), str(r), \
                                                      str(s), str(t))
                    count2 = 21
    #if all of the tableau is filled but the discards are not filled, this
    #checks for that and changes the count2 to 21 so that new cards are not
    #dealt.  Also, it reprints the Tableau one last time all filled out
                    
    count2 +=1
    #count variable to make sure there are not more than 20 cards dealt


finalScore = 0
finalScore = valueFinding2(cardList[0], cardList[5], finalScore)
finalScore = valueFinding2(cardList[4], cardList[9], finalScore)
finalScore = valueFinding3(cardList[10], cardList[11], cardList[12], \
                            finalScore)
finalScore = valueFinding3(cardList[13], cardList[14], cardList[15], \
                            finalScore)
finalScore = valueFinding4(cardList[1], cardList[6], cardList[10], \
                            cardList[13], finalScore)
finalScore = valueFinding4(cardList[2], cardList[7], cardList[11], \
                            cardList[14], finalScore)
finalScore = valueFinding4(cardList[3], cardList[8], cardList[12], \
                            cardList[15], finalScore)
finalScore = valueFinding5(cardList[0], cardList[1], cardList[2], \
                            cardList[3], cardList[4], finalScore)
finalScore = valueFinding5(cardList[5], cardList[6], cardList[7], \
                            cardList[8], cardList[9], finalScore)
#scores column AF, EJ, BGKN, CHLO, and DIMP and scores rows ABCDE, FGHIJ,
#KLM, and NOP and adds the scores together to make finalScore

print 'Your final score is: ',finalScore
