#Jenna Smedley
#Level 03 Assignment -- Create 'Higher or Lower' game


play_again = "Y"
import random 

#Keep the game going until user stops it
while play_again == "Y" or play_again == "y":
    
    #Game setup
    print("Welcome to the game! May the odds be ever in your favor.")
    print("I'm thinking of a number between 1 and 100. Try and guess what it is!")
    secret_num = random.randint(1,100)
    guess = int(input("Guess a number between 1 and 100: "))
    num_of_guesses = 1

    #Responses to guesses
    while guess != secret_num:
        if guess > secret_num:
                    print("Try again, guess lower!")
                    num_of_guesses += 1
        elif guess < secret_num:
                    print("Try again, guess higher!")
                    num_of_guesses += 1
        guess = int(input("Guess a number between 1 and 100: "))

    #User wins
    print("Congratulations! You guessed correctly.")
    print(f"You found my number in {num_of_guesses} guesses.")
    if num_of_guesses <= 3:
        print("Incredible!")
        play_again = input("Would you like to play again? (Y/N) ")
    elif num_of_guesses <= 5:
        print("Excellent!")
        play_again = input("Would you like to play again? (Y/N) ")
    elif num_of_guesses <= 7:
        print("Well done!")
        play_again = input("Would you like to play again? (Y/N) ")
    elif num_of_guesses <= 9:
        print("You got it!")
        play_again = input("Would you like to play again? (Y/N) ")
    elif num_of_guesses >=10:
        print("Lock in bro.")
        play_again = input("Would you like to play again? (Y/N) ")

#Ending
print("Goodbye!")
