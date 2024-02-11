import random
import math

def get_integer_input(prompt):
    while True:
        value = input(prompt)
        if value:
            try:
                return int(value)
            except ValueError:
                print("Please enter a valid integer.")

while True:
    lower = get_integer_input("Enter the lower range number: ")
    upper = get_integer_input("Enter the upper range number: ")

    x = random.randint(lower, upper)
    calc = round(math.log(upper - lower + 1, 2))
    print(f"You have {calc} chances to guess the integer!\n")
    # message = f'''do you want to try it for {calc} times or you want to try it for max 3 times ? please select'''
    if calc >= 6:
        # print(message)
        print("we are allowing max 4 attempts as the choice came more than 6 \n")
        calc = 4
        print(f"Now You have {calc} chances to guess the integer!\n")
    count = 0

    while count < calc:
        count += 1
        guess = get_integer_input("Guess the Number: ")

        if x == guess:
            print(f"Congratulations, you have guessed it in {count} try.")
            break
        else:
            if x > guess:
                print("You guessed too small!")
            elif x < guess:
                print("You guessed too high!")

    if x != guess:
        print(f"\nBetter Luck Next time! The number is {x}")

    play_again = input("Do you want to continue playing? If yes, enter 'Y'. Press any other key to exit: ")
    
    if play_again.upper() != 'Y':
        break
    