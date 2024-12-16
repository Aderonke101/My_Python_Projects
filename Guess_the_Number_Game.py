import random
def guess_the_number_game():
    #Generate a random number between 1and 100
    number_to_guess = random.randint(1,100)
    attempts = 100
    print("welcome to the Guess the Number Game!")
    print(f"You have {attempts} attempts to guess the number betwen 1 and 100.")

    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"congratulations! you guessed the number {number_to_guess} correctly in {attempt} attempts.")
            break
    else:
        print(f"sorry, you've used all {attempts} attempts. The correct number was {number_to_guess}.")
guess_the_number_game()

