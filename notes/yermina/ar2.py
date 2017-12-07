n = int(input())

s = input()

a = [int(x) for x in s.split()]

r = 0

for i in range(0, len(a)): # range(x, y) start from x to y (non incl)

	if a[i] > 0:

		r = r + 1

print(r)