d = int (input())	# Этот код считает количество дней относительно 11 октября 2017 года
m = int (input())	# Только при дате, отличающейся от 2017 на 100 и более лет существует погрешность
y = int (input())	# Считает лишние дни в 2100-ом и подобных годах
r = m
pr = 0
su = 0
ok = False
for i in range (r - 1):
	if y % 4 == 0:
		if y % 100 == 0:
			if y % 400 == 0:
				ok = True
			else:
				ok = False
		else:
			ok = True
	else:
		ok = False
	if i == 4 or i == 6 or i == 9 or i == 11:
		pr = 30
	elif i == 2:
		if ok:
			pr = 29
		else:
			pr = 28
	else:
		pr = 31
	su = su + pr
y = (y - 2017) * 365 + (abs(y-2018) // 4 )
c = y + su + d - 1
key = 284
if c == key:
	print ("TODAY") 
elif c > key:
	print ("FUTURE")
else:
	print ("PAST")
print (c, "date with respect to 1/01/2017") 