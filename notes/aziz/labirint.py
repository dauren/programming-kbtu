n = int (input())
a = []
for x in range (n):
	s = input()
	a.append(list(s))
x, y = [int(x) for x in input().split()]
k = 0
def flow(i,j):
	global k
	a[i][j] = '@'
	k = k + 1
	if a[i - 1][j] == '.':
		flow(i - 1, j)
	if a[i + 1][j] == '.':
		flow(i + 1, j)
	if a[i][j - 1] == '.':
		flow(i, j - 1)
	if a[i][j + 1] == '.':
		flow(i, j + 1)
flow(x-1, y-1)          #Решение задачи с площадью комнаты
print (k)