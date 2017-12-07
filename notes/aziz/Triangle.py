a = float (input ())  # задача определяет, лежит ли данная точка в треугольнике,
a1 = float (input ()) # координаты которого даны
b = float (input ())
b1 = float (input ())
c = float (input ())
c1 = float (input ())
x = float (input ())
y = float (input ())
import math
maxx = max(a, b, c)
minx = min(a, b, c)
maxy = max(a1, b1, c1)
miny = min(a1, b1, c1)
sidea = math.sqrt((a - b) ** 2 + (a1 - b1) ** 2)
sideb = math.sqrt((b - c) ** 2 + (b1 - c1) ** 2)
sidec = math.sqrt((c - a) ** 2 + (c1 - a1) ** 2)
k1 = math.sqrt((x - a) ** 2 + (y - a1) ** 2)
k2 = math.sqrt((x - b) ** 2 + (y - b1) ** 2)
k3 = math.sqrt((x - c) ** 2 + (y - c1) ** 2)
p = (sidea + sideb + sidec) / 2
s = math.sqrt (p * (p - sidea) * (p - sideb) * (p - sidec)) #Формула Герона
p1 = (k1 + k2 + sidea) / 2
s1 = math.sqrt(p1 * (p1 - k1) * (p1 - k2) * (p1 - sidea)) #Формула Герона
p2 = (k1 + k3 + sidec) / 2
s2 = math.sqrt(p2 * (p2 - k1) * (p2 - k3) * (p2 - sidec))  #Формула Герона
p3 = (k2 + k3 + sideb) / 2
s3 = math.sqrt(p3 * (p3 - k2) * (p3 - sideb) * (p3- k3))  #Формула Герона
if abs(s - (s1 + s2 + s3)) <= 0.000000000001: #Учитывается погрешность в вычислении квадратного корня
	print ("The point is inside the triangle")
else: 
	print ("No, the point is outside the tiangle")



	
