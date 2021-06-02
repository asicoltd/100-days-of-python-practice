heightList = input("Input everyone's height with a whitespaces like : 12 23 43 11\n").split()
size = 0
for person in heightList:
    size += 1
for hi in range(0,size):
    heightList[hi] = float(heightList[hi])
total = 0
for person in heightList:
    total += person
print(total/size)