user_input = input("Enter a list of numbers separated by spaces: ")

numbers = [int(n) for n in user_input.split()]

unique_numbers = sorted(set(numbers))

if len(unique_numbers) < 2:
    print("There is no second largest number.")
else:
    print("The second largest number is:", unique_numbers[-2]) 
