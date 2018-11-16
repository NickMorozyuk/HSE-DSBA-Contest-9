a = []
b = []
n = int(input())
for i in range(n):
    one, two = input().split()
    a.append(one)
    b.append(two)
k = input()
if k in a:
    print(b[a.index(k)])
else:
    print(a[b.index(k)])