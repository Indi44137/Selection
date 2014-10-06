#Indi Knighton
#06/10/2014
#This program asks for two numbers and displays the largest one

number1 = int(input("Please enter a number here: "))
number2 = int(input("Please enter a different number here: "))

if number1 > number2:
    print("{0} is larger then {1}".format(number1, number2))
else:
    print("{0} is larger then {1}".format(number2, number1))
