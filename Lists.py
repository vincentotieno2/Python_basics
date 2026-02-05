fruits=["apple","banana","orange","mango","pineapple"]
fruits.append("guava")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.extend(["pixies","avocado","grapes"])
print(fruits)

fruits.insert(2,"tomato")
print(fruits)

fruits.pop()#remove the last by index
print(fruits)

fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)

print(len(fruits))# tells you how many items are in the list

print(fruits.count("mango")) #tells you the number of times a value appears in a list

# A tupple is a list that cannot be modified. it is different in that it uses parentheses instead of square brackets.

days=("Mon", "Tue", "wed", "Thur", "Fri", "Sat", "Sun")
print(days.count("Sat"))
print(days[3]) #you can print by a certain index



#a set is a type of data structure that has unique elements, that is no duplicates. And you use curly brackets instead of square or round brackets.

numbers={23,24,46,78,12}
numbers.add(79)
print(numbers)

numbers.discard(23)
print(numbers)

#dictionary is a data structure that have items as key-value pairs. Also use curly brackets.

country_capitals={"USA":"DC", "Canada":"Ottawa", "Kenya":"Nairobi", "China": "Beijing", "Japan":"Tokyo"}
print(country_capitals)

print(country_capitals["China"])

print(country_capitals["USA"])

country_capitals["India"]="New Delhi"
print(country_capitals)

del country_capitals["USA"]
print(country_capitals)

print(len(country_capitals))

numbers=[1,2,3,3,4,5,6,7]
numbers.append(9)
print(numbers)

numbers.remove(6)
print(numbers)

numbers.insert(4,24)
print(numbers)

numbers.pop(4)
print(numbers)

ages=(21,18,17,39)
print(ages[3])

student_id={5471,5499,5678,6100,2378}
student_id.add(54230)
print(student_id)

student_id.discard(5499)
print(student_id)
