n = int (input())
a = []
for i in range (n):
	row = [int (x) for x in input().split()]
	a.append (row)
ok = True
for i in range (n):
	for j in range (n):
		if a[i][j] != a[j][i]:
			ok = False
			break
if ok:
	print ("yes")
else:
	print ("no")     #Код проверяет, является ли массив симметричным относительно главной диагонали