# Create a program that removes all duplicate characters from a string

# without function
text = 'sumitt'
dup = set()
result = ''
for i in text:
    if i not in dup:
        result += i
        dup.add(i)
print(result)