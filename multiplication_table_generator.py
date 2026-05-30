# Ask the user for a number
number = int(input("Enter a number: "))
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# Print the multiplication table
for i in range(start, (end+1)):
    result = number * i
    print(number, "x", i, "=", result)
