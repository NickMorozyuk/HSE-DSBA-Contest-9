o = {}
def vote(cand, votes):
    if cand in o:
        o[cand] += votes
    else:
        o[cand] = votes

file = open("input.txt")
for line in file:
    cand, votes = line.split()
    votes = votes.replace("\n", "")
    votes = int(votes)
    vote(cand, votes)

final = o.keys()
final = list(final)
final.sort()

for i in final:
    print(i, o[i])