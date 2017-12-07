n,m = input().split()
n = int(n)
m = int(m)
M=[]
names = [x for x in input().split()]

for i in range(0,n):
    M.append([int(a) for a in input().split()])
max_m = []
for j in range(0,m):
    max_r = -10000000
    for i in range(0,n):
        if max_r < M[i][j]:
            max_r = M[i][j]
            max_i = i
    max_m.append(max_i)
max_n = -1
for i in range(0,n):
    print(max_m.count(i))
    if max_n < max_m.count(i):
        max_n = max_m.count(i)
        ind = i
if max_n>m/2:
    print(names[ind])
else:
    print(-1)
