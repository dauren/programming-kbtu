n = int(input())  #Перевод введённого двоичного числа в десятичное
d = 0
p = 1
while n > 0:
	x = n % 10
	d = d + p*x
	p = p * 2
	n = n // 10
print (d)