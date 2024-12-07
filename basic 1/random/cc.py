from forex_python.converter import CurrencyRates

def convert_currency(amount, from_currency, to_currency):
    try:
        # Initialize the CurrencyRates object
        c = CurrencyRates()
        
        # Get the converted amount
        converted_amount = c.convert(from_currency, to_currency, amount)
        return converted_amount
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
amount = 100
from_currency = "USD"
to_currency = "INR"

converted_amount = convert_currency(amount, from_currency, to_currency)
print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
