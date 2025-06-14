import random # importing the random built-in library from python

# Number Guessing Game program ~ user will guess a number & keep playing until they decide to end.

def start():
    inital_program_message()

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

    while not name.isalpha():
        print("\nSomething went wrong let's try that again!")
        name = input("\nWhat is your name: ").strip()
    
    # welcome user
    print(f"\nWelcome {name.title()}! Let's begin 🔥")

    generate_random_number()

def is_number(prompt_text):
    user_input = input(prompt_text)

    while not user_input.isdigit():
        print("\nPlease enter a valid number.\n")
        user_input = input(prompt_text)
    return user_input


def generate_random_number():
    print("\nChoose the range of number to guess from\n")

    start_range = int(is_number("Start Range: "))
    end_range = int(is_number("End Range: "))

    # verify the range is correct
    start_range, end_range = correct_range(start_range, end_range)

    game_logic(random.randint(start_range,end_range))

def correct_range(start_range, end_range):
    if not start_range < end_range:
        print("\nStart Range must be less than End Range. Let's try that again!\n")
        start_range = int(is_number("Start Range: "))
        end_range = int(is_number("End Range: "))
    return start_range, end_range

def game_logic(random_number):
    score = 0
    health = ["❤️", "❤️", "❤️"]
    health_length = len(health)
    print(f"Health: {" ".join(health)}")

    while not health.count("💔") == 3 and score < 5:
        guess = int(is_number("\nGuess: "))
        if guess == random_number:
            print("Guess Right")
            break
        elif guess > random_number:
            print("Too HIGH")
            health_length -=1
        elif guess < random_number:
            print("Too LOW")
            health_length -=1
        health[health_length] = "💔"
        print(f"Health: {"".join(health)}")
    
    if score == 5:
        print('Win')
    if health.count("💔") == 3:
        print("GAME OVER 🥺")
        
                


def main():
    start() # start the inital program 

if __name__ == '__main__':
    main()