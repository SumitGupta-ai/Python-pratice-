num = [10,20,100,90,30,40,50]
largest_num = num[0]
second_largest = num[0]
for i in num:
    if i > largest_num:
          second_largest = largest_num
          largest_num = i
    elif i > second_largest and i < largest_num:
         second_largest =i
print(second_largest)
