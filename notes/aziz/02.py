def toUpper(c):
	if ord(c) >= 97 and ord(c) <= 122:
		x = ord(c) - 32
		return chr(x)			#Функция .upper, которую написали мы сами
	return c
c = input()
print (toUpper(c)) 