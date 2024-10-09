#Write a program that asks the user to enter their first name, last name, and age, then prints a message "Your name is [first name] [last name] and you are [age] years old."

first_name = input("Please enter your first name: ")
last_name = input("Please input your last name: ")
age = input("Please enter your age: ")

age = int(age)

print("Your name is {} {} and you are {} years old".format(first_name,last_name,age))

