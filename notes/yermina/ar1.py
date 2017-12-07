n = int(input())

s = input()

a = [int(x) for x in s.split()]

for i in range(0, len(a)): # range(x, y) start from x to y (non incl)

	if a[i] % 2 == 0:

		print(a[i], end=" ")