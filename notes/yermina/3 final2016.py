import math
n,m = [int(x) for x in input().split()]
nh = [int(x) for x in input().split()]
mh = [int(x) for x in input().split()]
min = 1110000
for i in range(0,n):
	for j in range(0,m):
		if min > math.fabs(nh[i]-mh[j]):
			min = math.fabs(nh[i]-mh[j])
			min_i=i
			min_j=j
print(min_i,min_j)