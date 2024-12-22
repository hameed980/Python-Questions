'''
'''

#             <==  Beginner Level Questions ==>
# Q.1)Write a program to create a tuple (1, 2, 3, 4, 5).
# QUESTION 1 (SOLUTION):
# tup = (1,2,3,4,5)
# print(tup)

# Q.2)Access the third element from the tuple (10, 20, 30, 40, 50).
# QUESTION 2 (SOLUTION):
# tup = (10,20,30,40,50)
# result = tup[2:3]
# print(result)

# Q.3)Check if the number 15 exists in the tuple (5, 10, 15, 20).
# QUESTION 3 (SOLUTION):
# import time
# tup = (5,10,15,20)
# exists = False
# for i in tup:
#     if i == 15:
#       exists = True
#       print("exists",i)
           
# Q.4)Concatenate two tuples (1, 2, 3) and (4, 5, 6).
# QUESTION 4 (SOLUTION):
# tup1 = (1,2,3)
# tup2 = (4,5,6)
# concatenate = tup1 + tup2
# print(concatenate)

# Q.5)Repeat the tuple (7, 8) three times.
# QUESTION 5 (SOLUTION):
# tup = (7,8)
# repeat_tuple = ()
# for i in range(3):
#     repeat_tuple += (i,)
# print(repeat_tuple)

# Q.6)Find the length of the tuple (100, 200, 300).
# QUESTION 6 (SOLUTION):
# tup = (100, 200, 300)
# count = 0
# for i in tup:
#     count += 1
#     print(count,)

# Q.7)Convert the list [1, 2, 3] into a tuple.
# QUESTION 7 (SOLUTION):
# li = [1,2,3]
# convert_in_tuple = ()
# for i in li:
#     convert_in_tuple += (i,)
#     print(convert_in_tuple)

# Q.8)Unpack the tuple (10, 20, 30) into variables a, b, and c.
# QUESTION 8 (SOLUTION):
# my_tuple = (10,20,30)
# a,b,c = my_tuple
# print(a,b,c)

# Q.9)Find the index of the element 25 in the tuple (10, 25, 30).
# QUESTION 9 (SOLUTION):
# my_tuple = (10, 25, 30)
# index = 0
# for i in range(len(my_tuple)):
#     if my_tuple[i] == 25:
#         index = i
#         break
# print(index)

# Q.10)Count how many times the number 2 appears in the tuple (1, 2, 2, 3).
# QUESTION 10 (SOLUTION):
# my_tuple = (1, 2, 2, 3)
# count = 0
# for i in my_tuple:
#     if i == 2:
#         count +=1
# print(count)

            #  <===  Intermediate Level Questions ===>
# Q.11)Extract a slice (20, 30, 40) from the tuple (10, 20, 30, 40, 50).
# QUESTION 11 (SOLUTION):
# my_tuple = (10, 20, 30, 40, 50)
# sliced_values = ()
# for i in range(1,4):
#     sliced_values += my_tuple[i],
# print(sliced_values)

# Q.12)Reverse the tuple (1, 2, 3, 4).
# QUESTION 12 (SOLUTION):
# my_tuple = (1, 2, 3, 4)
# reversed = ()
# for i in range(len(my_tuple)-1,-1,-1):
#     reversed += my_tuple[i],
#     print(reversed)
    
# Q.13)Access the number 4 from the nested tuple ((1, 2), (3, 4)).
# QUESTION 13 (SOLUTION):
# nested_tuple = ((1, 2), (3, 4))
# res = nested_tuple[1][1]
# print(res)

# Q.14)Create a tuple of squares (1, 4, 9, 16, 25) for numbers 1 to 5.
# QUESTION 14 (SOLUTION):
# my_tuple = (1,4,9,16,25)
# squares = ()
# for i in my_tuple:
#     squares += i**2,
# print(squares)

# Q.15)Demonstrate that tuples are immutable by attempting to change an element of (10, 20, 30).
# QUESTION 15 (SOLUTION):
# my_tuple = (10, 20, 30)
# try:
#     my_tuple[0] = 5  # This will raise an error
# except Exception as e:
#     print("Error:", e)

# Q.16)Merge a tuple (1, 2) with a list [3, 4] to form (1, 2, 3, 4).
# QUESTION 16 (SOLUTION):
# tup = 1,2
# li = [3,4]
# result = tup
# for item in li:
#     result += item,
# print(result)

# Q.17)Find the maximum and minimum values in the tuple (50, 20, 30).
# QUESTION 17 (SOLUTION):
# finding maximum
# tup = (20,30,99)
# max_value = tup[0]
# for item in tup:
#     if item > max_value:
#         max_value = item
# print(max_value)
# finding minimum
# tup = (50,20,30)
# min_value = tup[0]
# for item in tup:
#     if item < min_value:
#         min_value = item
# print(min_value)

# Q.18)Flatten the nested tuple ((1, 2), (3, 4)) into (1, 2, 3, 4).
# QUESTION 18 (SOLUTION):
# nested_tuple = ((1,2),(3,4))
# flatten = ()
# for outer in nested_tuple: 
#     for inner in outer:
#         flatten += inner,
# print(flatten)


# Q.19)Sort the tuple (30, 10, 20) into (10, 20, 30).
# QUESTION 19 (SOLUTION):
# my_tuple = (30, 10, 20)
# sorted_tuple = ()
# temp_list = [item for item in my_tuple]
# for i in range(len(temp_list)):
#     for j in range(i + 1, len(temp_list)):
#         if temp_list[i] > temp_list[j]:
#             temp_list[i], temp_list[j] = temp_list[j], temp_list[i]
# for item in temp_list:
#     sorted_tuple += (item,)
# print(sorted_tuple)


# Q.20)Find common elements between (1, 2, 3) and (2, 3, 4).
# tuple2 = (2,3,4,5,9)
# tuple1 = (1,2,3,5,7)
# common = ()
# for item1 in tuple1:
#     for item2 in tuple2: 
#         if item1 == item2:
#                 common += item1, 
# print(common)
# QUESTION 20 (SOLUTION):
