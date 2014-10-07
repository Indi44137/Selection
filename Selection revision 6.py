#Indi Knighton
#06/10/2014
#This program asks for three numbers and displays the largest one

number1 = int(input("Please enter a number here: "))
number2 = int(input("Please enter a different number here: "))
number3 = int(input("Please enter a third different number here: "))

if number1 > number2 and number3:
    print("{0} is larger then {1} and {2}".format(number1, number2, number3))
elif number3 > number1 and number1:
    print("{0} is larger then {1} and {2}".format(number3, number2, number1))
else:
    print("{0} is larger then {1} and {2}".format(number2, number1, number3))
