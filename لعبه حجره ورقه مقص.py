import os
import random

# ==========================================
# CONSTANTS: ASCII Art for Game Visuals
# ==========================================
SCISSORS = """
     _________
----'     ____)______ 
           __________)   
            _________)
           (____)
----,_____(____)    
"""

PAPER = """
     _________
----'     ____)______ 
           __________)   
            _________)
            _________)
----,______________)            
"""

ROCK = """
     _________
----'     ____)___ 
           ___(___)   
            __(___)
            __(___)
----,_________(___)    
"""

# Map string choices to their respective ASCII art for easy retrieval
GAME_IMAGES = {
    "rock": ROCK,
    "paper": PAPER,
    "scissors": SCISSORS
}

def clear_screen():
    """Clears the terminal screen based on the Operating System."""
    os.system("cls" if os.name == "nt" else "clear")

# ==========================================
# MAIN GAME LOOP
# ==========================================
print("Welcome to the Rock, Paper, Scissors Game!")

# Show help/rules at the very beginning if requested
user_help = input("Press Enter to continue or type 'help' for the rules: ").lower()
if user_help == "help":
    print("""
         ********** RULES **********
     1) You choose and the computer chooses.
     2) Rock smashes Scissors -> Rock wins.
     3) Scissors cut Paper -> Scissors wins.
     4) Paper covers Rock -> Paper wins.             
     """)
    input("\nPress Enter to start the game...")

while True:
    clear_screen()
    print("--- New Round ---")
    
    # Get and validate user input
    user_choice = input("Enter your choice (rock, paper, scissors) or 'exit' to quit: ").lower()
    
    # Handle exit condition
    if user_choice == "exit":
        print("\nThanks for playing! Goodbye!")
        break
        
    # Check for invalid inputs
    if user_choice not in GAME_IMAGES:
        print("\nInvalid choice. Please choose rock, paper, or scissors.")
        input("\nPress Enter to try again...")
        continue

    # Computer makes a random choice (choosing the string, not the art)
    computer_choice = random.choice(["rock", "paper", "scissors"])

    # Display choices using the ASCII art map
    print(f"\nYour choice:\n{GAME_IMAGES[user_choice]}")
    print(f"The computer chose:\n{GAME_IMAGES[computer_choice]}")

    # Determine the game outcome
    if user_choice == computer_choice:
        print("It's a tie! 🤝")
        
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print(f"🎉 You win! {user_choice.capitalize()} overcomes {computer_choice}.")
        
    else:
        print(f"😢 You lose! {computer_choice.capitalize()} overcomes {user_choice}.")

    # Pause the screen so the user can see the result before clearing
    input("\nPress Enter to continue to the next round...")