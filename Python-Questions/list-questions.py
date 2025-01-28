'''
Here is a list of questions line by line for easy readability:

Find the index of 'Paris' in ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'].
Multiply all numbers in the list [2, 3, 4] and print the result.
Print the second row and the first element of the third row from the nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
Generate a list of squares of numbers from 1 to 10 using list comprehension.
Find common elements in [1, 2, 3, 4] and [3, 4, 5, 6].
Split 'Python is fun' into a list and join back with hyphens.
Remove all odd numbers from the list [1, 2, 3, 4, 5, 6].
Find the largest even number in the list [11, 22, 33, 44, 55].
Count the total number of vowels in the list ['apple', 'banana', 'cherry'].
Let me know if you need this in any other format! 😊

'''
# 1.)Create a list with values [10, 20, 30, 40, 50]. Print the list and its length.
# QUESTION 1:(SOLUTION)
# values = [10,20,30,40,50]
# print(values)
# length = 0
# for i in values:
#     length = length+1
#     print(length)

# 2.)Access elements from the list ['apple', 'banana', 'cherry', 'date', 'elderberry'] (first, last, third).
# QUESTION 2:(SOLUTION)
# list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
# result = list[0::2]
# print(result)

# 3.)Add elements 5, 10, 15, 20 to an empty list and remove 10.
# QUESTION 3:(SOLUTION)
# list = [5,10,15,20]
# new_list = []
# for num in list:
#     if num != 10:  # skip the 10 condition false
#         new_list += [num]
# print("final",new_list)

# 4.)Slice the list ['red', 'green', 'blue', 'yellow', 'orange']
# (first three, last two, reverse).
# QUESTION 4:(SOLUTION)
#  first three
# list = ['red', 'green', 'blue', 'yellow', 'orange']
#first three 
# empty_list = []
# for i in range(3):
#     empty_list += [list[i]]
# print(empty_list)
#last two
# empty_list = []
# for i in range(len(list)-2,len(list)):
#     empty_list += [list[i]]
# print(empty_list)
#reverse
# empty_list = []
# for i in range(len(list)-1,-1,-1):
#     empty_list += [list[i]]
# print(empty_list)

# 5.)Check if 'dog' is in ['cat', 'dog', 'rabbit', 'bird'] and if 'fish' is not.
# QUESTION 5:(SOLUTION)
# list =  ['cat', 'dog', 'rabbit', 'bird']
# flag = False
# for i in list:
#     if list == "dog":
#          flag = True

# fish_in_list = True
# for j in list:
#     if list == "fish":
#         fish_in_list = False
# print("dog",flag)
# print("fish",fish_in_list)

# 6.) Iterate over the list [1, 2, 3, 4, 5] and print each element multiplied by 2.
# # QUESTION 6:(SOLUTION)
# list =  [1, 2, 3, 4, 5]
# sum_the_values = 0
# for element in list:
#     print(element * 2)
#     sum_the_values += element
# print(sum_the_values)
    
# 7.)Count how many times 2 appears in the list [1, 2, 2, 3, 4, 2, 5].
# QUESTION 7:(SOLUTION)
# list = [1, 2, 2, 3, 4, 2, 5]
# count = 0
# for i in list:
#     if i == 2:
#         count +=1
# print("count of 2: ",count)


# 8.)Find the maximum and minimum values in the list [23, 45, 67, 12, 34, 89].
# QUESTION 8:(SOLUTION)
#  MAXIMUM
# values = [199990000,49,56,78,23445,4353]
# max_value = values[0]
# for i in values:
#     if i>max_value:
#         max_value = i
# print(max_value)
# MINIMUM
# values = [1,49,56,78,23445,4353]
# max_value = values[0]
# for i in values:
#     if i<max_value:
#         max_value = i
# print(max_value)

# 9.)Remove duplicates from the list [1, 2, 3, 4, 2, 5, 1, 3].
# QUESTION 9:(SOLUTION)
# numbers = [1, 2, 3, 4, 2, 5, 1, 3]
# unique_numbers = [0] * len(numbers)  # Placeholder list with maximum possible size
# unique_count = 0  # Counter for the number of unique elements

# for num in numbers:
#     is_unique = True
#     # Check if the number is already in the unique_numbers list
#     for i in range(unique_count):
#         if unique_numbers[i] == num:
#             is_unique = False
#             break
#     # If the number is unique, add it to the unique_numbers list
#     if is_unique:
#         unique_numbers[unique_count] = num
#         unique_count += 1

# # Slice the list to include only the unique numbers
# unique_numbers = unique_numbers[:unique_count]
# print("Unique values:", unique_numbers)

# 10.)Merge two lists [1, 2, 3] and [4, 5, 6] into one.
# QUESTION 10:(SOLUTION)
# list1 = [1,2,3]
# list2 = [4,5,6]
# merge = list1[:]
# # for i in list2:
# #     merge += [i]
# # print(merge)

# 11.)Sort the list [88, 56, 92, 75, 69] in ascending and descending order.
# QUESTION 11:(SOLUTION)
numbers = [88, 56, 92, 75, 69]
ascending_order = sorted(numbers)
print("Ascending order:", ascending_order)
descending_order = sorted(numbers, reverse=True)
print("Descending order:", descending_order)

# 12.)Find the index of 'Paris' in ['New York', 'London', 'Paris', 'Tokyo', 'Berlin'].
# QUESTION 12:(SOLUTION)
# cities = ['New York', 'London', 'paris', 'Tokyo', 'Berlin']
# find = "paris"
# index = []
# for i in range(len(cities)):
#     if cities[i] == find.lower():
#         index.append(i)
# print(index)
# #
# 13.)Multiply all numbers in the list [2, 3, 4] and print the result.
# QUESTION 13:(SOLUTION)
# li = [2,3,4]
# value = 1
# for i in li:
#     value *= i
# print(value)

# Q.14)Print the second row and the first element of the third row from the nested list [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# QUESTION 14:(SOLUTION)

