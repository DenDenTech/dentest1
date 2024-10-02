# Initialize the number of bottles
bottles = 99

while bottles > 0:
    if bottles > 1:
        print(f"{bottles} bottles of beer on the wall")
        print(f"{bottles} bottles of beer")
        print("Take one down, pass it around")
        bottles -= 1
        if bottles == 1:
            print(f"{bottles} bottle of beer on the wall!\n")
        else:
            print(f"{bottles} bottles of beer on the wall!\n")
    else:
        print(f"{bottles} bottle of beer on the wall")
        print(f"{bottles} bottle of beer")
        print("Take it down, pass it around")
        bottles -= 1
        print("No more bottles of beer on the wall!")

