# pseudo code for our higher lower game!

#playagain = y
#while the user has pressed "y"
    # computer generates a random number between 1 and 100

    # While the user has not guessed the number
        # ask the user for a guess between 1 and 100

        # while the guess is less than 1 or greater than 100, print "invalid guess"

        # increment the number of guesses

        # if the guess is greater than the number, "guess lower"
        # if the guess is less than the number, "guess higher"

    # loop

    # print "congrats!"
    # print the number of guesses

    # if num of guesses < 3
        # print 'you are amazing!'
    # (etc etc)

    # ask the user to press "y" if they want to play again
#loop


negatives = 0
positives = 0
zeros = 0
numbers = [5, 16, -3, 0, 12]
for i in (0,4):
    current_number = numbers[1]
    if current_number == 0 :
        print(f"Number {current_number} is zero.")
        zeros += 1
    elif current_number < 0 :
        print(f"Number {current_number} is negative.")
        negatives += 1
    elif current_number > 0 :
        print(f"Number {current_number} is positive.")
        positives += 1
print(f"Positives: {positives}")
print(f"Negatives: {negatives}")
print(f"Zeroes: {zeros}")