# Daily Heart Rate Tracker

# Define time slots
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]

# Initialize an empty list to store heart rate data
heart_rates = []

# Loop over each time slot to get user input for heart rate
for slot in time_slots:
    heart_rate = int(input(f"Enter your heart rate (in BPM) in the {slot}: "))
    heart_rates.append([slot, heart_rate])

# Calculate the average heart rate
total_heart_rate = 0
for entry in heart_rates:
    total_heart_rate += entry[1]

average_heart_rate = total_heart_rate / len(heart_rates)

# Print the heart rates and average heart rate
print("\nHeart Rate Data:")
for entry in heart_rates:
    print(f"{entry[0]}: {entry[1]} BPM")

print(f"\nAverage heart rate today: {average_heart_rate:.2f} BPM")

# Optional: save heart rate data to a file
with open('heart_rate_data.txt', 'w') as file:
    file.write("Heart Rate Data:\n")
    for entry in heart_rates:
        file.write(f"{entry[0]}: {entry[1]} BPM\n")
    file.write(f"\nAverage heart rate today: {average_heart_rate:.2f} BPM\n")
