# 1.Given a list of numbers, find and print the maximum and minimum values.
# nums = [1, 2, 3, 4, 5]

nums=[1,2,3,4,5]
print(max(nums))
# 2. Given two lists below, merge the values from both lists to one and print
# a = [1,2,3,4]      b = [5,6,7,8]
a = [1,2,3,4]
b = [5,6,7,8]
print(a+b)

# 3. From a list, print the number of times the value 3 appears in the list:
# a = [1,3,4,5,2,1,3,9,3]

a = [1,3,4,5,2,1,3,9,3]
num=3
print(num," occurs how many times ? ",a.count(num))

# 4. From below list, Sort the list and print
a = [1,3,4,5,2,1,3,9,3]
a.sort()
print("Sorted list : ",a)

# 5. Given a set, add the element 6 to it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.add(6)
print(numbers)

# 6. Given a set, remove the element 3 from it and print the updated set.
numbers = {1, 2, 3, 4, 5}
numbers.remove(3)
print(numbers)

# 7. Given two sets, find and print their intersection.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1-set2)

# 8. Given a tuple, count and print the number of occurrences of the element 'apple'.
fruits = ('apple', 'banana', 'apple', 'cherry')
print("Apple occurs : ",fruits.count("apple"))

# 9. Given two tuples, concatenate them and print the result.
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

print(tuple1+tuple2)

# 10. Access and print the value associated with the key "age" from the dictionary.
person = {"name": "Alice", "age": 30, "city": "New York"}
print(person.get("age"))

# 11. Add new key,  gender to dictionary and assign “M” to it and print

person = {"name": "Alice", "age": 30, "city": "New York"}
person["gender"]="M"
print(person)
# 12. Remove the key "city" from the above Dict and print

person.pop("city")
print(person)
# 13. Given two dictionaries, merge them into one
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

dict3={}
for k,v in dict1.items():
    dict3[k]=v

for k,v in dict2.items():
    dict3[k]=v

print("Dict 3: ",dict3)
