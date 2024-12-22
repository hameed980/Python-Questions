'''
   #     PYTHON BASIC FUNCTION QUESTIONS
   
Write a function to add two numbers.
Write a function to find the square of a number.
Write a function to check if a number is even or odd.
Write a function to find the factorial of a number.
Write a function to reverse a string.
Write a function to check if a string is a palindrome.
Write a function to count vowels in a string.
Write a function to find the maximum number in a list.
Write a function to calculate the sum of all numbers in a list.
Write a function to check if a number is prime.

# '''
# Q1.) Write a function to add two numbers.
# QUESTION 1(SOLUTION):
# def add (a,b):
#     return a+b
# res = add(2,6)
# print(res)

# Q2.) Write a function to find the square of a number.
# QUESTION 2(SOLUTION):
# def square(num):
#     res = num ** 2
#     print(res)
# square(int(input("enter a number")))

# Q3.) Write a function to check if a number is even or odd.
# QUESTION 3(SOLUTION):
# def check(num):
#      if num % 2 == 0:
#         return "even"
#      else:
#         return "odd"
# res = check(int(input("enter a number")))
# print(res)

# Q4.) Write a function to find the factorial of a number.
# QUESTION 4(SOLUTION):
# def factorial(n):
#     initila_value = 1
#     for i in range(1,n+1):
#         # initila_value = initila_value * i
#         initila_value *= i 
#     return initila_value
# result = factorial(int(input("enter a number.")))
# print(result)

# Q5.)Write a function to reverse a string.
# QUESTION 5(SOLUTION):
# def reverse(st):
#    return st[::-1]
# result = reverse("how are you")
# print(result)

# Q6.)Write a function to check if a string is a palindrome.
# QUESTION 6(SOLUTION):
# def check(word):
#     if word == word[::-1]:
#         return "palindrom"
#     else:
#         return "not"
# res = check(input("enter a palindrom words"))
# print(res)

# Q7.)Write a function to count vowels in a string.
# QUESTION 7(SOLUTION):
# Function
# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count
# # Example Usage
# result = count_vowels("education")
# print(result)

# Q8.)Write a function to find the maximum number in a list.
# QUESTION 8(SOLUTION):
# def maximum(li):
#     initila = li[0]
#     for i in li:
#       if i > initila:
#         initila = i
#     return(initila)
# res = maximum([12,45,67,89])
# print(res)

# Q9.)Write a function to calculate the sum of all numbers in a list.
# QUESTION 9(SOLUTION):
# def addition(add):
#     sum = 0
#     for i in add:
#         sum += i
#     return sum
# res = addition([12,45,32,11,2])
# print(res)

# Q10.)Write a function to check if a number is prime.
# QUESTION 10(SOLUTION):
# Function
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
result = is_prime(6)
print(result)
