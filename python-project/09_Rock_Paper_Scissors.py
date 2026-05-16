import random
# create using if elif staement to make project of rock paper scissors game not using function nnot using loops also
print("Welcome to Rock, Paper, Scissors Game!")
print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Type 'exit' to quit the game.")
choices = ['rock','paper','scissors']
user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
if user_choice == 'exit':
    print("Thanks for playing! Goodbye!")
elif user_choice not in choices:
    print("Invalid choice! please choose rock, paper, or scissors.")
else:
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif user_choice == 'rock':
        if computer_choice == 'scissors':
            print("You win! Rock crushes Scissors.")
        else:
            print("You lose! Paper covers Rock.")
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print("You win! Paper covers Rock.")
        else:
            print("You lose! Scissors cut Paper.")
    elif user_choice == 'scissors':
        if computer_choice == 'paper':
            print("You win! Scissors cut Paper.")
        else:
            print("You lose! Rock crushes Scissors.")
