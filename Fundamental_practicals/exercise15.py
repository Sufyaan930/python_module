#Write a program that asks the user to enter a number and checks if it is positive, negative, or zero. Print "Positive", "Negative", or "Zero" accordingly.
num = input("Please enter a number: ")
num = int(num)

if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")
    