#Write a program that asks the user to enter the name and price of three products, then stores this information in a dictionary and prints it.

num_product = input("Please enter the number of the product: ")
for i in range(3):
    name = input(f"Please enter the name of the product{i+1}: ")
    price = input(f"Please input the price of the product{i+1}: ")
    price = float(price)



