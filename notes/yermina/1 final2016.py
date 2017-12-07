w = float(input())
h = int(input())
bmi = w / ((h/100)**2)
if bmi >= 19:
	w2 = 18.9*((h/100)**2)
x = w - w2
print(round(x))