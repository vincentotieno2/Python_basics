# flow control is where python decides which code is run and which code is skipped
#if statement ( when the condition is true, then run the code)
a=24
if a>=18:
    print("you are an adult") #True

b=29
if b<18:
    print("you are a minor") #False , so it skips the code (nothing happens)

#if...else (two choices)
c=13
if c>=18:
    print("you are an adult") #false (nothing happens)
else:
    print("you are a minor") #true

d=35
if d>=18:
    print("you are an adult") #true
else:
    print("you are a minor")# false (nothing happens)

#if...elif...else (multiple choices)

marks=81
if marks>=80:
    print("Grade A")
elif marks>=70:
    print("Grade B")
elif marks>=60:
    print("Grade C)")
else:
    print("Grade D")

#using the input() function with conditions
num1=int(input("Enter the number:",))
if num1>0:
    print("positive") #True
elif num1<0:
    print("negative")
else:
    print("zero")

num2=int(input("Enter the number:"))
if num2>0:
    print("positive")
elif num2<0:
    print("negative")
else:
    print("zero") #True

num3=int(input("Enter the number:"))
if num3>0:
    print("positive")
elif num3<0:
    print("negative") #True
else:
    print("zero")
