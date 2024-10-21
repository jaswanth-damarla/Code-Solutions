# Function to compute GCD using the Euclidean algorithm
def gcd(a, b):
    while b:  # This loop will continue until b becomes 0
        a, b = b, a % b  # Swap a with b, and b with a % b (remainder)
    return a  # When b becomes 0, a will be the GCD

# Take input from the user
num1 = int(input("Enter the first number: "))  # Input the first number
num2 = int(input("Enter the second number: "))  # Input the second number

# Calculate the GCD using the gcd function
result = gcd(num1, num2)

# Print the result
print("The GCD of", num1, "and", num2, "is:", result)
