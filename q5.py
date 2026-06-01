 # Write a program that accepts a sentence and calculates the number of upper and lower case letters

sentence = 'Hello World'
upper = 0
lower = 0
for char in sentence:
    if char.isupper():
       upper += 1
    elif char.islower():
        lower +=1
print(f"upper count number: ", upper)
print(f"lower count number: ", lower) 