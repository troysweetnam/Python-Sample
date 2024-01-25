# Troy Sweetnam, tsweetna@usc.edu
# ITP 115, Fall 2021
# Section: 31856
# Final Project
# interface.py
# Description:
# This program sets up the user interface for our national parks index, it allows for the user to choose an option from the menu
# which results in them looking at a list of the parks, searching by state, finding the largest park, or searching using their own
# input of search terms to find a park(s)

import tasks

def getMenuDict():
    # the code below is our initial menu for the user to choose from, it gives them the options to choose
    # how they want to interact with the park index
    dictionary = {}    # initializing the dictionary
    dictionary["A"] = "All national parks"
    dictionary["B"] = "Parks in a particular state"   # adding the keys and their elements into the dictionary
    dictionary["C"] = "The largest park"
    dictionary["D"] = "Search for park"
    dictionary["Q"] = "Quit"
    return dictionary




def displayMenu(menuDict):
    for i in menuDict:
        print(i + " -> " + menuDict[i])     # for each aspect of the menu, add the key plus and arrow to the content of
                                            # each key to our menu

def getUserInput(menuDict):
    userInput = ""                    # initialize our user input to nothing so the while loop will at least run once
    while userInput not in menuDict.keys():
        userInput = input("Choice: ")    # get the user input and make it upper case to match the keys of the dictionary
        userInput = userInput.upper()

    return userInput



def printAllParks(parksList):
    for i in parksList:
        print(i["Name"], " (", i["Code"], ")")    # print the park name followed by the code given for the park
        print("    Location: ", i["State"])          # print the state the park is located in
        print("    Area: ", i["Acres"], " acres")    # print the area of the park
        print("    Date Established: ", tasks.getDate(i["Date"]))   # importing the date using getParkDate from tasks

def getState():
    twoLetterInput = False  # initliazes our twoLetterInput as False to ensure the while loop runs at least once

    while twoLetterInput == False:
        userInput = input("Enter a state:")   # get input from user and make it upper case
        userInput = userInput.upper()
        if len(userInput) == 2:
            twoLetterInput = True      # if the length of their input = 2, then the input is valid
        else:
            print("Please enter the two letter abbreviation")   # if not, the input is invalid and the while loop runs again

    return userInput

def printParksInState(parksList):
    userState = getState()  # asking the user for the state in which we will print the parks
    counter = 0 # initialize our counter for the for loop

    for i in parksList:
        if userState in i["State"]:
            print(i["Name"], " (", i["Code"], ")")   # using our code from printAllParks to print the information of each park
            print("    Location: ", i["State"])         # that is found in the user inputted state
            print("    Area: ", i["Acres"], " acres")
            print("    Date Established: ", tasks.getDate(i["Date"]))
            counter = counter + 1  # add to the counter each time we find a state
    if counter == 0:
        print("There are no parks in ", userState, " or it is an invalid state")   # if our counter remainds at 0 after searching the parksList, there are no parks in
                                                     # the user inputted state

def printLargestPark(parksList):
    largestCode = tasks.getLargestPark(parksList)   # use our getLargestPark to return the code of the largest park

    for i in parksList:
        if i["Code"] == largestCode:      # checking every park in the parklist we will see which one is the largest
            print(i["Name"], " (", i["Code"], ")")
            print("    Location: ", i["State"])        # same code from printAllParks to print the information on the largest park
            print("    Area: ", i["Acres"], " acres")
            print("    Date Established: ", tasks.getDate(i["Date"]))
            print("    Description: ", i["Description"][1:])



def printParksForSearch(parksList):
    userInput = input("Enter text for searching: ")    # the user inputs text for us to check through our park index with
    userInput = userInput.lower()   # making it lower case
    userList = []  # initializing variable to see if the input matches any park details

    for i in parksList:
        if userInput in i["Name"].lower():
            userList.append(i)           # so if the input matches part of the name, we add that park into our our list for the user
        elif userInput in i["Code"].lower():
            userList.append(i)           # same for the code, if it matches we add it to userList
        elif userInput in i["Description"].lower():
            userList.append(i)           # again, same thing, but for any part of the description this time
    if len(userList) != 0:
        for i in userList:
            print(i["Name"], " (", i["Code"], ")")     # same print statements from printAllParks
            print("    Location: ", i["State"])
            print("    Area: ", i["Acres"], " acres")
            print("    Date Established: ", tasks.getDate(i["Date"]))

            parkDescription = i["Description"]  # indexing the description of our park
            print("    Description: ", parkDescription[1:len(parkDescription) - 1])   #printing the description of our park from the beginning
    else:                                                                             #of the description to the end
        print("There are no national parks for the search term \'", userInput, "\'" )    # in the case of no search matches, print that there is no match

