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
with open('hello.txt','r') as file:
    lines = file.readlines()
with open("reversed_data.txt",'w') as file:
    for line in reversed(lines):
       file.write(line)
       

