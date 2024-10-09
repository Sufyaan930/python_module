#Write a program that asks the user for their name and favourite number, then prints the message "Hello [name], your favourite number is [number]!", ensuring that the number is formatted with at least two digits (e.g., 07 instead of 7).

name = input("Please enter your name: ")
num = input("Please enter your favourite number: ")
num = int(num) 

print(f"Your name is {name} and your favourite number is {num:02d}")
