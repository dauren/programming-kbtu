def hanoi(n):
	if n == 1:
		return 1
	return hanoi(n-1) + 1 + hanoi(n-1)
n = int(input())
print (hanoi(n))    #Минимальное количество ходов для решения Ханойской башни