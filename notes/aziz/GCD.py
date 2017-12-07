a = int (input ())
b = int (input ())
mi = min (a,b)
ma = max (a,b)
while mi != 0:
	ma, mi = mi, ma % mi
print (ma) #Выводит наибольший общий делитель любых двух чисел