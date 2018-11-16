o = {}
n = int(input())
for i in range(n):
    k = [s for s in input().split()]
    country = k[0]
    for z in range(1, len(k)):
        o[k[z]] = country
m = int(input())
ans = []
for i in range(m):
    t = input()
    ans.append(o[t])

for i in ans:
    print(i)