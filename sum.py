n = int(input("Enter a number: "))


sum = 0

while n > 0:

    last_dig = n % 10


    n = n//10

    sum += last_dig

print("The sum of all the digits is:",sum)
