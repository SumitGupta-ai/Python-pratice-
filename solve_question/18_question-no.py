#  Create a program to print all Armstrong numbers between 1 to 1000. 

for num in range(1,1001):
   
   digit = str(num)

   power = len(digit)
   total = 0
   for d in digit:
      
      total += int(d) ** power

   if total == num:
      print(num)
