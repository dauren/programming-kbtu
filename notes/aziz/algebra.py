save = int (input())
a = save
for z in range (1, save + 1):
  a = save
  b = z
  while b != 0:
    a, b = b, a % b
  if a == 1:
    print (z)			#Находит все взаимно простые с введённым числом числа,
    					# начиная с 1 и заканчивая нашим числом