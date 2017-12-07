n = int(input())
f = 80
sch =  850
st = 2250
pen = 1500
p = ((n*100)/80) - 100
s1 = sch * (1 + p / 100)
st1 = st * (1 + p / 100)
pen1 = pen * (1 + p / 100)
print(int(s1), int(st1), int(pen1))
