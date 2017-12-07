n = input()
n=n.split()
n=''.join(c+' ' for c in n)
print(n[:len(n)-1])
