def isDigit(c):
	if ord(c) >= 48 and ord(c) <= 57:
		return True
	return False
s = '001'
def isInteger(s):
	if len(s) == 0:
		return False
	if s[0] == '0':
		return False
	ok = True
	for c in s:
		if not isDigit(c):
			return False
	return True
def isFloat(s):
	if s.count('.') > 1:
		return False
	elif s.count('.') == 1:
		point = s.find('.')
		if point == 0 or point == len(s) - 1:
			return False
		s = s.replace('.', '')
		return isInteger(s)
	else:
		return isInteger(s)
print (isFloat(s))