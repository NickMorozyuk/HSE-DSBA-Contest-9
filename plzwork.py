def op():
    return a[i][1]

d = {}
file = open("input.txt")
k = []
for line in file:
    line = line.replace("\n", "")
    v = [s for s in line.split()]
    for e in v:
        k.append(e)
for i in k:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1


a = {v:k for k, v in d.items()}





print(a)


