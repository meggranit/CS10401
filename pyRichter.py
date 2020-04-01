#PYTHON RICHTER SCALE CALCULATION
#Your first and last name: Meghan Granit
#Your ID: s1265607

#REQUIREMENTS:
# ask the user to "Enter the Richter scale value or -99 to end: "
# the program must end when the user enters -99
# the richter scale value entered must be greater than 0
# if the richter scale value is less than 0, the program must print  "Value must be greater than 0"
#   and the user must re-enter the richter scale value
# program must print the correct warning message for the richter scale value entered as per the accompanying diagram
# program must print only 1 warning message for each richter scale value entered
# the program must be tested so that it repeats until user enters -99
# the program must be tested so that if user enters a richter scale value less than 0,
#   "Value must be greater than 0" prints and the user must re-enter it
# the program must be tested with each of the following values to make sure the correct warning message is printed
#    8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6
#-------------------------------------------------------------------------

# HINT: Use the base number conversion program for guidance
#--------------------------------------------------------------------------------------------
# 1. Develop the ALGORITHM for Richter Scale program from the requirements and enter it below
#--------------------------------------------------------------------------------------------
#user input line
#if else statements assigning actions based on input number
#put code on loop until user inputs -99
#print warning sign for each richter scale value
#if input less than 0, must display message to re-enter value
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 2. Convert the ALGORITHM to PSEUDOCODE and enter it below
#-------------------------------------------------------------------------
#input number
#if value is -99, end program
#if any other number, repeat program until -99 is input
#if value is less than 0, display "Value must be greater than 0" and prompt user to re-enter
#if value is greater than or equal to 8.0, "Most structures fall"
#if value is greater than or equal to 7.0, "Many buildings destroyed"
#if value is greater than or equal to 6.0, "Many buildings considerably damaged, some collapse"
#if value is greater than or equal to 4.5, "Damage to poorly constructed buildings"
#else, "No destruction of buildings"
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
# 3. Convert the PSEUDOCODE into PYTHON CODE and enter it below
#-------------------------------------------------------------------------
i=0
while i<1:
    richter=float(input("Enter the Richter scale value or -99 to end:" ))
    if (richter==-99):
        i=1
    elif (richter>=8):
        print("Most structures fall")
        i=0
    elif (richter>=7):
        print("Many buildings destroyed")
        i=0
    elif (richter>=6):
        print("Many buildings considerably damaged, some collapse")
        i=0
    elif (richter>=4.5):
        print("Damage to poorly constructed buildings")
        i=0
    elif(richter<0):
        print("Value must be greater than 0")
        i=0
    else:
        print("No destruction of buildings")
        i=0
    
