# tasks.py
# Description:
# This program sets up the functions createListOfParks, getDate, and getLargestPark to be used in our main function and interface file,
# these functions populate the list of parks, allow us to get the date of a park into word form, and return the largest park


def createListOfParks(fileName="national_parks(1).csv"):
    loadFile = open(fileName, "r")    # loading the information from the csv
    counter = 0  # creating our counter for our for loop
    parkList = []                     # initialiazing our park list as empty before we fill it
    # initializing the newPark variable for the for loop

    for i in loadFile:
        newPark = {}
        if counter == 0:     # if the counter is 0, we initialize and strip the parks so they show the full description
            strippedParks = i.strip().split(",")    # stripping the parks of any commas
        else:
            description1 = i.find("\"")                        # finding the initial description of each park in loadFile
            fullDescription = i[description1:len(i) - 1]    # taking the whole string of the description of each parl
            keyValues = i.strip().split(",")                   # stripping the park description of the "," to show the full description
            for j in range(len(strippedParks)):
                newPark[strippedParks[j]] =  keyValues[j]     # for each new park1 we take the stripped description
            newPark["Description:"] = fullDescription             # for the newPark we will use the full description
            parkList.append(newPark)                             # adding the description to the park in our parkList
        counter = counter + 1

    return parkList


def getDate(dataStr):
    # the below statement initializes all of the months that are linked to the numerical value of the month

    months = {}   # initializing our dictionary of months
    months[1] = "January"
    months[2] = "February"
    months[3] = "March"       # adding each month and the numerical key into the dictionary
    months[4] = "April"
    months[5] = "May"
    months[6] = "June"
    months[7] = "July"
    months[8] = "August"
    months[9] = "September"
    months[10] = "October"
    months[11] = "November"
    months[12] = "December"
    splitDates = dataStr.split("-")   # this separates by "-" from the format YYYY-MM-DD

    year = splitDates[0]
    month = months[int(splitDates[1])]
    day = splitDates[2]
    date = month + " " + day + ", " + year    # converts the new splitDates into our new format to read

    return date


def getLargestPark(parksList):
    largestArea = 0  # initializing the largest parks area to 0, so there will at least be one park larger than it
    largestCode = ""     # initializing the largest parks code
    for i in parksList:
        if int(i["Acres"]) > largestArea:    # if the new park in the for loop is larger the the previous largest...
            largestCode = i["Code"]          # replace the old largest code with the new parks code
            largestArea = int(i["Acres"])    # and replace the largest area with the new parks area

    return largestCode
