k = []
d = {}
file = open("input.txt")
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

max_array = []
max = 0
a = list(d.items())
for i in range(len(a)):
    if a[i][1] > max:
        max = a[i][1]
        max_array = []
        max_array.append(a[i][0])
    if a[i][1] == max:
        max_array.append(a[i][0])

max_array.sort()

print(max_array[0])