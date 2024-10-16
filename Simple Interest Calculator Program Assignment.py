# Define the function calculate_interest
def calculate_interest(principal, rate, time):
    # Calculate simple interest
    interest = (principal * rate * time) / 100
    return interest

# Get the information from the customer
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate as a whole number (5% would be 5): "))
investment_time = int(input("Enter the investment time in whole years: "))

# Call the function and pass the information in
calculated_interest = calculate_interest(principal_amount, interest_rate, investment_time)

# Print the result in a user-friendly string, formatted
print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \n"
      f"at an interest rate of {interest_rate}% over a period of \n"
      f"{investment_time} years is: ${calculated_interest:,.2f}")
