import random

def roll_dice(num_side=6,num_dice=2):
    """Generate random numbers for dice rolls and returns a list of results."""
    results = []
    for _ in range(num_dice):
        roll = random.randint(1,num_side)
        results.append(roll)
    return results
def main():
    print("Welcome to the dice rolling simulator")


    roll_again = "yes"
    while roll_again.lower() in ["yes","y"]:
        dice_values = roll_dice()

        print("\nROlling the dices:")
        print(f"The values are:{dice_values}")
        print(f"Total sum:{sum(dice_values)}")

        roll_again = input("\n press 'y' or 'yes' to roll the dices again (any other exit):")

    print("Have a good day!")
if __name__ == "__main__":
    main()