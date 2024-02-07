# import numbers


# n = int(input("Enter a number: "))
# print(n >=100)

# # Read three numbers
# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))
# number3 = int(input("Enter the third number: "))
 

# # largest_number = number1
 
# # if number2 > largest_number:
# #     largest_number = number2
 

# # if number3 > largest_number:
# #     largest_number = number3
 
# # # Print the result


# largest_number = max(number1, number2, number3)
# print("The largest number is:", largest_number)

# value = input("Enter plant name: ")
# if value == "Spathiphyllum":
#     print("Yes - "+ value +" is the best plant ever")
# elif value == "spathiphyllum":
#     print("No, I want a big Spathiphyllum!")
# else:
#    print("Spathiphyllum! Not, "+ value +"!")

# income = float(input("Enter the annual income: "))

# if income < 85528:
# 	tax = income * 0.18 - 556.02
# else:
# 	tax = ((income - 85528) * 0.32) + 14839.

# tax = round(tax, 0)

# if (tax < 0):
#     print("No Tax!")
# else:
#     print("The tax is:", tax, "thalers")
 
# year = int(input("Enter a year: "))

# if year < 1582:
# 	print("Not within the Gregorian calendar period")
# else:
#     if bool(year % 4) : print("Common year")
#     elif bool(year % 100) : print("Leap year")  
#     elif bool(year % 400) : print("Common year")
#     else: print("Leap year") 
4
# secret_number = 777

# print(
# """
# +================================+
# | Welcome to my game, muggle!    |
# | Enter an integer number        |
# | and guess what number I've     |
# | picked for you.                |
# | So, what is the secret number? |
# +================================+
# """)


# while int(input()) != secret_number:    
#     print("Ha ha! You're stuck in my loop!")

# print("Well done, muggle! You are free now.")


# import time

# for i in range(5):
#     print(str(i+1) + " Mississippi")
#     time.sleep(1)

# print("Ready or not, here I come!")

# while True:
#     password= input("Please enter the secret password: ")
#     if password == "chupacabra": break
# print("You've successfully left the loop.")

#word= input("Please enter a word : ")
# word=word.upper()
# new_word= ""
# for i in word:
#     if i != "A": 
#         if i != "E":
#             if i != "I":
#                 if i != "O":
#                     if i != "U":
#                         new_word = new_word + i
#                         continue
# print (new_word)

blocks = int(input("Enter the number of blocks: "))
height = 0
layer = 1
while layer <= blocks:
    height += 1
    blocks -= layer
    layer += 1
    
print("The height of the pyramid:", height)