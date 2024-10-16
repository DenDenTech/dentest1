# Define the recursive function named factorial
def factorial(n):
    # Base case: factorial of 1 or 0 is 1
    if n == 1 or n == 0:
        return 1
    else:
        # Recursive step: n * factorial of (n-1)
        return n * factorial(n - 1)

# Create a main function
def main():
    try:
        # Prompt the user to enter a non-negative integer
        n = int(input("Enter a non-negative integer: "))
        
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            # Call the factorial function and print the result
            result = factorial(n)
            print(f"The factorial of {n} is {result}.")
    
    except ValueError:
        print("Invalid input. Please enter a valid non-negative integer.")
        main()  # Recursively call main to retry input

# Call the main function to run the program
if __name__ == "__main__":
    main()
