# Write a Python program to check if a string has all unique characters. 

string = 'teri pg college'
unique = set()
is_unique = True
for i in string:
    if i in unique:
        is_unique = False
        break
    else:
        unique.add(i)
print(is_unique)
        

    