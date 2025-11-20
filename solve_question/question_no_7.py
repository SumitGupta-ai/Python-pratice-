# . Write a program to calculate the factorial of a number using a loop

num = int(input("Enter a factorial number: "))

factorial = 1

if num < 0:
    print("Negative")

else:
    for i in range(1, num+1):
        factorial *= i
print(f"Factorial of {num} is {factorial}")
