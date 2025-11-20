#  Create a program to count the number of vowels in a string. 

text = input("Enter your charecter: ")
vowels = "aeiouAEIOU"
count = 0

for char in text:
    if char in vowels:
        count +=1

print("Numbers of vowels:", count )