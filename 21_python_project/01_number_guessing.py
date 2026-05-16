# import random
# print("Welcome to the number guessing app")

# low=int(input("Enter lower number:"))
# high=int(input("Enter higher number:"))

# print(f"you have 7 chance to guess the number between {low} and {high}. Let's start")

# num=random.randint(low,high)
# ch=7
# gc=0

# for i in range(ch):
#     guess=int(input("Enter your guess:"))
#     if guess==num:
#         print(f"Congratulations! You guessed the number in {i+1} tries.")
#         break
#     elif guess<num:
#         print("Too low!")
#     else:
#         print("Too high!")  
#     gc+=1

# if gc==ch:
#     print(f"Sorry, you didn't guess the number. It was {num}.")
# print("Thank you for playing the number guessing app!")



import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

low = int(input("Enter the Lower Bound: "))
high = int(input("Enter the Upper Bound: "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}. Let's start!")

num = random.randint(low, high) 
ch = 7                        # Total allowed chances
gc = 0                        # Guess counter

while gc < ch:
    gc += 1
    guess = int(input('Enter your guess: '))

    if guess == num:
        print(f'Correct! The number is {num}. You guessed it in {gc} attempts.')
        break

    elif gc >= ch and guess != num:
        print(f'Sorry! The number was {num}. Better luck next time.')

    elif guess > num:
        print('Too high! Try a lower number.')

    elif guess < num:
        print('Too low! Try a higher number.')