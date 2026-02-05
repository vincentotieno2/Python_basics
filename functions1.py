def greet():
    print("Hello world")
greet()

def addnumbers():
    a=6
    b=8
    sum=a+b
    print(sum)
addnumbers()

def AddNumbers(num1,num2):
    sum=num1+num2
    print(sum)
AddNumbers(4,7)

def checknumber(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
checknumber(6)

def Getnumber(num):
    if num%1==0 and num%num==0:
        print("prime")
    else:
        print("not prime")
num1=int(input("Enter the number:"))
Getnumber(num1)