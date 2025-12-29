# Check if All Numbers are Positive. Given a list of integers, determine if all numbers are positive. Using all()
# Input : numbers = [1, 2, 3, 4, 5]
# #Expected Output : True

numbers = [1, 2, 3, 4, 5]

result = all(n > 0 for n in numbers)
print(result)



# Check if Any Number is Even. Given a list of integers, check if any number is even. Using any()
# Input: numbers = [1, 3, 5, 7, 8]
# #Expected Output: True

numbers = [1, 3, 5, 7, 8]

result = any(n%2 == 0 for n in numbers)
print(result)


# Determine if any number in a list is divisible by 5 an print.
#

numbers = [1, 7, 12, 20, 9]

result = any(n % 5 == 0 for n in numbers)
print(result)
