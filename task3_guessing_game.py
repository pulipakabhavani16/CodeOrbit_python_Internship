# CodeOrbit Internship - Task 3
# Number Guessing Game

import random

print("===== Number Guessing Game =====")

while True:
    number = random.randint(1, 100)
    attempts = 0

    print("\nI have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < number:
                print("Too Low! Try Again.")
            elif guess > number:
                print("Too High! Try Again.")
            else:
                print("🎉 Congratulations! You guessed the correct number.")
                print("Total Attempts:", attempts)
                break

        except ValueError:
            print("Please enter a valid number.")

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thank you for playing!")
        break