# Write a Python script to reverse a given string.

s = input("Enter a charecter: ")
op = ""
for char in s:
   op = char + op
print("Your slicing charecter:", op)   



# Check if a number is a palindrome.

number = int(input("Enter a number: "))
original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10


if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
