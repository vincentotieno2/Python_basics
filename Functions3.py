def say_hi():
    print("Hi")
say_hi()

def greet(name):
    print("Hello", name)
greet("Vince")

def square(number):
    return number * number
result=square(5)
print(result)

def clean_text(text):
    return text.strip().lower()
name=clean_text("Hello  Vince")
print(name)

def repeat_word(word, num):
    for i in range (num):
        print(word)
repeat_word("python", 3)

def add(a,b):
    return a+b
def subtract (a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

print(add(17,23))
print(subtract (17,23))
print(multiply(17, 23))


def stats(a, b):
    total=a+b
    difference=a-b
    return total, difference
x,y=stats(11, 23)
print(x, y)
