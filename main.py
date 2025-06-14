import random # importing the random built-in library from python

# Number Guessing Game: User keeps guessing until they choose to stop.

def start():
    inital_program_message()

def inital_program_message():
    print("👾 Welcome to number guessing game 👾".title())
    begin = input("\nStart the game? Enter 'Y' for Yes or 'N' for No: ").strip()
    
    # handle incorrect user input
    while not begin.lower() in ['y','yes','n','no' ]:
        print("\nPlease enter a valid input (Enter 'Y' for Yes or 'N' for No):\n")
    
    if begin.lower() in['yes','y']:
        generate_random_number()
    elif begin.lower() in ['no','n']:
        print("\nSee you soon 👋\n")

def is_number(prompt_text):
    user_input = input(prompt_text)

    while not user_input.isdigit():
        print("\nPlease enter a valid number.\n")
        user_input = input(prompt_text)
    return user_input


def generate_random_number():
    print(f"\nWelcome Let's begin 🔥")
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

def play_again(prev_result):
    if prev_result == "won":
        play_again = input("\n🎉 You won! Want to play another round? (Y/N): ").strip()
    elif prev_result == "lost":
        play_again = input("\nGAME OVER 🥺 Would you like to play again? (Y/N): ").strip()
    
    # handle incorrect user input
    while not play_again.lower() in ['y','yes','n','no' ]:
        play_again = input("\nINVALID INPUT: Would you like to begin (Y - Yes or N - No ): ").strip()
    
    if play_again.lower() in['yes','y']:
        generate_random_number()
    elif play_again.lower() in ['no','n']:
        print("\nSee you soon 👋\n")



def game_logic(random_number):
    health = ["❤️", "❤️", "❤️"]
    health_length = len(health)
    print(f"\nHealth: {" ".join(health)}")

    while not health.count("💔") == 3:
        guess = int(is_number("\nGuess: "))
        if guess == random_number:
            break
        if guess > random_number:
            print("guess too HIGH")
            health_length -=1
        elif guess < random_number:
            health_length -=1
            print("guess too LOW")
        
        health[health_length] = "💔"
        print(f"\nHealth: {" ".join(health)}")
    
    if guess == random_number:
        print("\nYou Won 🏆")
        play_again("won")   
    elif health.count("💔") == 3:
        print("\nYou Lost 💔")
        play_again("lost")        

        
def main():
    start()

# Run the program only when this file is executed directly (not imported)
if __name__ == '__main__':
    main()
