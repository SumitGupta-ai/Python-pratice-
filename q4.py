# # Write a script to count the frequency of each character in a string.
# text = 'sumitt'
# print(len(text)) # but this method not build our logic


text = 'sumiitt'
feq = {} 
for char in text:
    if char in feq:
        feq[char] += 1
    else:
        feq[char] = 1
print(feq)
        