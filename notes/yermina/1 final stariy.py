n,m = [int(x) for x in input().split()]
usd = n/150.55 
eur = usd/1.3075
x = eur//m
print(x)