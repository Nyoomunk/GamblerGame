import random

def hint_or_answer(guess, answer):
    if guess == answer:
        return ", you guessed right! 2 coins for you!"
    elif guess > answer:
        return ", you guessed too high... deducting a coin..."
    else:
        return ", you guessed too low... deducting a coin..."

purse = int(10)

while True:
    answer = random.randint(1, 10)

    print("You currently have", purse, "coins, if you win you get 2 coins, if you guess wrong you lose a coin. 15 coins = retirementville.")
    
    while True:
        try: 
            guess = int(input("Guess my number from 1 to 10! "))
            break   
        except: print("That's not a valid number!")

    message = hint_or_answer(guess, answer)
    print("You guessed:", guess, message)

    while guess != answer:
        purse = purse-1
        while True:
            try:
                guess = int(input("Guess again! "))
                break
            except:
                print("That's not a valid number! Deducting a coin for the idiocy...")
        message = hint_or_answer(guess, answer)
        print("You guessed:", guess, message)

    purse = purse+2

    if purse >= 15:
        print("You've won! Thanks for playing :D")
        break

    if purse == 0:
        print("Damn you're a degenerate gambler, bankrupt and hopeless, have fun living on the streets.")
        break

    print("You have:", purse, "coins.")
    play_again = input("Play again? y? ")
    if play_again != "y" :
        print("Thanks for playing!")
        break