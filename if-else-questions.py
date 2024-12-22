#1.) Write a Python program to check if a number is divisible by both 5 and 3.
# Question 1 (SOLUTION):

# number = int(input("enter a number that divisible by 5 and 3  "))
# if(number % 5 == 0 and number % 3 == 0):
#     print("yes number is divisible by 5 and 3")
# else:
#     print("not divisible by 5 and 3")

# 2.)Write a Python program to check if a character is a vowel or a consonant.
# Question 2:(SOLUTION)

# user = input("enter a vowel")
# if user.lower() in "aeiou":
#     print("its vowewl")
# else:
#     print("not vowel")

#3.) Write a Python program to check if a person is a teenager (age between 13 and 19).
# Question 3:(SOLUTION)

# user_age = int(input("enter your age"))
# if (user_age >= 13 and user_age <= 18):
#     print("you under the teenage")
# else:
#     print("you not in teenage")

#4.) Write a Python program to find the smallest of three numbers.
# Question 4:(SOLUTION)

# user_input1 = int(input("enter a number1 "))
# user_input2 = int(input("enter a number2  "))
# user_input3 = int(input("enter a number3  "))
# if(user_input1 <= user_input2 and user_input1 <= user_input3):
#     print("the smallest number is user_input1 ",user_input1)
# elif(user_input2 <= user_input1 and user_input2<= user_input3):
#     print("the smallest number is user_input2",user_input2)
# else:
#     print("the smallest number is user_input3",user_input3)

# 5.)Write a Python program to check if a number is within a specific range (e.g., between 1 and 100).
# Question 5:(SOLUTION)

# userInput = int(input("enter a number between 1 and 100  "))
# if(userInput >= 1 and userInput <=100):
#     print("you are range in between 1 to 100")
# else:
#     print("you are not i n range")

#6.) Write a Python program to check if a year is a century year (ends with 00).
# Question 6:(SOLUTION)

# user_input = int(input("enter a century year  "))
# if(user_input % 100 == 0):
#     print("its century year")
# else:
#     print("its no acentury year")

# Check if a number is positive, negative, or zero.
# Question 7:(SOLUTION)
# number = int((input("enter a number")))
# if (number > 0):
#     print("number is positive")
# elif number <0:
#     print("number negative")
# else:
#     print("number is zero")

# 8.)Check if a person can vote based on their age.
# Question 8:(SOLUTION)
# user_age = int(input("enter a age"))
# if user_age >= 18:
#     print("you are eligible for voting")
# else:
#     print("you are not eligible for voting")
  

# 9.)Determine if a number is odd or even.
# Question 9:(SOLUTION)
# num_check = int(input("enter a number"))
# if num_check % 2 == 0:
#     print("{} is an even number ".format(num_check))
# else:
#     print("{} is an odd number".format(num_check))

#10.)Implement a grading system based on score ranges.
# Question 10:(SOLUTION)
# name = input("enter your name : ")
# mark = int(input("enter your marks between 0 to 100 : "))
# if (mark >= 90 and mark<100):
#     print("A+ grade excellent  {}".format(name))
# elif mark >=80 and mark<90:
#     print("A grade excellent {}".format(name))
# elif mark >= 70 and mark <80:
#     print("B grade very good {}".format(name))
# elif mark >= 60 and mark <70:
#     print("B grade  good {}".format(name))
# elif mark >= 50 and mark <60:
#     print("B grade fairly good {}".format(name))
# elif mark >= 40 and mark <50:
#     print("B grade chal jaiga {}".format(name))
# else:
#     print("foy are fail {}".format(name))

# 11.(Determine the season based on the input month.)
# Question 11:(SOLUTION)
# month = input("enter a month name")
# if (month == "december" or month == "january" or month == "february"):
#     print("Season: Winter")
# elif (month ==  "march"or month =="april" or month =="may"):
#     print("Season : Spring")
# elif (month == "june" or month =="july" or month =="august"):
#     print("Season : summer")
# elif (month == "september" or month =="october"or month =="november"):
#     print("Season: fall")
# else:
#     print("enter a valid month")

    
#12.) Calculate discounts based on total bill amount.
# Question 12:(SOLUTION)
# bill = int(input("Enter the total bill amount: "))
# if bill > 500:
#     discount = bill * 0.2
#     print(f"Discount applied: rps{discount}")
# elif bill >= 200:
#     discount = bill * 0.1
#     print(f"Discount applied: rps{discount}")
# else:
#     discount = 0
#     print("No discount applied.")


# 13.)Check if a given year is a leap year.
# Question 13:(SOLUTION)
# year = int(input("enter a year"))
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("its a leap year")
# else:
#     print("this is not a leap year")

# 14.)Create a simple calculator for basic operations (+, -, *, /).
# Question 14:(SOLUTION)
# num1 = int(input("enter a number1 : "))
# num2 = int(input("enter a number2 : "))
# operator = input(f"enter a operator like +,-,*,/ : ")
# if (operator == "+"):
#     print(f"sum of {num1} and {num2} is {num1 + num2}")
# if (operator == "-"):
#     print(f"subtraction  of {num1} and {num2} is {num1 - num2}")
# if (operator == "*"):
#     print(f"multiplication of {num1} and {num2} is {num1 * num2}")
# if (operator == "/"):
#     print(f"division of {num1} and {num2} is {num1 // num2}")
# else:
#     print("invalid operator")

# 15.)Create a "Guess the number" game .
# Question 15:(SOLUTION)
# guess_no = int(input("guess the number between 1 to 10 : "))
# number = 7
# if guess_no > number:
#     print("to high number")
# elif guess_no < number:
#     print("very small number")
# else:
#     print("congratulation you got the number")
