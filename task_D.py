buyers = []
file = open("input.txt")
for line in file:
    line.replace("\n", "")
    v = [s for s in line.split()]
    a = []
    check_client = True
    for i in range(len(buyers)):
        if buyers[i][0] == v[0]:
            check_item = True
            for z in range(1, len(buyers[i]), 3):
                if buyers[i][z] == v[1]:
                    buyers[i][z + 1] += int(v[2])
                    check_item = False


            if check_item == True:
                buyers[i].append(v[1])
                buyers[i].append(int(v[2]))
            check_client = False
    if check_client == True:
        a.append(v[0])
        a.append(v[1])
        a.append(int(v[2]))
        buyers.append(a)

buyers.sort()

for i in range(len(buyers)):
    for z in range(1, len(buyers[i]), 2):
        for f in range(1, len(buyers[i]), 2):
            if buyers[i][z] < buyers[i][f]:
                buyers[i][z], buyers[i][f] = buyers[i][f], buyers[i][z]
                buyers[i][z + 1], buyers[i][f + 1] = buyers[i][f + 1], buyers[i][z + 1]

for i in range(len(buyers)):
    print(buyers[i][0] + ":")
    for z in range(1, len(buyers[i]), 2):
        print(buyers[i][z], buyers[i][z + 1])
