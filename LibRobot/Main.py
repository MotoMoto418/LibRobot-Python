from ValidityCheck import *
from FileOps import *


flag = False
while flag ==  False:
    action = input("\nEnter: \n1) search - To search for a book. \n2) update - To update the database. \n3) view - To view the database. \n4) quit - To quit the program. \n").lower()
   
    if action == "search":
        ISBN = input("\nPlease enter a valid ISBN code: ").upper()
        print(search(ISBN))
        print("\nThank you for using this program. ")
        flag = True

    elif action == "update":
        
        flag2 = False
        while flag2 == False:
            book = input("\nEnter the book's name: ")
            author = input("Enter the author's name: ")
            year = input("Enter the year of publication: ")
            publisher = input("Enter the publisher's name: ")
            ISBN = input("Enter the valid ISBN code: ")
            
            if vCheck(ISBN):
                print(update(book, author, year, publisher, ISBN))
                print("\nThank you for using this program. ")
                flag = True
                flag2 = True
            
            else:
                print("\nInvalid ISBN. ")

        
    elif action == "view":

        file1 = open("isbnData.txt", "r")

        dataList = []
        for line in file1:
            dataList.append(line.strip().split("    "))

        file1.close()

        print("|            BOOK           |        AUTHOR         |  YEAR   |           PUBLISHER            |    ISBN     |")
        for item in dataList:
            print("|", item[0], " "*(24-len(item[0])), "|",item[1], " "*(20-len(item[1])), "|", item[2], " "*(6-len(item[2])), "|", item[3], " "*(29-len(item[3])), "|", item[4], " "*(10-len(item[4])), "|")
        print("\nThank you for using this program. ")
        flag = True

    elif action == "quit":
        print("\nThank you for using this program. ")
        flag = True

    else:
        print("\nInvalid entry. ")
        print("\nPlease try again. ")
