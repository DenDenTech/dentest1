# Function to calculate the area of a square
def square(side):
    area = side * side
    print("The area of the square is " + str(area) + " square units.")

# Function to calculate the area of a circle
def circle(radius):
    pi = 3.14
    area = pi * radius * radius
    print("The area of the circle is " + str(area) + " square units.")

# Test the functions
square(13)
circle(3)
