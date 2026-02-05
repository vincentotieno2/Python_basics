numbers=[1,2,3,4,5,6,7,8,9,10]
for x in numbers:
    if x>5:
      print(x)

language="Python"
for x in language:
    print(x)

fruits=["apple", "banana", "cherry"]
for x in fruits:
    if x=="apple":
      print(x)

num=[1,2,3,4,5,6,7,8,9,10]
for x in num:
    if x==3:
        break
    print(x)

for x in num:
    if x==4:
        continue
    print(x)

Numbers=[1,2,3,4]
cars=["toyota", "audi", "mercedes", "bmw"]
for x in Numbers:
    for y in cars:
        print(x,y,end="")
    print()
