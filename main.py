import random

print('DZ9')

randomList = []
for i in range(random.randint(3, 10)):
    randomList.append(random.randint(1, 9))
print(randomList)

newList = randomList[0:3:2] + [randomList[-2]]
print(newList)

print('Thank you for using')

########################################################

randomList = [random.randint(1, 9) for i in range(random.randint(3, 10))]
print(randomList)

newList = randomList[0:3:2] + [randomList[-2]]
print(newList)

print('Thank you for using')