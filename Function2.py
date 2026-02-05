def greet():
    print("Hello World")
greet()

def is_even(num):
    if num%2==0:
        print("Even")
    else:
        print("Odd")
is_even(8)

def addnumbers(a,b):
    sum=a+b
    print(sum)
addnumbers(5,9)

def get_sum(num1, num2):
    sum1=num1+ num2
    print(sum1)
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
get_sum(num1, num2)

def get_product(num3, num4):
    product=num3*num4
    print(product)
num3=int(input("Enter first number:"))
num4=int(input("Enter second number:"))
get_product(num3, num4)

def clean_name():
    name="maRiA "
    print(name.strip().lower())
clean_name()

def say_hi():
    print("Hi")
say_hi()