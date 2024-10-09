#You have a list of ages `[23, 45, 16, 27, 30, 18]` and need to perform a simple analysis.
#Write a program to calculate and print the average age, the youngest age, and the oldest age in the list.

age = [23,45,16,27,30,18]
average = sum(age) / len(age)
youngest = min(age)
oldest = max(age)

print(f"Average age is: {average} ")
print(f"Yougest age is: {youngest}")
print(f"Oldest age is: {oldest}")
