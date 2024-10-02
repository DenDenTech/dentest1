# Ask the user for their age
age = int(input("Enter your age: "))

# Check if the user is old enough to drive
if age >= 16:
    print("You are old enough to drive.")
else:
    print("You are not old enough to drive.")

# Check if the user can vote
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Check if the user can legally buy alcohol
if age >= 21:
    print("You can legally buy alcohol.")
else:
    print("You cannot legally buy alcohol.")

# Check if the user is eligible for a senior discount
if age >= 65:
    print("You are eligible for a senior discount.")
else:
    print("You are not eligible for a senior discount.")
