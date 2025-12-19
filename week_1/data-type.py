# Task: Convert the following values to the specified types and print the results
# Convert 3.75 to an integer and print the value

num=3.75
print(int(num))


# Convert "123" to a float and print the value
num=123
print(float(num))

# Convert 0 to a boolean and print the value

num=0
print(bool(num))

# Convert False to a string and print the value

#
# 2. Convert all characters in the string to uppercase. x = "hello"

str=input("Enter string to convert into uppercase")
print(str.upper())

# 3. Given x = 5 and y = 3.14, calculate z = x + y and determine the data type of z. And convert it to integer.
x=5
y=3.14
z=x+y
print(type(z))

# 4. Given the string s = 'hello', perform the following operations:
# Convert the string to uppercase.

s="hello"
print(s.upper())

# Replace 'e' with 'a'.
newS=s.replace('e','a')
print(newS)
# Check if the string starts with 'he'.
print("String start with 'he' ? ", s.startswith('he'))

# Check if the string ends with 'lo'.
print("String ends with 'lo' ? ", s.endswith('lo'))
