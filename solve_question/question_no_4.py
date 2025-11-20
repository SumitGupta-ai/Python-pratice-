# Create a program that prints the multiplication table of a given number.
    # single number table
try:
    number = int(input("Enter a value: "))
except ValueError:
    print("Invalid input. Please Enter an interger value.")
    exit()
print(f"\nMultiplication Table of {number}:")
for i in range(1, 11):
    product = number * i

    print(f"{number} X {i} = {product}")


    # 2 to 10 Table number.

print("\nMultipication tables of (2 to 10):\n")
for i in range(1, 11):
    for num in range(2, 6):
        print(f"{num} x {i:2} = {num*i:3}", end="  ")
    print()