#/****************************************************************************
#    Section 10
#    Computer Project #10
#****************************************************************************/

#This program creates a simulator for an elevator.  It uses three classes: a
#Building class, an Elevator class, and a Customer class.  These three classes
#interact with each other to output a building showing where all the customers
#are.  The elevator moves up the building and collects all of the customers and
#and drops them off on their way up.  If they customer is not dropped off, the
#elevator starts to go all the way down until the last customer is dropped off.
#The default method for the elevator is to go up all the way and then come back
#down.
#
#I created another method for the elevator to go up by two floors to each of the
#odd floors, and then go down through all of the even floors.
#
##Algorithm
##1. Ask the user for the number of floors and number of customers
##    a. do error checking for non integers
##2. Create the building with the number of floors
##3. With the number of customers, take each customer and put it through the
##Customer class to create a customer with an ID, a current floor, and a
##destination floor
##4. Create an elevator in the building.  Make the default elevator move up
##each floor and then go down each floor until all of the customers are off
##5. Make the new elevator that goes up to every other floor and then down
##on the floors it hasn't been to
##6. Put the customers on the elevator when the elevator's current floor is
##equal to their current floor.
##7. Take the customer off the elevator when their destination is reached and
##mark them as finished so that they do not get on the elevator again.
##8. Report how many floors each elevator had to go to in order to drop off
##all of the customers.

import random
import copy

def main():
    '''main function that starts the elevator in the building and keeps
    running it until it is finished with all the customers'''
    ourHouse = Building()
    while True:
        ourHouse.run()
        if len(ourHouse.lift.finished_list) == len(ourHouse.cust_list) and not \
        False in ourHouse.lift.finished_list:
            break
        #ends the elevator when all of the customers are at destination
    raw_input("Section Two:\n\n")
    #separates the default program from my method
    
    while True:
        ourHouse.run2()
        if len(ourHouse.lift2.finished_list) == len(ourHouse.cust_list1) and \
           not False in ourHouse.lift2.finished_list:
            break
    print "Default floors visited: ", ourHouse.lift.dist_traveled - 1
    print "New method floors visited: ", ourHouse.lift2.dist_traveled - 1
    #shows the comparison floors visited
    print "GAME OVER"

class Building(object):
    def __init__(self):
        '''initializes the varibles for the number of floors, customers, and the
        elevator'''
        self.numFloors = raw_input('How many floors?: ')
        while not self.numFloors.isdigit() or self.numFloors == '0' \
              or self.numFloors == '1':
            self.numFloors = raw_input('Input not valid, please try again: ')
        else:
            self.numFloors = int(self.numFloors)
        #error checking to make sure the number of floors is an integer and is
        #more than one floor

        self.numCust = raw_input('How many customers?: ')
        while not self.numCust.isdigit() or self.numCust == '0':
            self.numCust = raw_input('Input not valid, please try again: ')
        else:
            self.numCust = int(self.numCust)
        #error checking to make sure that the input is an integer
            
        self.cust_list = []
        for cust in range(0, self.numCust):
            self.cust_list.append(Customer(self, cust))
        #for the number of customers that the user input, it creates a new
        #customer using the Customer class
            
        self.cust_list1 = []
        for cust in self.cust_list:
            cust = copy.deepcopy(cust)
            self.cust_list1.append(cust)
        #deep copies the customer list for use with my method, other customer
        #list is for the default program
            
        self.lift = Elevator(self)
        #creates an elevator for the default

        self.lift2 = Elevator(self)
        #creates an elevator for the new method
        
    def run(self):
        '''runs the elevator by having it move and then outputting the
        building'''
        self.lift.move()
        self.output()

    def run2(self):
        '''runs a new elevator to try out my method of elevator movement'''       
        self.lift2.myMove()
        self.myOutput()        
    
    def output(self):
        '''outputs the floor, customers, and which floor the elevator is on'''
        print "Floor                 Customers                 Elevator"
        print "--------------------------------------------------------"
        floor_list = list(range(1, self.numFloors + 1))
        floor_list.reverse()
        for num in floor_list:
            print "  %i"%(num), " "*18,
            #prints the floor number
            cust_str = ''
            for cust in self.cust_list:
                if cust.cust_cur_floor == num and not cust.in_elevator:
                    cust_str += str(cust)+ ' '
                    #creates a string with the customers on the same floor
            print "%-10s" %(cust_str),
            #prints the customers on the particular floor
            if self.lift.current_floor == num:
                print "%17s" %(self.lift)
                print "--------------------------------------------------------"
                #prints the elevator if it's on that floor
            else:
                print "  "*18
                print "--------------------------------------------------------"
        print "\n"

    def myOutput(self):
        '''outputs my method for elevator movement and shows the floor, the
        customers, and which floor the elevator is on'''
        print "Floor                 Customers                 Elevator"
        print "--------------------------------------------------------"
        floor_list = list(range(1, self.numFloors + 1))
        floor_list.reverse()
        for num in floor_list:
            print "  %i"%(num), " "*18,
            cust_str = ''
            for cust in self.cust_list1:
                if cust.cust_cur_floor == num and not cust.in_elevator:
                    cust_str += str(cust)+ ' '
            print "%-10s" %(cust_str),
            if self.lift2.current_floor == num:
                print "%17s" %(self.lift2)
                print "--------------------------------------------------------"
            else:
                print "  "*18
                print "--------------------------------------------------------"
        print "\n"

    
