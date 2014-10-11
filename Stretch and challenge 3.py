#Indi Knighton
#11/10/2014
#This programme will take three separate integers and display the date with them

month = int(input("Please enter a number between 1-12: "))
day = int(input("Please enter a number between 1-31: "))
year = int(input("Please enter the year in numbers here: "))

if 1931 < year > 2030:
    print("You have entered an invalid year")
elif month == 1:
        print("The month you entered is {0} January {1}".format(day, year))
elif month == 2:
        print("The month you entered is {0} February".format(day, year))
elif month == 3:
        print("The month you entered is {0} March {1}".format(day, year)) 
elif month == 4:
        print("The month you entered is {0} April {1}".format(day, year))
elif month == 5:
        print("The month you entered is {0} May {1}".format(day, year))
elif month == 6:
        print("The month you entered is {0} June {1}".format(day, year))
elif month == 7:
        print("The month you entered is {0} July {1}".format(day, year))
elif month == 8:
        print("The month you entered is {0} August {1}".format(day, year))
elif month == 9:
        print("The month you entered is {0} September {1}".format(day, year))
elif month == 10:
        print("The month you entered is {0} October {1}".format(day, year))
elif month == 11:
        print("The month you entered is {0} November {1}".format(day, year))
elif month == 12:
        print("The month you entered is {0} December {1}".format(day, year))
    
    
