'''
Create a dictionary with keys "name", "age", and "city" and values "John", 25, and "New York".
Access the value of the "name" keyCheck if a key exists.
Add key value pair "country": "USA" to the dictionary.
Check if the "age" key exists in the dictionary.
Delete a key-value pair Remove "city" from the dictionary.
Iterate through keys Print all keys in the dictionary.
Iterate through values Print all values in the dictionary.
Iterate through key-value pairs Print all key-value pairs in the dictionary.
Find the length of a dictionary Count the number of key-value pairs in the dictionary.
Merge two dictionaries Merge two dictionaries into one.
Create a dictionary from two lists Create a dictionary using keys = ["name", "age", "city"] and values = ["Alice", 30, "Los Angeles"]
Count word frequency in a string Count the frequency of each word in "hello world hello everyone".
Dictionary comprehension Create a dictionary with squares of numbers from 1 to 5.
 Sort dictionary by keys Sort the dictionary {"b": 2, "a": 1, "c": 3} by keys.
 Sort dictionary by values Sort the dictionary {"b": 2, "a": 1, "c": 3} by values.
Find the maximum value in a dictionary Find the key with the maximum value in {"a": 10, "b": 20, "c": 15}.
.Invert a dictionary Swap keys and values in {"a": 1, "b": 2, "c": 3}.
Remove duplicate values Remove duplicate values from {"a": 1, "b": 2, "c": 1}.
find common keys in two dictionaries Find common keys in {"a": 1, "b": 2, "c": 3} and {"b": 4, "c": 5, "d": 6}.
 Nested dictionaries Create a dictionary with nested dictionaries to store students' scores.
Check if two dictionaries are equal Check if {"a": 1, "b": 2} and {"b": 2, "a": 1} are equal.
Find the minimum value in a dictionary Find the key with the minimum value in {"a": 10, "b": 20, "c": 5}.
'''
# Q1.)Create a dictionary with keys "name", "age", and "city" and values
# # "John", 25,and "New York".
# QUESTION 1: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# print(my_dict)

# Q2.)Access the value of the "name" key
# QUESTION 2: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# print(my_dict["name"])

# Q3.)Add key value pair "country": "USA" to the dictionary.
# QUESTION 3: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# my_dict["country"] = "USA"
# print(my_dict)

# Q4.)Check if the "age" key exists in the dictionary.
# QUESTION 4: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# print("age" in my_dict)

# Q5.)Delete a key-value pair Remove "city" from the dictionary.
# QUESTION 5: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# my_dict.pop("city")
# print(my_dict)

# Q6.) Iterate through keys Print all keys in the dictionary.
# QUESTION 6: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# for i in my_dict:
    # print(i)
    
# Q7.)Iterate through values Print all values in the dictionary.
# QUESTION 7: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# for values in my_dict.values():
#     print(values)

# Q8.)Iterate through key-value pairs Print all key-value pairs in the dictionary.
# QUESTION 8: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# for key , value in my_dict.items():
#     print("keys. {} == values. {}".format(key,value))
    
# Q9.)Find the length of a dictionary Count the number of key-value pairs in the dictionary.
# QUESTION 9: (SOLUTION)
# my_dict = {"name":"john","age":25,"city":"New York"}
# length = len(my_dict)
# print(length)

# Q10.) Merge two dictionaries into one.
# QUESTION 10: (SOLUTION)
# dict1 = {"name":"john","age":25,"city":"New York"}
# dict2 = {"f-name":"david","weight":30.5,"country":"eng"}
# dict2.update(dict1)
# print(dict2)

# Q11.)Create a dictionary from two lists Create a dictionary using keys
# ["name", "age", "city"] and values = ["Alice", 30, "Los Angeles"]
# QUESTION 11: (SOLUTION)
# keys = ["name","age","city"]
values = ["Alice", 30, "Los Angeles"]
# my_dict = dict(zip(keys,values))
# print(my_dict)

# Q12.)Count word frequency in a string Count the frequency of each word in
# "hello world hello everyone".
# QUESTION 12: (SOLUTION)
text = "hello world hello everyone"
words = text.split()
word_count = {}
for word in words:
    # print(word)
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)

# Q13.)Dictionary comprehension Create a dictionary with squares of numbers from
# 1 to 5.
# QUESTION 13: (SOLUTION)
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)

# Q14.)Sort dictionary by keys Sort the dictionary {"b": 2, "a": 1, "c": 3} by keys.
# QUESTION 14: (SOLUTION)
# my_dict = {"b": 2, "a": 1, "c": 3} 
# res = dict(sorted(my_dict.items()))
# print(res)

# Q15.)Sort dictionary by values Sort the dictionary {"b": 2, "a": 1, "c": 3} 
# by values.
# QUESTION 15: (SOLUTION)
# my_dict = {"b": 2, "a": 1, "c": 3}
# sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
# print(sorted_dict)

# Q16.)Find the maximum value in a dictionary Find the key with the maximum value
# in {"a": 10, "b": 20, "c": 15}.
# # QUESTION 16: (SOLUTION)
# main ={"a": 10, "b": 20, "c": 15}
# max_val = max(main,key=main.get)
# print(max_val,main[max_val])

# Q17.)Invert a dictionary Swap keys and values in {"a": 1, "b": 2, "c": 3}.
# QUESTION 17: (SOLUTION)
# my_dict = {"a": 1, "b": 2, "c": 3}
# inverted_dict = {value: key for key, value in my_dict.items()}
# print(inverted_dict)

# Q18.)Remove duplicate values Remove duplicate values from {"a": 1, "b": 2, "c": 1}.
# QUESTION 18: (SOLUTION)
# my_dict = {"a": 1, "b": 2, "c": 1}
# unique_values = {value: key for key, value in my_dict.items()}
# print(unique_values)

# Q19.)find common keys in two dictionaries Find common keys in 
# {"a": 1, "b": 2, "c": 3} and {"b": 4, "c": 5, "d": 6}.
# QUESTION 19: (SOLUTION)
d1 = {"a": 1, "b": 2, "c": 3}
d2 =  {"b": 4, "c": 5, "d": 6}
common  = d1.keys() & d2.keys()
print(common)

# Q20.)Nested dictionaries Create a dictionary with nested dictionaries to 
# store students' scores.
# QUESTION 20: (SOLUTION)
# nested_dict = {
#     "david":{
#         "math": 60,
#         "science": 80
#     },
#     "john":{
#         "physics": 60,
#         "english": 80
#     }
# }
# print(nested_dict)

# 21.)Check if two dictionaries are equal Check if {"a": 1, "b": 2} and
# {"b": 2, "a": 1} are equal.
# QUESTION 21: (SOLUTION)
d1 = {"a":1,"b":2}
d2 = {"b":2,"a":1}
print(d1 == d2)

# Q22.)Find the minimum value in a dictionary Find the key with the minimum
# value in {"a": 10, "b": 20, "c": 5}.
# QUESTION22: (SOLUTION)
original_dict = {"a": 10, "b": 20, "c": 5}
min_val = min(original_dict,key=original_dict.get)
print(min_val,original_dict[min_val])

# Q1.)
# QUESTION 1: (SOLUTION)
# Q1.)
# QUESTION 1: (SOLUTION)
# Q1.)
# QUESTION 1: (SOLUTION)
# Q1.)
# QUESTION 1: (SOLUTION)