# . Write a program to find the GCD of two numbers. 

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
x,y = a,b

while y != 0:
    x,y = y,x % y
gcd = x
lcm = (a * b) // gcd

print(f"GCD is {gcd}")
print(f"LCM is {lcm}")