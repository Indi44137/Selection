#Indi Knighton
#09/10/2014
#This programme will work out your gross wages and display them. 

hours_worked = float(input("Please enter the amount of hours you work per week here: "))
hourly_pay_rate = float(input("Please enter how much you get payed per hour: "))

import math

overtime_pay = (hours_worked - 40) * 1.5
weekly_pay_rate1 = hours_worked * hourly_pay_rate
weekly_pay_rate2 = overtime_pay + weekly_pay_rate1

if hours_worked > 60:
    print("You have entered an invalid number. Please try again")
elif hours_worked < 0:
    print("You have entered an invalid number. Please try again")
elif hours_worked > 40:
    print("Your weekly pay is £{0}".format(weekly_pay_rate2))
else:
    print("Your weekly pay is £{0}".format(weekly_pay_rate1))

    

    
    

