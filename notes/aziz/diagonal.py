n = int (input())
a = []
for i in range (n):
	a.append ([0] * n)
for i in range (n):
	for j in range (n):
		if i + j == n - 1:
			a[i][j] = 1   #Заполнение побочной диагонали единицами
		if i + j > n - 1:
			a[i][j] = 2   #Заполнение всего, что находится ниже побочной диагонали двойками
for i in  range (n):
	for j in range (n):
		print (a[i][j], end = ' ')
	print ()