# Troy Sweetnam, tsweetna@usc.edu
# ITP 115, Fall 2021
# Section: 31856
# Final Project
# main_sweetnam_troy.py
# Description: This is our main function for the national parks index, it allows the user to interact with teh index and see certain
# information about national parks by state, by search, or by size.

import tasks
import interface      # importing our other files to call their functions


def main():
    print("National Parks")

    parkDictionary = tasks.createListOfParks(fileName="national_parks(1).csv")   # create the list of parks for us to reference

    userInput = ''              # initializing our userInput to start the while loop
    menuDict = interface.getMenuDict()     # create the dictionary for the menu

    while userInput != 'q':    # so long as the user has not quit yet...
        interface.displayMenu(menuDict)
        userInput = interface.getUserInput(menuDict)    # display the menu and get user input
        userInput = userInput.lower()
        if userInput == 'a':
            interface.printAllParks(parkDictionary)     # if the input is A, call the printAllParks to print parks
        elif userInput == 'b':
            interface.printParksInState(parkDictionary) # if the input is B, call the printParksInState which will
        elif userInput == 'c':                          # gather user input and print the parks in the desired state
            interface.printLargestPark(parkDictionary)    # if the input is C, call the printLargestPark function
        elif userInput == 'd':
            interface.printParksForSearch(parkDictionary)    # if the input is D, call the printParksForSearch function
                                                            # this will also prompt the user for usr input
    print("Thank you! Goodbye.")

main()



