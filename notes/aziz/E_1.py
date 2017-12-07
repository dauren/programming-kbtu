s = input()
d1 = s.find ('f')
d2 = len(s) - s[::-1].find('f') - 1
if d2 != d1 and d1 != -1:
	print (d1, d2)
elif d1 != -1:
	print (d1)   #Ищет позиция первой и последней букв f в введённой строчке