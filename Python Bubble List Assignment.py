# Accept five names from the user and store them in a list
names = []
for i in range(5):
    name = input("Enter a name: ")
    names.append(name.lower())

# Bubble Sort algorithm to sort the list in ascending order
swapped = True
while swapped:
    swapped = False
    for i in range(len(names) - 1):
        if names[i] > names[i + 1]:
            swapped = True
            names[i], names[i + 1] = names[i + 1], names[i]

# Print the sorted list
print("Sorted list:", names)

# Reverse the sorted list
names.reverse()

# Print the reversed list
print("Reversed list:", names)
