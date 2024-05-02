import random

print("Hello, Welcome to Guessing game!\n Choose a number between 1 to 100")

lower_number = int(input('Enter a lower range'))
higher_number = int(input('Enter a higher range'))

guess_number = random.randint(lower_number, higher_number)
number_of_guesses = random.randint(1,7)

print(f"You have {number_of_guesses} of guesses")
count = 0

while count < number_of_guesses:
    count +=1
    guess = int(input("Guess the random number: "))

    if guess == guess_number:
       print("Congratulations, you guessed correctly in ",count, "try" )
       break 
    elif guess > guess_number:
        print("You guessed is too high")
    elif guess < guess_number:
        print('Your guess is too small')

if count >= number_of_guesses:
    print("The number is", guess_number)
    print("Game Over, Try again next time")

