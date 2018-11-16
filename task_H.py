o = {}
ans = []
k = []
file = open("input.txt")
for line in file:
    for word in line.split():
        k.append(word)

for i in k:
    if i not in o:
        o[i] = 1
    else:
        o[i] += 1
    ans.append(o[i] - 1)

for i in ans:
    print(i, end = " ")