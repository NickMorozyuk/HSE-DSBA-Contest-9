file = open("input.txt")
k = []
for line in file:
    v = [s for s in line.split()]
    for e in v:
        k.append(e)
print(k)