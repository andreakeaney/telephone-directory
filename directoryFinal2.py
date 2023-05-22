"""
***Documentation***
Name of File: directory.py
Author: Andrea Keaney
Date: 26-04-23
Description: This application is password protected. It holds data inc first name, last name, phone number, sex and address in a txt file. It reads data from the text file
that has a list of first names, a list of last names, a list of sex [m/f], a list of telephone numbers and a list of addresses.
The application is menu driven as follows:
1 - Add new contact (prompts to enter number of contacts, first name, last name, sex, telephone number and address.
It will then hold the data in 5 separate lists. Ie firstNames[], lastNames[], sex[], telNum[], address[])
2 - Display all contacts
3 - Search contact by name by entering 1+ letters (Eg by entering the letter 'A' the program will
list all names that start with 'A' such as Andrew, Andrea, Agnes.
The more letters entered, the more refined the results of the search will be. Eg entering 'An' will return Andrew, Andrea only)
4 - Search contact by number
5 - Remove a contact by name (Removes a contact by name and removes all associated data)
6 - Remove a contact by number (Removes a cntact by number and removes all associated data)
7 - Exit program (Saves the current list in the txt file, overwrites by adding new entries, removing rows from deleted entries)
==================Stages of building this code======================
1. Created layout of all functions
2. Coded password() function to include countdown of attempts left to guide user.
3. Tested password() using incorrect attempts.
*a. Expected result: Password is incorrect! Please try again. You have {remainingAttempts} attempts left.
*b. Actual Result: as expected
4. Tested password() using correct password
*a. Expected result: "i'm in menu"
*b. Actual result: As expected
5. Created lists for:
   firstNames=[]
   lastName=[]
   age=[]
   sex=[]
   telNum=[]
   address=[]
6. Code readData()
7. Test by pring all data
8. Code menu()
9. Test by seeing if menu displays all options
10. Code addNew()
11. Test
"""
#start program
def main():
    password()
    firstNames=[]
    lastNames=[]
    ages=[]
    sexes=[]
    telNums=[]
    addresses=[]
    readData(firstNames,lastNames,ages,sexes,telNums,addresses)

#call menu() function
    menu(firstNames,lastNames,ages,sexes,telNums,addresses)

#======================prompt user for password
"""def password():
   for x in range (3):
       enteredPassword = input("Please enter password to continue:\n")
       remainingAttempts = 2-x
       if enteredPassword != "clydecollege1":
           print(f"Password is incorrect! Please try again. You have {remainingAttempts} attempts left.")
       if enteredPassword == "clydecollege1":
           menu(firstNames, lastNames, ages, sexes, telNums, addresses)"""
def password():
    for x in range (3):
        enteredPassword = input("Please enter password to continue:\n")
        remainingAttempts = 2-x
        if enteredPassword != "clydecollege1":
            print(f"Password is incorrect! Please try again. You have {remainingAttempts} attempts left.")           
        elif enteredPassword == "clydecollege1":
            print("correct!")
            break
    if remainingAttempts == 0:
        print("You've exceeded 3 attempts. The program will exit")
        exit(0)

#Display a menu and prompts user to select an option (1-7)
def menu(firstNames,lastNames,ages,sexes,telNums,addresses):
   while True: #loop forever until we choose to stop
       print(
       "1-\tAdd new contact\n"
       "2-\tDisplay all contacts\n"
       "3-\tSearch contact by name by entering 1+ letters\n"
       "4-\tSearch contact by number\n"
       "5-\tRemove a contact by name\n"
       "6-\tRemove a contact by number\n"
       "7-\tExit Program and Save Data\n")
       selection = int(input("Please select an option from the menu above (1-7):\n"))

       if(selection==1): #add new
           numContacts = int((input("Enter number of contacts to be added: \n")))
           #call inputdata() function passing number students, names, marks and grades variables
           inputData(firstNames,lastNames,ages,sexes,telNums,addresses,numContacts)

       elif(selection==2): #display all contacts
         
           if(len(firstNames)==0):
               input("Your contact list is empty. Press Enter to continue!")
           else:
               for z in range(len(firstNames)):
                   print(f"Name:\t\t{firstNames[z]} {lastNames[z]}\nAge:\t\t{ages[z]}\nSex:\t\t{sexes[z]}\nTelNum:\t\t{telNums[z]}\nAddress:\t{addresses[z]}\n\n")
           input("Press Enter to continue!")
         
       elif(selection==3): #search by name
           searchName(firstNames,lastNames,ages,sexes,telNums,addresses)

       elif(selection==4): #search by number
           searchNum(firstNames,lastNames,ages,sexes,telNums,addresses)
   
       elif(selection==5): #remove by name
           removeName(firstNames,lastNames,ages,sexes,telNums,addresses)

       elif(selection==6): #remove by name
           removeNum(firstNames,lastNames,ages,sexes,telNums,addresses)

       elif(selection==7): #exit and save data
           saveExit (firstNames,lastNames,ages,sexes,telNums,addresses)
           print("Thank you and Bye!")
           exit(0)

