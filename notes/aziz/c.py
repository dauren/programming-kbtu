n, m = [int (x) for x in input().split()]  #Задача про спортсменов с informatics
a = []
for i in range (n):
	row = [int (x) for x in input().split()]
	a.append (row)  		
s = 0
r = []
for i in range (n):
	s = 0
	for j in range (m):
		s = s + a[i][j]
	r.append (s)			#Код ищет сумму каждой строки
maxi = r[0]
key = 0
for i in range (n):
	if maxi < r[i]:
		maxi = r[i]
		key = i
print (maxi)             #Выводит максимальную сумму и позицию
print (key)