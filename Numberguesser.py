import random
print(" Welcome to the Number Guesser Game!")
low = int(input("Enter the lowest number: "))
high = int(input("Enter the highest number: "))
secret_number = random.randint(low, high)
print(f"I have chosen a number between {low} and {high}. Try to guess it.")
while True:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f" Congratulations! You guessed it right: {secret_number}")
        break
