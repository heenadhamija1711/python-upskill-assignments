# For loop
# Write a program that takes the input from the user and checks if a number is even or odd.

number=int(input("Enter the number : "))
if(number %2==0):
    print("Even number : ",number)
else :
    print("Odd number : ",number)

# Reverse a string using a for loop and check it is a palindrome. - Strings = “civic”, “hello”

str=input("Enter the string to reverse : ")
reversed_str=str[::-1]
print(reversed_str)

# Using the input from the user, Generate the first N numbers of the Fibonacci sequence.
n = int(input("Enter the number of terms: "))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive number")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b



# From list [1,2,3,4,5]. Write code to find two values from the list when added the result is 9.	#Expected output : [4, 5]
#
nums = [1, 2, 3, 4, 5]
target = 9

result = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result = [nums[i], nums[j]]

print(result)


# While loop
# Print all even numbers between 1 and 20 using a while loop.

startnum=1
endnumber=20
while(startnum<endnumber):
    if(startnum %2==0):
        print(startnum)
    startnum=startnum+1

# Break
# Find the first occurrence of a number in a list and stop further searching.
numbers = [10, 20, 30, 40, 50]
search_for = 30

for num in numbers:
    if(num == search_for):
        break
    print(num)

# Continue
# Using continue statement, print only the odd numbers from 1 to 10.


start_num=1
end_number=10

while(start_num<end_number):
    if(start_num %2 ==0):
        start_num=start_num+1
        continue
    print(start_num)
    start_num=start_num+1

# Pass
# What will be the output
for i in range(5):
    if i == 3:
        pass
    print(i)
# Output : 0 1 2 3 4


# Match
# Write a program that takes a day of the week as input and prints whether it's a weekday or weekend using match conditional statements.


day = input("Enter a day of the week: ").lower()

match day:
    case "monday" | "tuesday" | "wednesday" | "thursday" | "friday":
        print("Weekday")
    case "saturday" | "sunday":
        print("Weekend")
    case _:
        print("Invalid day")

