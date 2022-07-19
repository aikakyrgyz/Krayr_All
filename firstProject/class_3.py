# Wed, May 25, 2022

# if statements: conditional statements
# relational operators and boolean operators

# number = int(input("Enter a number:"))
#
# # if this number is positive, print positive
#
# if number>0: # True
#     print('The number entered was positive')
#
# print('End')


# truthiness

number  = 10 # True
string = 'some characters' # True
string = '' # False


# data = input('Enter anything: ') # as long as it is not empty
#
# if data:
#     print('You entered something')


# data = bool(input("Enter something: "))
#
# if data:
#     print('You entered something')


##################################
# num = int(input('Enter a number')) # -5
# if num > 0: # -5 -> False
#     print('Positive')
# elif num < 0:
#     print('Negative')
# else:
#     print('It was zero')
# # only one else statement can belong to this structure
# print('End')
##############


#########################
# evaluates each if statement in order, no matter what the previous evaluation was
# num = int(input('Enter a number')) # -5
# if num > 0:
#     print('Positive')
# if num == 5:
#     print('It was 5')
# if num>0 and num ==5: # True and True -> True
#     print("postive and 5")
# if num<0:
#     print('Negative')
# else:
#     print('End')
###################

# while loops


# x = 2
# print(x) # 2
# x = 5
# print(x) #5

##############################################

counter = 0
while True:
    if counter == 5:
        break   # break the program, get out of the while loop
    print('Hello')
    counter += 1  # counter = counter + 1 # incrementing
print("END")
# first loop:
    # print Hello -> counter +=1 -> 0 + 1 = 1 <- couunter
    # print Hello -> counter +=1 -> 1 + 1 = 2 <- counter
    # print Hello -> counter +=1 -> 2 + 1 = 3 <- counter
    # counter = 5


######################################
# num = int(input('Enter an integer')) # 10
#
# while num > 0:
#     print(num)
#     num -= 1 # decrementing # num = num - 1
#
# print('End')


######################################

# while True:
#     name = input('Enter your name')
#     if name == '':
#         print('Please enter it again')
#     else:
#         break
# print(f'You entered {name}')

######################################

# or alternatively

# name = ''
# # name = 'John'
#
# while name == '':
#     name = input('Enter your name')
#
#     if name == '':
#         print('The input was empty, please reenter')
#
# print(f'You entered {name}')


########################################
# sum = 0
# count = 0
# print('Please enter 5 positive numbers')
#
# while count < 5:
#     num = int(input('Next number: '))
#     if num == 0:
#         print('The number was zero')
#         break
#     else:
#         sum += num # sum = sum + num # 1st: 0 + 5 = 5 <- sum
#                                      # 2nd: 5 + 10 = 15 <-  sum
#                                     # 3rd: 15 + 20 = 35 <-  sum
#
#         count += 1                   # 1st: 0 + 1
#                                     # 2nd: 1 + 1 = 2 <- count
# else:
#     print(f'The sum of the numbers was {sum}')

##########################################


# [5, 10, 15, 20]
# [0,  1,  2,  3]
# data type

#############################################
my_range = range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]
index = 0
sum = 0

while index < len(my_range):
    sum += my_range[index]
    index += 1

print('The sum is', sum)


#############################################
# 1. 0 < 9 -> True:
        # 0 + my_range[0] = 0 + 1 = sum
        # index = 0 + 1 = 1

# 2. 1 < 9 -> True:
        # sum = 1 + my_range[1] = 1 + 2 = 3
        # index = 1 + 1 = 2

# 9. 8 < 9 -> True:
        # sum = 36 + my_range[8] = 36 + 9 = 45
        # index = 8 + 1 = 9

# for

# the difference between the while loop and for loop
# you want to use the while loop: When you do not EXACTLY know how many times you want to
# run the block of code

# you want to use the for loop:  When you EXACTLY know how many times you want to run that code


#############################################

# rewriting the previous while with a for loop


# range(1, 10) # [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0

for number in range(1, 10):
    sum += number
    #1. sum = 0 + 1
    #2. sum = 1 + 2
    #....

print('The sum is:', sum)

#############################################

range(1, 10, 2)  # [1, 3, 5, 7, 9]
# range(start, stop, step)

for number in range(0, 100, 2):
    if number == 98:
        print(number)
    else:
        print(number, end = ', ')


for i in range(100):
    print('YEY ')


################ SLICING ################

"""
>>> fruit = 'apple'
>>> # slicing
>>> fruit[0]
'a'
>>> 'apple'[0]
'a'
>>> 'apple'[3]
'l'
>>> word = 'interesting'
>>> 'interesting'[0:8]
'interest'
>>> word[0:8]
'interest'
>>> word = word[0:8]
>>> word
'interest'
>>> # 'string'[start:end:step]
>>> # 'string'[start:end]
>>> # 'string'[:end]
>>> # 'string'[start]
>>> # 'string'[end]
>>> # 'string'[any_index]
>>> '01234567'[0:7:2]
'0246'
>>> fruit[:3]
'app'
>>> fruit[0:2]
'ap'
>>> fruit[0::2]
'ape'
>>> fruit[::1]
'apple'
>>> fruit[::-1]
'elppa'
>>> # 'string'[::step]
"""

# three ways to comment:
""" comment """
''' comment '''
# one line comment


