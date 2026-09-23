# CHAPTER FIVE
# to the power of
calculation = 2 ** 8
print(calculation)

# mod
calculation1 = 5 % 3
print(calculation1)

#division
calculation2 = 5 / 3
print(calculation2)

#floor division (returnrs quotient)
calculation3 = 5 // 3
print(f"The result is: {calculation3}")

# bank rounding (if it's a .5, it always rounds to the nearest even number)
calculation4 = round(2.5)
print(calculation4)

# abbreviated arithmetic
account_balance = 1000.00
account_balance += 100 # deposit
print("Account balance is : $" + str(account_balance))

#result of comparison is boolean
comparison = (5 > 3) and (4 == 4) and (2 > 3)
print(comparison)

# CHAPTER 6

age = int(input("Enter your age: "))

if age >= 40:
    print("You are over the hill!")
else:
    print("You are still young!")

if age >= 40:
    print("ur old")
elif age < 40 and age >= 0:
    print("u are still young")
elif age < 0:
    print("age cannot be negative")

if age < 0:
    print("age cannot be negative")
elif age < 40:
    print("u are still young")
elif age >= 40:
    print("ur old")
else:
    print("Invalid input!")