#======================read data from txt file  
def readData(firstNames,lastNames,ages,sexes,telNums,addresses):
       #start reading data in text file [telData.txt] line by line to populate the lists [firstNames,lastNames,age,sex,telNum,address]
   with open("telData2B.txt","r") as myFile: #open file for read only
       for eachLine in myFile: #loop through the text file line by line
           #print(f" {eachLine}")
           detailsOfLine=eachLine.split(",") #split each line read into 3 separate elements separated by commas [0,1,2] using the split() function
           #this function returns a list                #2 commas gives 3 elements
           firstNames.append(detailsOfLine[0]) #add index 1 to names list
           lastNames.append(detailsOfLine[1]) #add index 2 to marks list
           ages.append(detailsOfLine[2]) #add index 3 to grades list and strip off the 'new line' special character
           sexes.append(detailsOfLine[3])
           telNums.append(detailsOfLine[4])
           addresses.append(detailsOfLine[5].strip("\n"))

#=========================add a new contact  
def inputData(firstNames,lastNames,ages,sexes,telNums,addresses,numContacts):
   for x in range (numContacts): #loop as many times as number of students
       firstName=input("Please enter first name:\n")
       firstNames.append(firstName)
       lastName=input("Please enter last name:\n")
       lastNames.append(lastName)
       sex=input("Please enter sex [m/f]:\n")
       sexes.append(sex)
       age=int(input("Please enter age in years:\n"))
       ages.append(age)
       telNum=input("Please enter telephone number using numbers only:\n")
       telNums.append(telNum)
       address=input("Please enter full address including postcode:\n")
       addresses.append(address)

##=================search contacts by name/part of name
def searchName(firstNames,lastNames,ages,sexes,telNums,addresses):
   found=bool(False) #found variable will change to true if name exists
   letters=input("Enter a letter or more of the student's name to be searched:\n")
   i=0
   while i<len(firstNames):
       if firstNames[i].find(letters.capitalize(),0,len(letters))!=-1 or \
               firstNames[i].find(letters.lower(),0,len(letters))!=-1:
                 print(f"Name: {firstNames[i]} {lastNames[i]}\t Age: {ages[i]}\t Sex: {sexes[i]} Telephone Number: {telNums[i]} Address: {addresses[i]}")
                 found=bool(True)
       i=i+1
   if found ==bool(False):
       print(f"Sorry, no contacts matching {letters}")
   input("Please hit Enter to continue")

#search contacts by number/part of number
def searchNum(firstNames,lastNames,ages,sexes,telNums,addresses):
   found=bool(False) #found variable will change to true if name exists
   numbers=input("Enter a number or more of the contact to be searched:\n")
   i=0
   while i<len(telNums):
       #if telNums[i].find(numbers(),0,len(numbers))!=-1 or telNums[i].find(numbers.lower(),0,len(numbers))!=-1:
       if telNums[i].__contains__(numbers):
                 print(f"Name: {firstNames[i]} {lastNames[i]}\t Age: {ages[i]}\t Sex: {sexes[i]} Telephone Number: {telNums[i]} Address: {addresses[i]}")
                 found=bool(True)
       i=i+1
   if found ==bool(False):
       print(f"Sorry, no contacts matching {numbers}")
   input("Please hit Enter to continue")

#search by name for contact and delete contact and all relevant information  
def removeName(firstNames,lastNames,ages,sexes,telNums,addresses):
   if len(firstNames) == 0:
       input("There are no students available. Hit Enter To Continue.")
   else:
       nameToBeRemoved = input("Please Enter Name Of Contact To Be Removed: \n")
                             
       if nameToBeRemoved in firstNames:
                 
           index = firstNames.index(nameToBeRemoved)
           del firstNames[index]
           del lastNames[index]
           del ages [index]
           del sexes [index]
           del telNums [index]
           del addresses [index]
         
           input(f"{nameToBeRemoved} Was Successfully Removed. Hit Enter To Continue.")
       else:
           print(f"{nameToBeRemoved} does not exist.")
           input("Hit Enter To Continue.")

#search by number for contact and delete contact and all relevant information  
def removeNum(firstNames,lastNames,ages,sexes,telNums,addresses):
   if len(firstNames) == 0:
       input("There are no students available. Hit Enter To Continue.")
   else:
       numToBeRemoved = input("Please Enter Telephone Number Of Contact To Be Removed: \n")
                             
       if numToBeRemoved in telNums:
                 
           index = telNums.index(numToBeRemoved)
           del firstNames[index]
           del lastNames[index]
           del ages [index]
           del sexes [index]
           del telNums [index]
           del addresses [index]
         
           input(f"Contact With Tel Num: {numToBeRemoved} Was Successfully Removed. Hit Enter To Continue.")
       else:
           print(f"{numToBeRemoved} does not exist.")
           input("Hit Enter To Continue.")

#save all changes to file and exit program
def saveExit(firstNames,lastNames,ages,sexes,telNums,addresses):
   with open("telData2B.txt", "w") as f:
       for i in range(len(firstNames)):
           f.write(f"{firstNames[i]},{lastNames[i]},{ages[i]},{sexes[i]},{telNums[i]},{addresses[i]}\n")  

#call the main function
if __name__ == "__main__":
   main()    