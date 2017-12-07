n = int(input())
if n%2==0:
	f = 1
	for i in range(1,n+1):
		if i%2==0:
			f = f*i
print(f)