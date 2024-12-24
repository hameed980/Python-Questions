# QUESTION1 (SOLUTION):
# with open('hello.txt','w') as f:
    # f.write("hello world")

# QUESTION2 (SOLUTION):
# with open('hello.txt','r') as f:
#     data = f.read()
#     print(data)

# QUESTION3 (SOLUTION):
# with open('hello.txt', 'a') as file:
    # file.write('\nThis is a new line.')
    
# QUESTION4 (SOLUTION):
# with open('hello.txt') as f:
#     line = f.readlines()
#     print(len(line))

# QUESTION5 (SOLUTION):
# import os
# print(os.path.exists("hello.txt"))

# QUESTION6 (SOLUTION):
# li = (['Alice', 'Bob', 'Charlie'])
# with open("hello.txt",'w') as f:
#     for name in li:
#         f.write(name + '\n')  
  
# QUESTION7 (SOLUTION):
# with open('hello.txt','r') as f:
#     data = f.readlines()
#     print([name.strip() for name in data])

# QUESTION8 (SOLUTION):
# with open('hello.txt','r') as file:
#     data = file.read()
#     print(data)
# with open("copy.txt",'w') as file:
#     file.write(data)
    
#  QUESTION9 (SOLUTION):
# with open('hello.txt','r') as f:
#     data = f.read()
#     content = data.split()
#     print(len(content))

# QUESTION10 (SOLUTION):
# with open('hello.txt','r') as file:
#     lines = file.readlines()
# with open("reversed_data.txt",'w') as file:
#     for line in reversed(lines):
#        file.write(line)

# QUESTION 11 (SOLUTION):
# from collections import Counter
# with open("hello.txt",'r') as f:
#     data = f.read()
#     frequency = Counter(data)
# print(dict(frequency))

# QUESTION 12 (SOLUTION):
# with open('hello.txt','r') as f:
#     data = f.read()
#     new_data = data.replace("hello",'hi')
# with open("hello.txt",'w') as f:
#     f.write(new_data)
# print(new_data)

# QUESTION 13(SOLUTION):
# with open('hello.txt','r') as file1, open('copy.txt','r') as file2,open('merged.txt','w') as outfile:
#     outfile.write(file1.read() + '\n' + file2.read())
    
# QUESTION 14(SOLUTION):
# with open("hello.txt",'r') as f:
#     line = f.readlines()
# with open("hello.txt",'w') as f:
#     for i in line:
#        if i.strip():
#            f.write(i)

# QUESTION 15(SOLUTION):
import csv
# data = [["Name","Age"],
#         ["abdul",18],
#         ['hameed',19]
# ]
# with open('hello.txt','w',newline='') as f:
#    writer =  csv.writer(f)
#    writer.writerows(data)

# QUESTION 16(SOLUTION):
# with open('hello.txt','r') as f:
#     data = csv.reader(f)
#     for i in data:
#         print(i)

# QUESTION 17(SOLUTION):
# with open('copy.txt','r') as f:
#     data = f.readlines()
# data.sort()
# with open("copy.txt",'w') as f:
#     f.writelines(data)

# QUESTION 18(SOLUTION):
# with open('hello.txt','r') as f:
#     data = f.read()
# unique_words = set(data.split())
# print(len(unique_words))
    
# QUESTION 19(SOLUTION):
# num1 = 10
# num2 = 0
# try:
#     result = num1/num2
#     print(result)
# except ZeroDivisionError as e:
#     with open('error.log','a') as f:
#         f.write(f'Error {e} \n')

# QUESTION 20(SOLUTION):
# import json
# data = {"name":"abdul","age":18}
# with open ('data.json','w') as f:
#     json.dump(data,f)
# with open ('data.json','r') as f:
#     result = json.load(f)
# print(result)