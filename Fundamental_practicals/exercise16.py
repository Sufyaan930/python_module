#Write a program that asks the user to enter their birth year, calculates their age, and prints a message stating their age. Assume the current year is 2024.

current_year = 2024
birth_year = input("Please enter your birth year: ")
birth_year = int(birth_year)
age = current_year - birth_year

print(f"Your age is {age}")
