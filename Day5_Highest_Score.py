scoreList = input("Add all scores with whitespace like 12 32 45\n").split()
max = -1
size = 0
for n in scoreList:
    size += 1
for n in range(0,size):
    scoreList[n] = int(scoreList[n])
for score in scoreList:
    if score >= max:
        max = score
print(max)