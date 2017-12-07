n = int (input())
save = n
inv = 0
while n > 0:
	x = n % 10
	inv = inv  * 10 + x
	n = n // 10
if inv == save:
	print ("YES")    #Проверяет, является ли число палиндромом
else:
	print ("NO")