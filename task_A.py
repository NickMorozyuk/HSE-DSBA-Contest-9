n = int(input())
words = set()
words_lower = set()
for i in range(n):
    v = input()
    words.add(v)
    words_lower.add(v.lower())


ans = 0

k = [s for s in input().split()]
for i in range(len(k)):
    q = k[i].lower()
    if q in words_lower:
        if k[i] not in words:
            ans += 1
    else:
        if sum(1 for c in k[i] if c.isupper()) > 1 or k[i] == q:
            ans += 1

print(ans)