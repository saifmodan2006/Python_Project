# import time

# def countdown(t):
#     while t>= 0:
#         print(f"Time remaining {t} Seconds",end = "\r")
#         time.sleep(1)
#         t -= 1

#     print("BLAST OFF!" + "" * 20)

# secods = input("Enter the ccountdown timer in seconds:")

# try:
#     seconds = int(secods)
#     if secods < 0:
#         print("please enter a non-negative number:")
#     else:
#         countdown(seconds)
# except ValueError:
#     print("Invalid Input. please enter an integer.")






import time

def countdown(t):
    """
    A simple countdown timer.
    t: an integer representing the total seconds for the countdown.
    """
    while t >= 0:
        print(f"Time remaining: {t} seconds", end="\r") # Overwrites the current line
        time.sleep(1)
        t -= 1
    print("BLAST OFF! " + " "*20) # Prints the final message and clears the last line

# User input
seconds = input("Enter the countdown time in seconds: ")

# Validate and run the timer
try:
    seconds = int(seconds)
    if seconds < 0:
        print("Please enter a non-negative integer.")
    else:
        countdown(seconds)
except ValueError:
    print("Invalid input. Please enter an integer.")

