students = []
a = []
with open("a.txt", "r") as file:
    lines = file.readlines()
    students = lines[0].replace("\n", "").split("\t")[1:]       #Код, открывающий файл a.txt
    for line in lines[1:]:                                      # с подписками в инстаграме
        values = line.replace("\n", "").split("\t")[1:]
        row = []
        for v in values:
            row.append(int(v))
        a.append(row)
n = len(students)
for i in range(0, n):
    for j in range(0, n):
        #a[i][j] == 1 j-th is following i-th
        if a[i][j] == 1 and a[j][i] == 0:
            print("%s is not following %s" % (students[i], students[j]))
print("-----")
for i in range(0, n):
    name = students[i]
    ok = True
    for j in range(0, n):
        if a[i][j] != a[j][i]:
            ok = False
            break
    if ok:
        print("%s is follow backer" % students[i])
 
for i in range(0, n):
    for j in range(0, n):
        if a[j][i] == 1 and a[i][j] == 0:
            print("%s is not following back %s" % (students[j], students[i]))