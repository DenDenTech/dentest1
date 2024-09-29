# This program converts kilograms to pounds and displays the results for four different samples

# Conversion factor from kilograms to pounds
conversion_factor = 2.20462

# Declare variables for the samples in kilograms
sample1_kg = 10
sample2_kg = 15
sample3_kg = 20
sample4_kg = 25

# Calculate the corresponding weights in pounds
sample1_lb = sample1_kg * conversion_factor
sample2_lb = sample2_kg * conversion_factor
sample3_lb = sample3_kg * conversion_factor
sample4_lb = sample4_kg * conversion_factor

# Display the results with appropriate formatting
print("\nKilograms to Pounds Conversion:")
print("Sample 1: {} kg = {:.4f} lb".format(sample1_kg, sample1_lb))
print("Sample 2: {} kg = {:.4f} lb".format(sample2_kg, sample2_lb))
print("Sample 3: {} kg = {:.4f} lb".format(sample3_kg, sample3_lb))
print("Sample 4: {} kg = {:.4f} lb".format(sample4_kg, sample4_lb))
