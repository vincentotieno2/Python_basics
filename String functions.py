#f-string function enables us to put variables directly inside the string
from ctypes import pythonapi

name="Vincent"
age= 28
is_student = True

print("My name is " + name+",I am "+ str(age) + " years old, and student status is "+ str(is_student) + ".")
print(f"My name is {name}, I am {age} years old, and student status is {is_student}.")
#f-string enables the code toi be shorter, cleaner and easier to read.

#Split function helps to break a big string into smaller strings.
#Sytax is variable.split("separator")

Stamp= "2026-09-20 14:30" #separate date and time.
print(Stamp.split("-")) #'2026, '09', '20' , '14:30'

csv_file="1234, Max, USA, 1998-12-23, M"
print(csv_file.split(",")) #'1234', 'Max', 'USA', '1998-12-23', 'M'

#Mulitplier function enables you to repeat the string multiple times.
#Syntax is string* number
print("ha"*5) #output is hahahahaha
print("="*3) # this function is used to repeat characters to create clear sections in output

#extraction functions. Words are broken down into characters which are seen as indices, either positive indices or negative
#indexing and slicing
#syntax is variable[index]
text="python"
#extracting the first character
print(text[0]) #output is p in the positive position
print(text[-6]) #output is p in the negative index position

#extracting the last character
print(text[5]) #output is n positive position
print(text[-1]) #output is n negative position

#slicing function is used to extract a portion of a string
#syntax is variable[start point:end point]
date="2026-01-20"
#extract the year
print(date[0:4]) #output is 2026 , the starting point is 0 and the end point 4.
print(date[:4]) #another style if your starting point is zero.

#extract month
print(date[5:7]) #output is 01

#extract the day
print(date[8:]) #output is 20
