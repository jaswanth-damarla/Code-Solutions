# Take input from the user
user_input = input("Enter a list of numbers separated by spaces: ")

# Convert the input into a list of integers
numbers = [int(n) for n in user_input.split()]

# Create an empty dictionary to store frequency counts
frequency_dict = {}

# Loop through each element in the list
for element in numbers:
    # Update the frequency count in the dictionary
    if element in frequency_dict:
        frequency_dict[element] += 1
    else:
        frequency_dict[element] = 1

# Print the frequency dictionary
print(frequency_dict)
