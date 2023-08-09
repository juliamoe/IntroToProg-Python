# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JMoekkoenen,8/8/2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

objFile=open(objFile,"r") #reading the .txt file in the folder
for row in objFile:
    lstRow=row.split(",")
    dicRow={"Task":lstRow[0],"Priority":lstRow[1].strip()}  #creating a dictionary
    lstTable.append(dicRow) #making the dictionary rows a table


objFile.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):

        print(lstTable) #prints out the data

        continue

    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):

        while(True):
            strTask=input("Task: ")
            strPriority=input("Priority: ")
            lstTable.append({"Task":strTask,"Priority": strPriority}) #adding the user input data into the dictionary
            strdes=input("Are you done adding data? (y/n)") #desicion on if user is done adding items
            if strdes=="y":
                break
        continue

    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):

        strTask = input("Enter the Item to Remove:")
        for row in lstTable:
            if row["Task"].lower() == strTask.lower(): #looking for the match for user input
                lstTable.remove(row) #removes the chosen task row
                print("Row removed")
            else:
                print("Row not found")
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):

        objFile = open("ToDoList.txt","w")
        for row in lstTable:
            objFile.write(str(row["Task"])+","+str(row["Priority"]+"\n")) #saving each row into the .txt file
        objFile.close()
        print("Changes have been saved!")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        strExit=input("Are you sure you want to exit the program? (y/n)")
        if strExit=="y":
            print("Program closing...")
            break #Exit the program
        else:
            continue # looping back to the menu
