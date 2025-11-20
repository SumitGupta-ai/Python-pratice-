# Create a program to print the Fibonacci series up to N terms.

n = int(input("Enter the number if terms: "))

a,b = 0, 1

for i in range(n):
    print(a, end=" ")
    next_num = a+b

    a = b
    b = next_num