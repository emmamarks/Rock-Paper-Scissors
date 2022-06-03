import random

while True:

    user_action = input("Enter a choice (Rock, Paper, Scissors): ")
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nPlayer ({user_action}) : CPU ({computer_action})\n")

    if user_action == computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            print("Rock smashes Scissors! You win!")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            print("Paper covers Rock! You win!")
        else:
            print("Scissors cuts Paper! You lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            print("Scissors cuts Paper! You win!")
        else:
            print("Rock smashes Scissors! You lose.")
    else:
        print("Invalid Input. Check your spelling!")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break