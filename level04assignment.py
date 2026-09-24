# Jenna Smedley
# Level 04 Assignment: Personal Expense Analyzer

# create list
expenses = []

# ask user for expenses
while True:
    expense = float(input("Enter an expense or 0 to finish: "))
    if expense < 0:
        print("Invalid input.")
    if expense == 0:
        break
    if expense > 0:
        expenses.append(expense)

# classify expenses
small_expense = []
mid_expense = []
large_expense = []
for num in expenses:
    if num < 25:
        small_expense.append(num)
    elif num < 100:
        mid_expense.append(num)
    else:
        large_expense.append(num)

# print summary
print("Expense Summary")
print(f"Number of expenses: {len(expenses)}")
print(f"Total: ${sum(expenses):,.2f}")
print(f"Average: ${sum(expenses)/len(expenses):,.2f}")
print(f"Smallest expense: ${min(expenses):,.2f}")
print(f"Largest expense: ${max(expenses):,.2f}")
print(f"Small expenses: {len(small_expense)}")
print(f"Medium expenses: {len(mid_expense)}")
print(f"Large expenses: {len(large_expense)}")

