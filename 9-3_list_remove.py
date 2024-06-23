a = [[4,1],[2,5],[4,0],[4,2],[3,4]]
n = len(a)
b = []

for i in range(n):
    if a[i][0] != 4:
        b.append(a[i])

print(b)

