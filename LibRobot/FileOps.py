from ValidityCheck import *

def search(ISBN):
    
    file1 = open("isbnData.txt", "r")

    names = []
    authors = []
    years = []
    publishers = []
    isbn10 = []

    for data in file1:
        split = data.split("    ")
        names.append(split[0])
        authors.append(split[1])
        years.append(split[2])
        publishers.append(split[3])
        isbn10.append(split[4].strip())

    file1.close()

    flag = False

    if vCheck(ISBN):
        while flag == False:
            for isbn in isbn10:
                if ISBN == isbn:
                    index = isbn10.index(isbn)
                    flag = True
                    return "\nThe book you're looking for is '" + names[index] + "' written by " +  authors[index] +   " in " +  years[index] +  " published by " +  publishers[index] +  "."

                else:
                    continue

            if flag == False:
                return "\nThe ISBN you searched for wasn't found. "

    else:
        return "\nThe ISBN code you entered is invalid. "

def update(book, author, year, publisher, ISBN):
    
    file1 = open("isbnData.txt", "a")
    file1.write("\n" + book + "    " + author + "    " + year + "    " + publisher + "    " + ISBN)
    file1.close() 
    return "\nDatabase updated. "
        