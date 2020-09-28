#Danny Rigdon - 09/22/2020
#HW06 - Car Rental / Program

#Declare/initialize variables and CONSTANTS

BASE_CHARGE = 65
totalCharge = 0
daysRent = 0
custFName = ""
custLName = ""
carType = ""
userAnswer = ""
userAnswerTwo = ""

#Does the user want to rent a car today?

userAnswer = input("Hello! Would you like to rent a vehicle today? (Yes or No) ")

if userAnswer == "YES":
    print("Great! Let's get started.")
    print('\n')
elif userAnswer == "Yes":
    print("Great! Let's get started.")
    print('\n')
elif userAnswer == "yes":
    print("Great! Let's get started.")
    print('\n')
elif userAnswer == "Y":
    print("Great! Let's get started.")
    print('\n')
elif userAnswer == "y":
    print("Great! Let's get started.")
    print('\n')
    
else:
    print("Thank you for your consideration. Have a great day!") + quit()
    
#Prompt the user for their name.

custFName = input("Please enter your first name. ")
print("Hello " + str(custFName + "!"))
print('\n')

custLName = input("Please enter your last name. ")
print("Thank you for providing that information, " +str(custFName + "."))
print('\n')


#Prompt the user for the number of days that the vehicle is needed.

daysRent = int(input("How many days will you need the vehicle you're renting? (example: 14) "))
print("You will be renting the vehicle for " + str(int(daysRent)) + " day(s).")
print('\n')
    
#What kind of vehicle does the user want to rent?

print("--------------------------------------------------------------------------------------------")
print("Vehicle Type Pricing (including additional fees):")
print('\n')
print("Base Charge For Any Rental - $" + str(int(BASE_CHARGE)))
print('\n')
print("Compact - $" + str(int(BASE_CHARGE)) + " (no additional fees)")
print("Standard - $" + str(int(BASE_CHARGE)) + " + ($10.00 fee)")
print("SUV - $" + str(int(BASE_CHARGE)) + " + ($15.00 fee)")
print("Van - $" + str(int(BASE_CHARGE)) + " + ($25.00 fee)")
print('\n')
print("All rental types qualify for a 20% discount if the rental period is longer than seven days.")
print("--------------------------------------------------------------------------------------------")

while userAnswer != "No" or "no":
    carType = input("Please choose between the following vehicle types: Compact, Standard, SUV, or Van. ")

    if carType == "Compact":
        print("Great choice! Our compact vehicles are an excellent value.")
        print('\n')
        break
    elif carType == "compact":
        print("Great choice! Our compact vehicles are an excellent value.")
        print('\n')
        break
    elif carType == "Standard":
        print("Our standard vehicles are great. There is an additional fee of $10.00 for this selection.")
        print('\n')
        break
    elif carType == "standard":
        print("Our standard vehicles are great. There is an additional fee of $10.00 for this selection.")
        print('\n')
        break
    elif carType == "SUV":
        print("This is an excellent choice! There is an additional fee of $15.00 for this selection.")
        print('\n')
        break
    elif carType == "Suv":
        print("This is an excellent choice! There is an additional fee of $15.00 for this selection.")
        print('\n')
        break
    elif carType == "suv":
        print("This is an excellent choice! There is an additional fee of $15.00 for this selection.")
        print('\n')
        break
    elif carType == "Van":
        print("That is a spacious choice! There is an additional fee of $25.00 for this selection.")
        print('\n')
        break
    elif carType == "van":
        print("That is a spacious choice! There is an additional fee of $25.00 for this selection.")
        print('\n')
        break

    else:
        print("We do not currently offer that vehicle type.")
        print('\n')
        continue

#Allow the user to confirm their choice of vehicle type.
    
userAnswerTwo = input("Are you sure you'd like to rent this vehicle type: " + str(carType + "? " + "(Yes or No) "))
print("\n")

if userAnswerTwo == "NO":
    carType = input("Please choose between the following vehicle types: Compact, Standard, SUV, or Van. ")
    print("\n")
elif userAnswerTwo == "No":
    carType = input("Please choose between the following vehicle types: Compact, Standard, SUV, or Van. ")
    print("\n")
elif userAnswerTwo == "no":
    carType = input("Please choose between the following vehicle types: Compact, Standard, SUV, or Van. ")
    print("\n")
elif userAnswerTwo == "N":
    carType = input("Please choose between the following vehicle types: Compact, Standard, SUV, or Van. ")
    print("\n")
elif userAnswerTwo == "n":
    carType = input("Please choose between the following vehicle types: Compact, Standard, SUV, or Van. ")
    print("\n")

#Calculate total charge and fees.
    
#Additional fees = Standard(10), SUV(15), Van(25)
#If renting for more than (7) days, subtract 20% of total cost
    
print("Thank you for your selection!")
print("Please wait while we calculate your total cost.")
print(".")
print(".")
print(".")

if carType == "Compact":
    totalCharge = BASE_CHARGE
elif carType == "compact":
    totalCharge = BASE_CHARGE
elif carType == "Standard":
    totalCharge = BASE_CHARGE + 10
elif carType == "standard":
    totalCharge = BASE_CHARGE + 10
elif carType == "SUV":
    totalCharge = BASE_CHARGE + 15
elif carType == "Suv":
    totalCharge = BASE_CHARGE + 15
elif carType == "suv":
    totalCharge = BASE_CHARGE + 15
elif carType == "Van":
    totalCharge = BASE_CHARGE + 25
elif carType == "van":
    totalCharge = BASE_CHARGE + 25
    
if daysRent > 7:
    totalCharge = totalCharge - (totalCharge * .20)
    
#Display transaction details with a total charge.

print("Here are your transaction details:")

print("----------------------------------")

print("Customer Name: " + str(custFName + " " + custLName))
print("Number of Days Renting: " + str(int(daysRent)))
print("Vehicle Type: " + str(carType))
print("Total Bill : " + "$" + str(totalCharge))

print("\n")

print("Thank you, we appreciate your business! Please drive safely.") + quit()