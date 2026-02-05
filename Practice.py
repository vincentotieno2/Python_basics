num=int(input("Enter the  number:"))
if num>0:
    print("positive")
elif num<0:
    print("negative")
else:
    print("number is zero")

weight=int(input("Enter the weight:"))
if weight<=1:
    cost=50
elif weight<=5:
    cost=100
else:
    cost=200
print("The shipping cost is Rs", cost)

num2=int(input("Enter 2nd number:"))
total=0

while num2>0:
    last_digit=num2%10
    total=total+last_digit
    num2=num2//10
print("The sum of digits is", total)
