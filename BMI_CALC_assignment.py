# Global conversion variables
POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

def calculate_bmi(weight_pounds, height_inches):
    # Convert weight to kilograms
    weight_kg = weight_pounds * POUNDS_TO_KG
    # Convert height to meters
    height_meters = height_inches * INCHES_TO_METERS
    # Calculate BMI
    bmi = weight_kg / (height_meters ** 2)
    return bmi

def main():
    try:
        # Get the user's weight and height
        weight_pounds = float(input("Enter your weight in pounds: "))
        height_inches = float(input("Enter your height in inches: "))
        
        # Calculate BMI
        bmi = calculate_bmi(weight_pounds, height_inches)
        
        # Determine BMI category
        if bmi < 18.5:
            category = "underweight"
        elif 18.5 <= bmi < 24.9:
            category = "normal weight"
        elif 25 <= bmi < 29.9:
            category = "overweight"
        else:
            category = "obese"
        
        # Display the results
        print(f"Your BMI is: {bmi:.2f}")
        print(f"You are in the {category} category.")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for weight and height.")
        main() # Recursively call main to retry input

if __name__ == "__main__":
    main()
