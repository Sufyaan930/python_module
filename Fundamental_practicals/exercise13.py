#You are building a basic user information system where you need to collect and store user details.
#Write a program that asks the user for their name, age, and favourite colour, then stores these details in a dictionary and prints the dictionary.

name = input("Enter your full name: ")
age = input("Please enter your age: ")
age = int(age)
favourite_color = input("Please enter your favourite color: ")

mydict = {
    "name": name,
    "age": age,
    "favourite_color" : favourite_color

}
print(mydict)
