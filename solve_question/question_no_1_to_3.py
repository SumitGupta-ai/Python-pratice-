# Write a Python program to swap two variables.
first_name = "sumit"
last_name = "gupta"

first_name, last_name = last_name, first_name
print(f"After swapping: first_name = {first_name}, last_name = {last_name}")


#  Take user input and display it back to the user.

name = input("Enter a name: ")
course_name = input("Enter a course name: ")
college_name = input("Enter a college name: ")
father_name = input("Please Enter your father name: ")
print(f"Your details\nname: {name}\ncourse: {course_name}\ncollege: {college_name}\nfather name: {father_name}")



# Write a program to check if a number is even or odd.

number = int(input("Enter a value: "))
if number %2 == 0:
    print("Even number")
else:
    print("Odd number")