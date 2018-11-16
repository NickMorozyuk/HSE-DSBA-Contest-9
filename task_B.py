parties = []
votes = []
remainder = []
places = []
file = open("input.txt")
for line in file:
    name = ""
    v = [s for s in line.split()]
    for i in range(len(v) - 1):
        name += str(v[i]) + " "
    name = name[:-1]
    parties.append(name)
    votes.append(int(v[len(v) - 1]))
    remainder.append(0)
    places.append(0)

total_votes = sum(votes)
pic = total_votes / 450

for i in range(len(remainder)):
    remainder[i] = votes[i] % pic
    places[i] = votes[i] // pic

a = remainder
while sum(places) != 450:
    places[a.index(max(a))] += 1
    a[a.index(max(a))] = 0
    if sum(a) == 0:
        a = remainder

for i in range(len(parties)):
    print(parties[i], int(places[i]))