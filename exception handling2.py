try:
    numerator=10
    denominator =0
    result=numerator/denominator
    print(result)

except:
    print("undefined calculation")

print("program finished")




try:
    data=[10.20,30]
    index=int(input("Enter an index:"))
    result=data[index]/int(input("Enter a divisor:"))
    print("Result is:", result)

except ValueError:
    print("Error: Invalid number entered")

except IndexError:
    print("Error: Index out of range")

except ZeroDivisionError:
    print("Error: Cannot divide by zero")

else:
    print("Calculation Successful")

finally:
    print("Program finished")