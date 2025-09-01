import random

print("Number Guessing Game")

# Random number between 1 and 9
number = random.randint(1, 99)

# Number of chances
max_chances = 5
chances = 0

print("Guess a number (between 1 and 99):")

# While loop to count the number of chances
while chances < max_chances:
    try:
        # Get user input
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Please enter a valid number between 1 and 9.")
        continue

    # Increase chance count
    chances += 1

    if guess == number:
        print(f"CONGRATULATIONS! YOU GUESSED THE NUMBER {number} IN {chances} ATTEMPTS!")
        break

    remaining = max_chances - chances

    if remaining == 0:
        print(f"Sorry, you've used all your chances. The number was {number}. Better luck next time!")
        break
    else:
        if guess < number:
            print("Your guess was too low: Guess a number higher than", guess)
        else:
            print("Your guess was too high: Guess a number lower than", guess)

        print(f"You have {remaining} {'chance' if remaining == 1 else 'chances'} left.\n")
