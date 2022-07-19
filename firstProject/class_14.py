
# Files and Paths

# absolute
# file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story.txt')

# specify the mode (by default, the mode is on read, 'r')
file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story.txt', 'r')

print(type(file))

# I/O - input/output

# relative
# file  = open('story.txt')

# print(file.readline())
# print(file.readline())
# print(file.readline())

file.close()

# raises ValueError: I/O operation on closed file
# file.readline()


file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story.txt')
while True:
    line = file.readline()
    if line == '':
        break
    elif line.endswith('\n'):
        line = line[:-1]

    print(line)
file.close()


file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story.txt')
# readlines returns a list of lines
l = file.readlines()
print(l)
file.close()


################ SIMPLER WAY TO WRITE THE LOOP ###############
# You can just use the for loop instead of writing a while loop and calling readline() function
file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story.txt')
for line in file:
    if line.endswith('\n'):
        line = line[:-1]
    print(line)
file.close()


# WRITING TO THE FILE
file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story2.txt', 'w')
print(type(file))
print(file.mode)  # w


file.write('This is my story\n')
file.write('and your story\n')
file.close()



# append
file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story2.txt', 'a')
file.write('The story goes like this ....\n')
# can write a sequence of elements by calling writelines()
l = ['apple\n', 'and banana and berry\n', 'End of the story\n']
file.writelines(l)
file.close()

### file
'''
file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story2.txt', 'r')

# all of the operations on file summarized
file.read() # a string that represents the content of the file

file.readline() # read one line

file.readlines()# returns a list of each element on each line

file.write('something') # writes the string to the end of the file, however, if the file has an existent content when we just 
start writing to the file, then it is going to rewrite the file (erases the previous content)

file.writelines(l) # writes each element in l(list) to the file

file.close()

'''
# possible modes
path = '/Users/aigerimkubanychbekova/Desktop/my/firstProject/story2.txt'

'''
open(path, 'w') # open a file for writing, can be existent or non-existent (creates the file if the file does not exist)
open(path, 'r') # open an existing file for reading
open(path, 'a') # opens an existing file for appending


'''
print(open(path, 'a'))

file2 = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story3.txt', 'w')
file2.write('I was created\n')
file2.write('This is a continuation\n')
file2.close()


#
# file2 = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story3.txt', 'w')
# file2.write('This should have been a continuation\n')
# file2.close()


file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story3.txt', 'r')

for line in file:
    print(line[:-1]) # no need to do file.readline()


# different OS paths
# MAC -> forward slash
# Windows -> 'C:\\Directory\\file.txt' -> backward slashes

# To make the code compatible with different operating system we can create path objects

# Use pathlib library

from pathlib import Path

p = Path('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story3.txt')
print(p)
print(type(p))


print(p.exists())
print(p.is_file())
print(p.is_dir())

file = p.open('r')
print(file.readlines())
file.close()

# pathlib and os.path


# Exception and Files

# x = int(input('Enter a digit:'))



#
# def funct():
#     a = 10
#     funct2(a)
#
#
# def funct2(str):
#     print(len(str))
#
#
# funct()


# # Catching an exception
# try:
#     x = int(input('Enter a digit:'))
#     print(x)
# except:
#     print('It was a string')
#
# ###########the exception is not caught
# x = int(input('Enter a digit:'))
#
# print("The program didn't break")
# ##############



# catching block syntax

'''
try:
    statements that will be executed once
    if any exception is raised, control is passed to except
except:
    statements that will execute after the exception was raised
else:
    statements that will execute only if the exception was not raised
finally:
    statements that execute no matter exception was raised or not
  

# the last two clauses are optional  
'''

try:
    file = open('non-existant path')
except:
    print('The path does not exist')
else:
    print('The path exists')
finally:
    print('This is printed anyways')


try:
    file = open('/Users/aigerimkubanychbekova/Desktop/my/firstProject/story3.txt')
except:
    print('The path does not exist')
else:
    print('The path exists')
finally:
    print('This is printed anyways')

