# Initialize the seating list with seats 1 through 20
seats = list(range(1, 21))

# Function to display available seats
def display_seats(seats):
    print("Available seats:", seats)

# Function to handle the ticket purchase process
def purchase_ticket(seats):
    while True:
        display_seats(seats)
        seat = int(input("Enter the seat number you want to purchase (enter 0 to finish): "))
        if seat == 0:
            break
        elif seat in seats:
            seats.remove(seat)
            print(f"Seat {seat} has been successfully purchased.")
        else:
            print("Invalid seat number or seat already sold. Please try again.")

# Main program
print("Welcome to the ticket sales system!")
purchase_ticket(seats)
print("Thank you for using the ticket sales system!")
