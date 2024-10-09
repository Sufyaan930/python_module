#Write a program that converts the following:
# Convert the integer `5` to a float.
#Convert the float `3.9` to an integer.
#  Convert the string `"123"` to an integer.

integer_value = 5
float_value = 3.9
string_value = "123"

converted_float = float(integer_value)
converted_int_from_float = int(float_value)
converted_int_from_string = int(string_value)

print(f"integer {integer_value} converted to float is: {converted_float}")
print(f"float {float_value} converted to integer is: {converted_int_from_float}")
print(f"string {string_value} converted to integer is: {converted_int_from_string}")


