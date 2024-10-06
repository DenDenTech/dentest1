# Create a list named days with all seven days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Initialize an empty list called steps
steps = []

# Using a loop, ask the user to enter the number of steps for each day
for day in days:
    steps.append(int(input(f"How many steps did you take on {day}? ")))

# Display the steps recorded for each day
for day, step in zip(days, steps):
    print(f"You took {step} steps on {day}")

# Calculate and display the total number of steps taken in the week
total = sum(steps)
print(f"Total steps: {total}")

# Calculate the average number of steps taken per day
average = round(total / len(steps))
print(f"Average steps: {average}")
