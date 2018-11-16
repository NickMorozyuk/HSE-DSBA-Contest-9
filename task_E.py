file = open("input.txt")
candidates = []
votes = []
total_votes = 0
for z in file:
    total_votes += 1
    z = z.replace("\n", "")
    if z not in candidates:
        candidates.append(z)
        votes.append(1)
    else:
        votes[candidates.index(z)] += 1

for i in range(len(votes)):
    if votes[i] > total_votes / 2:
        print(candidates[i])
        quit()


k = max(votes)
for i in range(len(candidates)):
    if votes[i] == k:
        print(candidates[i])
        votes[i] = 0


k = max(votes)
for i in range(len(candidates)):
    if votes[i] == k:
        print(candidates[i])