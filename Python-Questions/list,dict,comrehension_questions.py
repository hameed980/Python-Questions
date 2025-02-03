
# List Comprehension Questions:
# 1. Create a list of squares of numbers from 1 to 10.
# QUESTION 1 (SOLUTION):
li = [i**2 for i in range(1,11)]
print(li)
# 2. Generate a list of even numbers between 1 and 20.
list1 = [i for i in range(1,21) if i%2 ==0]
print(list1)

# 3. Create a list of odd numbers between 1 and 15.
odd_num = [i for i in range(1,15) if i%2 !=0]
print(odd_num)
# 4. Filter a list to include only strings starting with "a".
words = ["apple", "banana", "apricot", "cherry"]
filter_word = [word for word in words if word[0] == ('a')]
print(filter_word)

# 5. Create a list of the lengths of each word in a given sentence.
sentence = 'Python is fantastic'
length_word = [len(word) for word in sentence.split()]
print(length_word)

# 6. Generate a list of numbers divisible by 3 and 5 from 1 to 50.
generating_no = [num for num in range(1,51) if num%3 == 0 and  num%5==0]
print(generating_no)

# 7. Flatten a nested list.
nested_list = [[1, 2], [3, 4], [5, 6]]
flatten_list = [column for row in nested_list  for column in row]
print(flatten_list)

# 8. Convert all words in a list to uppercase.
# 9. Create a list of tuples (number, square).
# 10. Generate a list of prime numbers between 2 and 20.


# Dictionary Comprehension Questions:
# 1. Create a dictionary of squares for numbers 1 to 5.
# 2. Create a dictionary from two lists: keys and values.
# 3. filter a dictionary to include only items with values greater than 2.
# 4. Create a dictionary with numbers as keys and their cubes as values.
# 5. Invert a dictionary (swap keys and values).
# 6. Create a dictionary with characters and their ASCII values.
# 7. Merge two dictionaries with common keys summed.
# 8. Create a dictionary with numbers and their parity (even/odd).
# 9. Count the frequency of each character in a string.
# 10. Create a dictionary grouping numbers by their remainder when divided by 3.
# '''
