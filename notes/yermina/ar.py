n = int(input())

s = input()

a = [int(x) for x in s.split()]

ok = False

for i in range(1, len(a)): # range(x, y) start from x to y (non incl)

	if a[i] * a[i - 1] > 0:

		ok = True

		break

if ok:

	print("YES")

else:

	print("NO")