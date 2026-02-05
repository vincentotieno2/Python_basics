a=3 #global variable
def add ():
    print (a) # a
add()

def addtwo():
    b=6 #local variable
    return a+b
print(addtwo())

def addthree():
   b=10
   return b+a
print(addthree())
