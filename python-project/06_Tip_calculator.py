# Function to calculate the final amount per person
def calculate_split_amount(bill, tip_percentage, num_people):
    # Calculate the total tip amount
    tip_amount = bill * (tip_percentage / 100)
    
    # Calculate the total bill including the tip
    total_bill = bill + tip_amount
    
    # Calculate the amount each person pays
    amount_per_person = total_bill / num_people
    
    # Return the result rounded to two decimal places for currency format
    return round(amount_per_person, 2)

# Main part of the program to get user input
def main():
    print("Welcome to the tip calculator!")
    
    # Get the total bill amount from the user and convert to a float
    # We use a loop for input validation
    while True:
        try:
            bill = float(input("What was the total bill? $"))
            if bill <= 0:
                print("Bill amount must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number for the bill.")

    # Get the tip percentage and convert to an integer
    while True:
        try:
            tip_percentage = int(input("What percentage tip would you like to give? (e.g., 15, 20) "))
            if tip_percentage < 0:
                 print("Tip percentage cannot be negative. Please try again.")
                 continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the percentage.")

    # Get the number of people splitting the bill and convert to an integer
    while True:
        try:
            num_people = int(input("How many people to split the bill? "))
            if num_people <= 0:
                print("Number of people must be at least one. Please try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer for the number of people.")

    # Calculate the final amount per person
    final_amount = calculate_split_amount(bill, tip_percentage, num_people)
    
    # Print the result formatted to two decimal places
    print(f"\nEach person should pay: ${final_amount:.2f}")

if __name__ == "__main__":
    main()
