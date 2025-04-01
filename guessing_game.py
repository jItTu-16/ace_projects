import random as ran

def game_number_guess():
    secret_num = ran.randint(1,100)
    print("Welcome to the Number guessing game!\nI have guessed a number between 0 and 100, can you guess the right...? \nYou got 7 guess.\n")
    for i in range(7):
        num = int(input(f"Enter your {i + 1} guess :- \n"))
        if num == secret_num:
            print(f"Congo!!! You Guessed the number {secret_num} correctly.\n")
            break
        elif num > secret_num:
            print("Its high! Guess again\n")
        elif num < secret_num:
            print("Its Low! Guess again\n")

game_number_guess()