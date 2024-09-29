# This program calculates the percentage of the total budget spent in various categories

# Prompt the user to enter their total budget
total_budget = float(input("Enter your total budget: "))

# Declare the amounts spent in various categories
housing = 0  # Rent free as you live at home
utilities = 0  # Free as you live at home
groceries = 200  # Protein drinks and meal preps for gym
transportation = 1500  # Ubers
health_care = 30  # Copay and prescription
personal_care = 50  # Toothpaste, deodorant, body spray, mouthwash
clothing = 25  # Clothing
debt = 0  # No debt

# Calculate the percentage of the total budget spent in each category
housing_percentage = (housing / total_budget) * 100
utilities_percentage = (utilities / total_budget) * 100
groceries_percentage = (groceries / total_budget) * 100
transportation_percentage = (transportation / total_budget) * 100
health_care_percentage = (health_care / total_budget) * 100
personal_care_percentage = (personal_care / total_budget) * 100
clothing_percentage = (clothing / total_budget) * 100
debt_percentage = (debt / total_budget) * 100

# Display the results in a user-friendly format
print(f"\nBudget Breakdown:")
print(f"Housing: {housing_percentage:.2f}%")
print(f"Utilities: {utilities_percentage:.2f}%")
print(f"Groceries: {groceries_percentage:.2f}%")
print(f"Transportation: {transportation_percentage:.2f}%")
print(f"Health Care: {health_care_percentage:.2f}%")
print(f"Personal Care: {personal_care_percentage:.2f}%")
print(f"Clothing: {clothing_percentage:.2f}%")
print(f"Debt: {debt_percentage:.2f}%")
