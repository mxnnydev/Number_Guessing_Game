import random # importing the random built-in library from python

# Number Guessing Game program ~ user will guess a number & keep playing until they decide to end.

life = 3 # inital score amount

def start():
    inital_program_message()
    collect_user_info

def inital_program_message():
    print("👾 Welcome to number guessing game 👾".title())
    begin = input("\nWould you like to begin (Y - Yes or N - No ): ").strip()
    
    # handle incorrect user input
    while not begin.lower() in ['y','yes','n','no' ]:
        begin = input("\nINVALID INPUT: Would you like to begin (Y - Yes or N - No ): ").strip()
    
    if begin.lower() in['yes','y']:
        collect_user_info()
    elif begin.lower() in ['no','n']:
        print("Okay see you later")

def collect_user_info():
    name = input("\nWhat is your name: ").strip()
    
    # welcome user
    print(f"\nWelcome {name.title()}! Let's begin 🔥")

    generate_random_number()

def generate_random_number():
    print("\nChoose the range of number to guess from\n")
    start_range = int(input("Starting point: "))
    end_range = int(input("\nEnding point: "))
    
    random_number = random.randint(start_range,end_range)
    
    # call insert random number in start_game function
    start_game(start_range,end_range,random_number)

def is_valid_guess(guess):
    if guess.isdigit():
        return True
    else:
        while not guess.isdigit():
            print("\nINVALID INPUT")
            user_guess = input("\nGuess: ")
        return True
        

def score(type_score):
    global life
    if life < 0:
        print("\nYou lost :( WANNA PLAY AGAIN! 🏳️")
    if type_score == 'add':
        life+= 1
    elif type_score == 'sub':
        life-= 1
        


def start_game(start_range, end_range,rand_num):
    print(f"Game Life Health ❤️ ❤️ ❤️ - {life}")
    print(f"\nStart Guess from {start_range} - {end_range}")
    user_guess = input("Guess: ")

     # after verifying valid input convert to int type
    if is_valid_guess(user_guess):
        user_guess = int(user_guess)
    # check based on generated random value
    while user_guess != rand_num:
        if user_guess == rand_num:
            print("You Guessed to RIGHT")
            score('add')
        elif user_guess > rand_num:
            print("You Guessed to HIGH")
            score('sub')
        elif user_guess < rand_num:
            print("You Guessed to LOW")
            score('sub')
        # if user response is WRONG ask again until lifeline remains
        user_guess = input("Guess: ")
        if is_valid_guess(user_guess):
            user_guess = int(user_guess)
    


def main():
    start() # start the inital program 

if __name__ == '__main__':
    main()


## Overview of things to fix 🛑
# fix: how the game keep track of health
# fix: how the game tell user when they win
# fix: how the game tell user when they lose
# fix: how the game end the game or continue 