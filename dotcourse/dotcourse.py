import pandas as pd 
allBooks = []
flag = True
while flag:
    bookName = input("the name of ur book : ")
    bookPageNumber = input("the number of pages in ur book : ")
    bookpublishedDay = input("the day ur book was published : ")
    bookpublishedMonth = input("the month ur book was published : ")
    bookpublishedYear = input("the year ur book was published : ")
    bookpublished = f"{bookpublishedDay}/{bookpublishedMonth}/{bookpublishedYear}"

    currentBook = {'name' : [bookName], 'pages' : [bookPageNumber], 'published' : [bookpublished]}
    allBooks.append(currentBook)
    df = pd.DataFrame(allBooks)
    print(df)

    updatFlag = input("do u want to update the book info ? (y/n) : ")
    if updatFlag == 'n':
        flag = False