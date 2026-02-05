#implicit type conversion
Num=10 # first example
Num1=20.00
print(Num1+Num)

firstname="Vincent" #second example
secondname="Otieno"
print(firstname+secondname)

#explicit type conversion
num_string="123"
num_int=23
num_string=int(num_string)
num_sum=num_int+num_string
print(num_sum) #output is 146

#float conversion function
num=10
num=float(num)
print(num) #output is 10.0

#example 2
A="123"
A=float(A)
print(A) #output is 123.0

#example 3
p=3
p=float(p)
print(p) #output is 3.0

#string conversion function
age= 10
age=str(age)
print("age :",age) #output is age:10

#example 2
a="4"
b=2
print(str(b)+a) #output is "24"

#example 3
Num1= 10
Num2="20"
print(str(Num1)+Num2) #output is "1020"
print(int(Num2)+Num1) #output is 30

#type conversion float to int
a=3.142
a=int(a)
print(a) #output is 3

A=10
A=str(A)
print(A) #output is "10"


