marks=int(input("Enter your marks:"))

if marks<0 or marks>100:
    print("Please enter a valid number")
elif marks>=80:
    print("A")
elif marks>=60:
    print("B")
elif marks>=40:
    print("C")
else:
    print("Fail")


balance=float(input("Enter your account balance:"))
withdrawal=float(input("Enter your withdrawal amount:"))

if withdrawal<=0:
    print("Invalid amount")
elif withdrawal>balance:
    print("Insufficient funds")
else:
    balance-=withdrawal
    print("Withdrawal successful")
    print("Remaining balance:",balance)

height=float(input("Enter your height:"))

if height<0:
    print("Enter a valid height")
elif height<120:
    print("Not allowed")
elif height<=139:
    print("Allowed with supervision")
else:
    print("Allowed")