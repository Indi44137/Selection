#Indi Knighton
#08/10/2014
#Programme stating whether water is boiling, frozen or neither

temperature_of_water = int(input("Please enter the temperature of your water here: "))

if temperature_of_water <= 0:
    print("Your water is frozen")
elif temperature_of_water > 100:
    print("Your water is boiling")
else:
    print("Your water is neither boiling or frozen")
