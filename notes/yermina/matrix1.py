n = int(input())
a = []
for i in range (0,n):
	a.append([0]*n)
for i in range (0,n):
	for j in range (0,n):
		if i+j==n-1 or i-j==0:
			a[i][j]=1
		if i+j>n-1 and i-j>0:
			a[i][j]=1
		if i+j<n-1 and i-j<0:
			a[i][j]=1
for i in range (0,n):
	for j in range (0,n):
		print(a[i][j], end=' ')
	print()