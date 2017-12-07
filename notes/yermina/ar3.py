n = int(input())

s = input()

a = [int(x) for x in s.split()]

temp=a[i]

for i in range(0, len(a)-1): # range(x, y) start from x to y (non incl)

	a[i]=temp

	a[i] = a[i - 1]

	a[i -1] = temp



for item in a:

	print(item, end =" ")