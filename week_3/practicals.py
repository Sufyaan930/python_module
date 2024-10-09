#Create an empty list called **`fruits`**
fruits=[]
#Add the following items to the list using the **`append()`** method: **`apple`**, **`banana`**, **`orange`**
fruits.append('apple')
fruits.append('banana')
fruits.append('orange')
#Print the length of the list using the **`len()`** function
print("The length of the list is: ",len(fruits))
#Print the second item in the list
print("The second item in the list is: ",fruits[1])
#Change the value of the second item to **`grape`**
fruits[1]='grape'
#Print the entire list using a loop
print("The items in the list are: ")
for fruit in fruits:
 print(fruit)
#Remove the first item from the list using the **`pop()`** method
fruits.pop(0)
#Print the updated list
print("The updated list is: ",fruits)
