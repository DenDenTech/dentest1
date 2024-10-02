# Ask the user for their numeric grade
grade = int(input("Enter your numeric grade (0-100): "))

# Check if the number is between 0 and 100
if grade < 0 or grade > 100:
    print("Invalid grade. Please enter a grade between 0 and 100.")
else:
    # Determine the letter grade based on the numeric grade
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    # Display the letter grade
    print(f"Your letter grade is: {letter_grade}")
