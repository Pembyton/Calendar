while True: #here makes it repeat
    year = int(input("please type the year of today. ")) #here takes the year
    month = int(input("please type the month of today in numbers please don't put any 0s except for 10.")) #here takes the month
    date = int(input("please type the date of today. ")) # here takes the date
    if month == (1): # here transform the number of month into actual month's name
        Month = "January"
    if month == (2):
        Month = "February"
    if month == (3):
        Month = "March"
    if month == (4):
        Month = "April"
    if month == (5):
        Month = "May"
    if month == (6):
        Month = "June"
    if month == (7):
        Month = "July"
    if month == (8):
        Month = "August"
    if month == (9):
        Month = "September"
    if month == (10):
        Month = "October"
    if month == (11):
        Month = "November"
    if month == (12):
        Month = "December"
    if month == 1: #here makes sure the date don't have weird dates like january 0, also prints the actual thing
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 2:
        if date >= 1:
            if date <= 28:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 3:
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 4:
        if date >= 1:
            if date <= 30:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 5:
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 6:
        if date >= 1:
            if date <= 30:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 7:
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 8:
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 9:
        if date >= 1:
            if date <= 30:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 10:
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 11:
        if date >= 1:
            if date <= 30:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month == 12:
        if date >= 1:
            if date <= 31:
                if year >= 0:
                    print("Today is" , year , "," , Month , date)
    if month >= 13: #here makes sure there are only 12 months and prints the ERROR
        print("ERROR")
    if month <= 0:
        print("ERROR")
    if month == 1: #here makes sure there aren't any weird dates and print the ERROR if there is any
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if month == 2:
        if date <= 0:
            print("ERROR")
        if date >=29:
            print("ERROR")
    if month == 3:
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if month == 4:
        if date <= 0:
            print("ERROR")
        if date >= 31:
            print("ERROR")
    if month == 5:
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if month == 6:
        if date <= 0:
            print("ERROR")
        if date >= 31:
            print("ERROR")
    if month == 7:
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if month == 8:
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if month == 9:
        if date <= 0:
            print("ERROR")
        if date >= 31:
            print("ERROR")
    if month == 10:
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if month == 11:
        if date <= 0:
            print("ERROR")
        if date >= 31:
            print("ERROR")
    if month == 12:
        if date <= 0:
            print("ERROR")
        if date >= 32:
            print("ERROR")
    if year <= -1: #here makes sure the year can't be negative and if it is, print ERROR
        print("ERROR")
