These files allow the user to interact with a database of the 63 U.S. National Parks and request information from the index. Users can search for parks by state, size, or unique keywords.There are three files; main.py, interface.py, and tasks.py, which are summarized in the descriptions below.

TASKS.PY
- This file defines three functions that are used within our main.py and interface.py files
- Loads and transforms the national_parks(1).csv to remove commas from all the fields within the CSV file
- Defines a function that converts the numerical "Date" field into a string that displays the date in a written format
- Defines a function that returns the park with the largest area

INTERFACE.PY
- This file imports the tasks.py file in order to call relevant functions from that file
- Initializes a dictionary that serves as a options menu for how the user wants to ineteract with the park index
- Defines functions that prompt the user to select a state or input keywords to reference information from the database
- Defines functions that print the specific information requested by the user

MAIN.PY 
- This file imports the tasks.py and interface.py files in order to call functions from those files
- Defines and runs the main function for the national parks index by initializing the user input as well as creating the dictionary that is used as the menu of user options
- Until the user chooses the option to quit the program, it prompts the user and executes the relevant functions to report information from the database based off user input



