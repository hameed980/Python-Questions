'''
Here are some **basic beginner-level `while` loop questions**:

1. **Print Numbers from 1 to 10**  
2. **Sum of Numbers from 1 to N**  
3. **Print Even Numbers from 1 to N**  
4. **Print Multiplication Table of a Number**  
5. **Reverse a Given Number**  
6. **Count the Digits of a Number**  
7. **Find the Factorial of a Number**  
8. **Print the First N Fibonacci Numbers**  
9. **Check if a Number is Palindrome**  
10. **Keep Asking for Input Until "exit" is Entered**  
11. **Find the Sum of Digits of a Number**  
12. **Print Numbers from N Down to 1** 
13. **Display All Divisors of a Num**  
14. **Guess the Correct Number (Simple Game)**  
15. **Print a Triangle Pattern of Numbers Using `while`**  

Would you like solutions and explanations for any of these questions?
'''
# 1. **Print Numbers from 1 to 10**  
# QUESTION 1:(SOLUTION)
# i = 1
# while i <=10:
#     print(i)
#     i+= 1

#2. **Sum of Numbers from 1 to N**  
# QUESTION 2:(SOLUTION):
# num = int(input("enter a number"))
# i = 1
# total = 0
# while i<= num:
#     total += i
#     i +=1
#     print("the sum of numbers from 1 to" ,num , "is", total)

# 3. **Print Even Numbers from 1 to N**  
# QUESTION 3:(SOLUTION)
# num = int(input("enter a number"))
# i = 1
# while i<=num:
#     if i % 2 == 0:
#       print(i)
#     i +=1

# 4. **Print Multiplication Table of a Number**  
# QUESTION 4:(SOLUTION)
# user = int(input("enter a number "))
# i = 1
# while i<=10:
#    print(f"{user} X {i} = {user *i}")
#    i+=1

#5. **Reverse a Given Number**  
# QUESTION 5:(SOLUTION)
# using for loop
# num = 1234
# reversed_num = ''
# for digit in str(num):
#     reversed_num = digit + reversed_num
# print(reversed_num)
# using while loop
# num = 12345
# reverse_num = 0
# while num > 0:
#     digit = num % 10
#     reverse_num =reverse_num *10 +digit
#     num //= 10
#     print("reversed digit", reverse_num)

#6. **Count the Digits of a Number**  
# QUESTION 6:(SOLUTION)
# num = int(input("Enter a number: "))
# if num == 0:
#     print("Number of digits: 1")
# else:
#     count = 0
#     while num > 0:
#         num //= 10
#         count += 1
#     print("Number of digits:", count)

#7. **Find the Factorial of a Number**
# QUESTION 7:(SOLUTION)
#   
# num = int(input("Enter a number: "))  # Input a number
# factorial = 1  # Initialize factorial to 1 (since factorial of 0 is 1)

# # Check for non-negative number
# if num < 0:
#     print("Factorial does not exist for negative numbers.")
# else:
#     while num > 0:  # Loop to multiply the current value with the next smaller number
#         factorial *= num  # Multiply factorial by the current num
#         num -= 1  # Decrease the value of num by 1 in each iteration

#     print("Factorial is:", factorial)

#8. **Print the First N Fibonacci Numbers**  
# QUESTION 8:(SOLUTION)
# Input from the user
n = int(input("Enter the number of Fibonacci numbers to print: "))

if n <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    print("The first", n, "Fibonacci numbers are:")
    while count < n:
        print(a, end=" ")
        a, b = b, a + b  # Update to the next Fibonacci numbers
        count += 1  # Increment the counter
    print()

