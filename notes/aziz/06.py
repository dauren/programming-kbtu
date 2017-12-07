s = input()
n = ''
for i in range(len(s)):
	if i < len(s)-1 and s[i] == ' ' and s[i+1] == ' ':
		pass
	else:
		n = n + s[i]
print (n)			#Заменить несколько идущих подряд пробелов на один