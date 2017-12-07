ci = input()
k = int(input())
ori = ''
ci = ci.upper()
k = k%26
for c in ci:
	ori = ori + chr((ord(c) - ord('A') - k)%26 + ord('A'))
print (ori)			# Шифр Цезаря