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
max = 0
a = list(d.items())
final = []
for i in range(len(a)):
    one = a[i][0]
    two = a[i][1]
    final.append((two, one))
final.sort(reverse = True)
for i in range(len(a)):
    for z in range(len(a)):
        if final[i][0] == final[z][0] and final[i][1] < final[z][1]:
            final[i], final[z] = final[z], final[i]
for i in range(len(a)):
    print(final[i][1])