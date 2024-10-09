#Write a program to perform basic arithmetic operations (addition, subtraction, multiplication, division) on two numbers and print the results.

num1 = input("Enter integer 1: ")
num2 = input("Enter integer 2: ")
num1 = int(num1)
num2 = int(num2)

sum = num1 + num2
difference = num1 - num2 
product = num1 * num2 
division = num1 / num2 

print(f"The addition of the two integers is: {sum}")
print(f"The substraction of the two integers is: {difference}")
print(f"The multiplication of the two integers is: {product }")
print(f"The division of the two integers is: {division}")
