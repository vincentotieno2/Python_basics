units=int(input("Enter the number of units:"))
if units<=100:
    bill=0
elif units<=200:
    bill= (units-100)*5
else:
    bill=(100*5)+(units-200)*10

print("Total bill amount is Rs",bill)


marks=int(input("Enter your marks:"))
if marks>=90:
    Grade="A"
elif marks>=75:
    Grade="B"
elif marks>=60:
    Grade="C"
elif marks>=40:
    Grade="D"
else:
    Grade="Fail"
print("Grade is",Grade)

GB=int(input("Enter your monthly mobile data usage in GB:"))
if GB<=2:
    bill=0
elif GB<=5:
    bill=(GB-2)*50
else:
    bill=(3*50)+(GB-5)*100
print("Total monthly bill is Rs",bill)

income=int(input("Enter your annual income:"))

if income<0:
    print("Invalid income")
elif income<=250000:
    tax=0
elif income<=500000:
    tax=(income-250000)*0.05
elif income<=1000000:
    tax=12500+(income-500000)*0.20
else:
    tax=112500+(income-1000000)*0.30
print("Total tax is Rs", tax)