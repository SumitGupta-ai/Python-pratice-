# Write a program to find the largest of three numbers.

num1 = int(input("Enter an value number: "))
num2 = int(input("Enter an value number: "))
num3 = int(input("Enter an value number: "))

largest_number = max(num1, num2, num3)

print(f"The largest number is: {largest_number}")

if num1>num2 and num1>num3:
    print(f'{num1} is largest number')
elif num2>num1 and num2 > num3:
      print(f'{num2} is largest number')
else:
       print(f'{num3} is largest number')


