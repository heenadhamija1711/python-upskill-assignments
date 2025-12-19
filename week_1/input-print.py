# Objective: Ask the user for their name and greet them.
# Task: Write a program that asks the user for their name and then prints a greeting   message using their name.

name=input("Enter username : ")
print("Hello "+name+" !! ")

# Objective: Perform basic arithmetic operations based on user input.
# Task: Ask the user to enter two numbers from the user and print their sum, multiplication, and division.
num1=int(input("Enter first number : "))
num2=int(input("Enter second number : "))
sum=num1 + num2
print("Sum is : ", sum)

# Task: Ask the user to enter input names separated by commas, split the string from comma and copy to a list and print.
names=input("Enter names separated by commas : ")
ls=names.split(",")
print(ls)

# Task: Ask the user to enter their age and check if they are eligible to vote based on their age.

age=int(input("Enter person's age : "))
if(age >= 18) :
    print("Person is eligible for voting")
else :
    print("Person is not eligible for voting")

# For value = 3.14159, Using f-string print output for only up to 2 decimal places.
# Output: 3.14

value = 3.14159
print(f"{value:.2f}")