class Elevator(object):
    '''Elevator class, had methods on how the elevator moves and what is in it'''
    def __init__(self, myBuild):
        '''initialises the variables for the number of floors, the current
        floor, the direction, the distance travelled, the building, and
        the register list'''
        self.numFloors = myBuild.numFloors

        self.current_floor = 0

        self.direction = 1

        self.dist_traveled = 0

        self.build = myBuild
        
        self.register_list = []
        
    def changeDirection(self):
        '''method for how the elevator moves and then changes direction'''
        if self.current_floor == self.numFloors:
            self.direction = -1
            #makes the elevator go down
        if self.current_floor == 1:
            self.direction = 1
            #makes the elevator go up
        return self.direction

    def __str__(self):
        '''prints an X to represent the elevator'''
        return 'X'
    
    def move(self):
        '''moves the elevator based on the direction it's going'''
        self.changeDirection()
        for item in self.build.cust_list:
            if item.cust_cur_floor == self.current_floor and not item.finished:
                self.register_customer(item)
                #puts the customer in the elevator
            elif item.cust_dest_floor == self.current_floor and \
                 item.in_elevator:
                self.cancel_customer(item)
                #gets the customer out of the elevator at destination floor
        self.finished_list = []
        for cust in self.build.cust_list:
            if cust.finished:
                self.finished_list.append(cust)
            #adds a customer to the finished list
        if len(self.finished_list) == len(self.build.cust_list):
            print "***** SIMULATION FINISHED *****"
            print "Floors visited: ", self.dist_traveled - 1
            #subtracts one for the initial floor
        else:
            self.current_floor = self.current_floor + self.direction
            #adds the direction to the elevator specified in the direction
            #method
            self.dist_traveled += 1

    def myChangeDirection(self):
        '''my method for changing the direction of the elevator'''
        if self.current_floor == self.numFloors:
            self.direction = -1
        if self.current_floor == 1:
            self.direction = 2
        #if it is one, add two
        if self.current_floor % 2 != 0:
            self.direction = 2
        #if it is odd, add two
        if self.current_floor % 2 == 0:
            self.direction = -2
        #if it is even, subtract two
        return self.direction

    def myMove(self):
        '''using my method for changing the direction of the elevator, I move
        the elevator'''
        self.myChangeDirection()
        for item in self.build.cust_list1:
            if item.cust_cur_floor == self.current_floor and not item.finished:
                self.register_customer(item)
            elif item.cust_dest_floor == self.current_floor and \
                 item.in_elevator:
                self.cancel_customer(item)
        self.finished_list = []
        for cust in self.build.cust_list1:
            if cust.finished:
                self.finished_list.append(cust)
        if len(self.finished_list) == len(self.build.cust_list1):
            print "***** SIMULATION FINISHED *****"
            print "Floors visited: ", self.dist_traveled - 1
        else:
            self.current_floor = self.current_floor + self.direction
            if self.current_floor > self.numFloors and self.numFloors %2 == 0:
                self.current_floor = self.numFloors
            #if the number of floors is even, and the current floor is an odd
            #number above the numFloors, the current floor is set to the
            #even number of floors
            if self.current_floor > self.numFloors and self.numFloors %2 !=0:
                self.current_floor = self.current_floor - 3
            #if the number of floors is odd, the current floor will be the
            #numFloors and then the next iteration it will be two over that
            #so it should subtract three to get one below the numFloors which
            #is an even number
            if self.current_floor < 1:
                self.current_floor = 1
            #if the current floor is less than one, set it back to one to go
            #through the loop again
            self.dist_traveled += 1
            
    def register_customer(self, customer):
        '''registers the customer in the elevator'''
        self.register_list.append(customer)
        customer.in_elevator = True
    
    def cancel_customer(self, customer):
        '''takes the customer out of the elevator'''
        customer.in_elevator = False
        customer.cust_cur_floor = self.current_floor
        customer.finished = True
        self.register_list.remove(customer)

class Customer(object):
    '''customer Class, has variables for each customer'''
    def __init__(self, myBuild, cust):
        '''initializes varibles for the customer like the customer ID, the
        current customer floor, the destination floor, and whether the customer
        is still in the elevator or is finished'''
        self.cust_id = cust + 1
        
        self.cust_cur_floor = random.randint(1, myBuild.numFloors)

        self.cust_dest_floor = random.randint(1, myBuild.numFloors)
        #gets random numbers between one and the number of floors for the
        #current floor of the customer and the destination floor
        
        self.in_elevator = False

        self.finished = False
        
        while self.cust_dest_floor == self.cust_cur_floor:
            self.cust_dest_floor = random.randint(1, myBuild.numFloors)
            
    def __str__(self):
        '''print function to represent the customer by their ID'''
        return str(self.cust_id)
    
    def is_finished(self):
        '''method to make the customer finished when they reach their
        destination floor'''
        if self.cust_cur_floor == self.cust_dest_floor:
            self.finished = True

main()

