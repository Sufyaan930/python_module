#Write a program that asks the user to enter the name and price of three products, then stores this information in a dictionary and prints it.

p1name = input("Please enter the name of product 1: ")
p1price = input("Please enter the price of product 1: ")
p2name = input("Please enter the name of product 2: ")
p2price = input("Please enter the price of product 2: ")
p3name = input("Please enter the name of product 3: ")
p3price = input("Please enter the price of product 3: ")

details = {
    "name of product 1" : p1name,
    "price of product 1": p1price,
    "name of product 2" : p2name,
    "price of product 2" : p2price,
    "name of product 3" : p3name,
    "price of product 3" : p3price
}
print(details)