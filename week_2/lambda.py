# Given a list let's see how to double each element of the given list. Using map()
# #Expected Output: [2, 4, 6, 8]
#
a = [1, 2, 3, 4]

newlist = list(map(lambda x: x * x, a))
print(newlist)

# Use filter() and lambda to extract all even numbers from a list of integers.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #Expected Output: [2, 4, 6, 8, 10]
#
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newlist = list(filter(lambda x: x % 2 == 0, numbers))
print(newlist)

# Use reduce() and lambda to find the longest word in a list of strings.
# from functools import reduce
# words = ["apple", "banana", "cherry", "date"]
# #Expected Output: 'banana'
#

from functools import reduce

words = ["apple", "banana", "cherry", "date"]

longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)

# Use map() to square each number in the list and round the result to one decimal place.
# my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
# #Expected Output: [18.9, 37.1, 10.6, 95.5, 4.7, 78.9, 21.1]
#

my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]
newlist = list(map(lambda x: round(x * x, 1), my_floats))

print(newlist)

# Use filter() to select names with 7 or fewer characters from the list.
# my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]
# #Expected Output: ['olumide', 'josiah', 'omoseun']
#

my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

result = list(filter(lambda name: len(name) <= 7, my_names))
print(result)


# Use reduce() to calculate the sum of all numbers in a list. [1, 2, 3, 4, 5]
#
from functools import reduce

numbers = [1, 2, 3, 4, 5]

total_sum = reduce(lambda a, b: a + b, numbers)
print(total_sum)
