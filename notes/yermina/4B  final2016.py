n = int(input())
m = [int(x) for x in input().split()]
a = []
for i in range(0,n):
	if m[i]%2!=0 and m[i] not in a:
		a.append(m[i])
print(len(a))