def pow(a,n):
	if n == 1:
		return a
	else:
		if n % 2 == 0:
			x = pow(a, n //2)
			return x * x
		else:
			x = pow(a,n-1)
			return x*a
print (pow(2,12))		# Функция возведения в степень