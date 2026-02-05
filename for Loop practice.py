numbers=[1,2,3,4,5,6,7,8,9,10]
for letter in numbers:
    print(letter, end="")
print()

names=["Vincent", "Victoria", "Lynn", "Dennis"]
for name in names:
    print("Hello", name)

for letter in numbers:
    if letter<=8:
        print(letter)

for letter in numbers:
    if letter==8:
        break
    print(letter)

for letter in numbers:
    if letter==3:
        continue
    print(letter)

for letter in numbers:
    if letter%2==0:
        continue
    print(letter)

for x in range(1,11):
    if x%2==0:
        continue
    print(x)

weight=88
while weight<=93:
    print(weight)
    weight+=1

population_per_county= 25
while population_per_county<=32:
    print(population_per_county)
    population_per_county+=2


for row in range(3):
    for col in range (4):
        print("X")
    print()