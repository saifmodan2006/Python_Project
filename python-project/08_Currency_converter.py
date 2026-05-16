from forex_python.converter import CurrencyRates
from decimal import Decimal

def convert_currency(amount, from_currency, to_currency):
    """
    Converts an amount from one currency to another using real-time rates.
    """
    try:
        c = CurrencyRates()
        # Convert amount, using Decimal for precision
        converted_amount = c.convert(from_currency, to_currency, Decimal(str(amount)))
        # Round to 2 decimal places for typical currency display
        return round(converted_amount, 2)
    except Exception as e:
        return f"Error: {e}"

# --- Example Usage ---
# Get user input
amount_to_convert = input("Enter the amount to convert: ")
from_curr = input("Enter the source currency code (e.g., USD): ").upper()
to_curr = input("Enter the target currency code (e.g., EUR): ").upper()

# Perform conversion and print result
result = convert_currency(amount_to_convert, from_curr, to_curr)

if isinstance(result, str):
    print(result)
else:
    print(f"\n{amount_to_convert} {from_curr} = {result} {to_curr}")

