# chapter SEVEN

#Definite loop = we know how many times we want it to run
#Indefinite = We don't know how many times it will run

for i in range(5): #Definite #i is the counter
    print(i)

for counter in range(100, 105): #Definite
    print(counter)

for counter1 in range(100, 106, 2): #Definite
    print(counter1)

for i1 in range(0, 101, 5): 
    print(i1)


age = int(input("How old are you? "))
print(age)

if age < 0:
    print("Invalid input. Please try again")
    age = int(input("How old are you? "))

while age < 0:
    print("You can't be negative years old!")
    age = int(input("How old are you really? "))


for count in range(1,6):
    print("Day 1, Appointment " + str(count))
for count1 in range(1,6):
    print("Day 2, Appointment " + str(count1))
for count2 in range(1,6):
    print("Day 3, Appointment " + str(count2))

for i in range(1,4):
    for j in range(1,6):
        print(f"Day {i}, Appointment {j}")
