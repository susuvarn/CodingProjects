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

# blocks = int(input("Enter the number of blocks: "))
# height = 0
# layer = 1
# while layer <= blocks:
#     height += 1
#     blocks -= layer
#     layer += 1
    
# print("The height of the pyramid:", height)

# c0 =  int(input("Enter a non-zero non-negative value: \n"))
# steps = 0

# while c0 != 1:
    
    
#     if (c0 % 2 == 0):
#         c0 = c0 // 2
#         print(str("\n"), c0)
#     else:
#         c0 = (3 * c0) + 1
#         print(str("\n"), c0)

#     steps+=1
# else:
#     print("\n Total steps :", str(steps))


# for i in range (1,11,2):
#     print(i)

# x = 1
# while x < 11:
#     if( x % 2 != 0):
#         print(x)
#     x+=1

# for ch in "abch@pythoninstitute.org":
#     if ch == "@":
#         break
#     print(ch, sep="_", end="" )

# for d in "0165031806510":
#     x = "x"
#     if d != "0":
#         print(d, end="")
#         continue
    
#     print(x, end="")
    
# n = 3
# while n > 0:
#     print(n + 1)
#     n -= 1
# else:
#     print(n)

# i = 15
# x = 4
# y = 1
 
# a = x & y
# b = x | y
# c = ~x  # tricky!
# d = x ^ 5
# e = x >> 2
# f = x << 2



# print(a, b, c, d, e, f)

# numbers = [10, 5, 7, 2, 1]
# print("Original list contents:", numbers)  # Printing original list contents.

# numbers[0] = 111
# print("\nPrevious list contents:", numbers)  # Printing previous list contents.

# numbers[1] = numbers[4]  # Copying value of the fifth element to the second.
# print("Previous list contents:", numbers)  # Printing previous list contents.

# print("\nList length:", len(numbers))

# hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# number = int(input("Enter a number to insert: "))
# hat_list[3] = number
# # Step 1: write a line of code that prompts the user
# # to replace the middle number with an integer number entered by the user.

# del hat_list[4]
# # Step 2: write a line of code that removes the last element from the list.

# print(len(hat_list))# Step 3: write a line of code that prints the length of the existing list.

# print(hat_list)

# variable_1 = 1
# variable_2 = 2
# print (variable_1, variable_2) 
# variable_1, variable_2 = variable_2, variable_1

# print (variable_1, variable_2)

# my_list = [10, 1, 8, 3, 5]
# print(my_list)
# my_list[0], my_list[4] = my_list[4], my_list[0]
# my_list[1], my_list[3] = my_list[3], my_list[1]
 
# print(my_list)

# # step 1
# beatles = []
# print("Step 1:", beatles)

# # step 2
# beatles.append("John Lennon")
# beatles.append("Paul McCartney")
# beatles.append("George Harrison")
# print("Step 2:", beatles)

# # step 3
# for i in range(2):
#     name = input("Enter band member name: \n")
#     beatles.append(name)
# print("Step 3:", beatles)

# # step 4
# del beatles[-1]
# del beatles[-1]
# print("Step 4:", beatles)

# # step 5
# beatles.insert(0,"Ringo Starr")
# print("Step 5:", beatles)


# # testing list legth
# print("The Fab", len(beatles))

# list = []
# swapped = True
# num = int(input("Enter the number of elements to sort"))

# for i in range(num):
#     val = float(input("Enter the element: "))
#     list.append(val)

# print("The original list: ",list)

# # while swapped:
# #     swapped = False
# #     for i in range(len(list)-1):
# #         if list[i] > list[i+1]:
# #             swapped = True
# #             list[i], list[i+1] = list[i+1], list[i]

# list.sort()

# print("Sorted list", list)      

# list.reverse()

# print("Reversed list", list) 

# my_list = [17, 3, 11, 5, 1, 9, 7, 15, 13]
# largest = my_list[0]
# for i in my_list[1:]:
#     if i>largest:
#         largest = i
# print(largest)

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# to_find = 5678
# found = False

# for i in range(len(my_list)):
#     if  to_find == my_list[i]:
#         found = True
#         break

# if found : print("Element found")
# else: print("Element not found")

# bets = [3, 7, 11, 42, 34, 49]
# bets.sort()
# drawn = [5, 11, 9, 42, 3, 49]
# drawn.sort()

# hits = 0

# for i in bets:
#     if i in drawn:
#         hits += 1

# print(hits)

# list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
# print("Original List ", list)

# new_list = []

# for i in list:
#     if i not in new_list:
#         new_list.append(i)


# print("The list with unique elements only:")

# print(new_list)

# board = [["X" for i in range(8)] for j in range(8)]
# print(board)
# board[0][0] = "ROOK"
# board[0][7] = "ROOK"
# board[7][0] = "ROOK"
# board[7][7] = "ROOK"
# board[4][2] = "KNIGHT"
# board[3][4] = "PAWN"
# print(board)


# temps = [[0.0 for i in range(24)] for j in range(31)]

# total = 0.0
 
# for day in temps:
#     total += day[11]
 
# average = total / 31
 
# print("Average temperature at noon:", average)
my_list = [[0, 1, 2, 3] for i in range(3)]
print(my_list[2][0])
 