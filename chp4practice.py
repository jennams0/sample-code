#Jenna Smedley
# record name, addy, and age of person via inputs
sFirstName = input("Enter your first name: ")
sLastName = input("Enter your last name: ")
sStreetAddress = input("Enter your street address: ")
sCity = input("Enter your city: ")
sState = input("Enter your state: ")
sBirthYear = input("Enter your year of birth: ")

iBirthYear = int(sBirthYear)

print(sFirstName.upper(), sLastName.upper())
print(sStreetAddress)
print(sCity + " " + sState.upper())
print("In 2026", sFirstName, "was", 2026-iBirthYear, "years old")