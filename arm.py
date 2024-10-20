n = int(input("Enter a number: "))

l = len(str(n))

original_n = n

sum = 0

while n > 0:

    last_dig = n % 10

    x  =  last_dig ** l

    n = n//10

    sum += x

if sum == original_n:
    print(original_n,", is a armstrong number")

else:
    print(original_n,", is not a armstrong number")
