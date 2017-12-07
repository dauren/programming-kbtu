a = 1
def check(l, r):    #Бинарный поиск. Код ищет число а среди первых ста чисел
	if l >= r:
		return l
	m = (l+r)//2
	if a > m:
		return check(m+1,r)
	else:
		return check(l,m)
print (check(1,100)) 