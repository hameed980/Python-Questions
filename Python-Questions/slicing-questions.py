'''
Questions:
1.)Reverse a list arr = [1, 2, 3, 4, 5].

2.)Extract the first 4 elements from arr = [10, 20, 30, 40, 50, 60].

3.)Extract the last 3 elements from arr = [5, 10, 15, 20, 25].

4.)Extract every second element from arr = [1, 2, 3, 4, 5, 6].

5.)Extract elements between indices 2 and 5 from arr = [0, 1, 2, 3, 4, 5].

6.)Extract every third element from arr = [10, 20, 30, 40, 50, 60, 70].

7.)Reverse part of the list from index 1 to 4 in arr = [1, 2, 3, 4, 5, 6].

8.)Extract the middle 3 elements from arr = [1, 2, 3, 4, 5, 6, 7].

9.)Extract every second element in reverse order from arr = [10, 20, 30, 40, 50].

10.)Extract elements from index 1 to -2 in arr = [100, 200, 300, 400, 500, 600].

11.)Extract all odd-indexed elements from arr = [1, 2, 3, 4, 5, 6, 7, 8].

12.)Combine elements from index 0 to 2 and index 4 to 5 in arr = [1, 2, 3, 4, 5, 6].

13.)What happens if the start and stop indices are equal, e.g., arr[2:2]?

14.)Extract the substring "yth" from the string s = "Python".

15.)Duplicate a list using slicing, e.g., arr = [1, 2, 3].

16.)Slice out the first half of arr = [1, 2, 3, 4, 5, 6, 7, 8].

17.)Slice out the second half of arr = [1, 2, 3, 4, 5, 6, 7, 8].

18.)Remove the last element from arr = [10, 20, 30, 40, 50] using slicing.

19.)Remove the first element from arr = [10, 20, 30, 40, 50] using slicing.

20.)Extract all elements except the first and last from arr = [1, 2, 3, 4, 5].
'''


# 1.)Reverse a list 
# QUESTION 1 (SOLUTION):
# arr = [1, 2, 3, 4, 5]
# update = arr[::-1]
# print(update)

#2.)Extract the first 4 elements from
# QUESTION 2 (SOLUTION):
# arr = [10, 20, 30, 40, 50, 60]
# update = arr[:4]
# print(update)

#3.)Extract the last 3 elements from 
# QUESTION 3 (SOLUTION):
# arr = [5, 10, 15, 20, 25]
# update = arr[-3:]
# print(update)

#4.)Extract every second element from 
# QUESTION 4 (SOLUTION):
# arr = [1, 2, 3, 4, 5, 6]
# update = arr[::2]
# print(update)

# 5.)Extract elements between indices 2 and 5 from 
# QUESTION 5 (SOLUTION):
# arr = [0, 1, 2, 3, 4, 5]
# update = arr[2:6]
# print(update)

#6.)Extract every third element from
# QUESTION 6 (SOLUTION):
# arr = [10, 20, 30, 40, 50, 60, 70]
# update = arr[::3]
# print(update)

#7.)Reverse part of the list from index 1 to 4 in 
# QUESTION 7 (SOLUTION):
# arr = [1, 2, 3, 4, 5, 6]
# update = arr[:1] + arr[1:5][::-1] + arr[5:]
# print(update)

#8.)Extract the middle 3 elements from 
# QUESTION 8 (SOLUTION):
# arr = [1, 2, 3, 4, 5, 6, 7]
# update = arr[2:5]
# print(update)

#9.)Extract every second element in reverse order from
# QUESTION 9 (SOLUTION):
# arr = [10, 20, 30, 40, 50]
# update = arr[-1::-2]
# print(update)

#10.)Extract elements from index 1 to -2 in 
# QUESTION 10 (SOLUTION):
# arr = [100, 200, 300, 400, 500, 600]
# update = arr[1:-1]
# print(update)

#11.)Extract all odd-indexed elements from 
# QUESTION 11 (SOLUTION):
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# update = arr[1::2]
# print(update)

#12.)Combine elements from index 0 to 2 and index 4 to 5 in 
# QUESTION 12 (SOLUTION):
# arr = [1, 2, 3, 4, 5, 6]
# update = arr[:3]+arr[4:]
# print(update)

#13.)What happens if the start and stop indices are equal, e.g., arr[2:2]?
# QUESTION 13 (SOLUTION):
# in this case array will be empty

# 14.)Extract the substring "yth" from the string s = "Python".
# QUESTION 14 (SOLUTION):
name = "python"
update = name[1:4]
print(update)

#15.)Duplicate a list using slicing, e.g., arr = [1, 2, 3].
# arr = [1,2,3]
# update = arr[:]
# print(update)

#16.)Slice out the first half of 
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# update = arr[:4]
# print(update)

#17.)Slice out the second half of
# QUESTION 17 (SOLUTION):
# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# update = arr[4:]
# print(update)

#18.)Remove the last element from 
# QUESTION 18 (SOLUTION):
# arr = [10, 20, 30, 40, 50]
# update = arr[:-1]
# print(update)

#19.)Remove the first element from 
# QUESTION 19 (SOLUTION):
# arr = [10, 20, 30, 40, 50]
# update =arr[1:]
# print(update)

#20.)Extract all elements except the first and last from 
# QUESTION 20 (SOLUTION):
# arr = [1, 2, 3, 4, 5]
# update = arr [1:-1]
# print(update)