s = input()
print (s[(len(s)+1)//2::] + s[:(len(s)+1)//2:])
print (s[len(s)//2 + len(s)%2:] + s[:len(s)//2 + len(s)%2])
print (s[len(s) - len(s)//2:] + s[:len(s) - len(s)//2])
#Несколько способов разрезать строку на две части и поменять их местами