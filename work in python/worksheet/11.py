n = int(input("Enter the order of matrix: "))
a = []
for i in range(n):
    row = []
    for j in range(n):
        colm = int(input("Enter a element[{}][{}]; ".format(i, j)))
        row.append(colm)
    a.append(row)

m = int(input("Enter the same order as above: "))
b = []
for i in range(m):
    row = []
    for j in range(m):
        colm = int(input("Enter a element[{}][{}]; ".format(i, j)))
        row.append(colm)
    b.append(row)





ab = [[0]*n for _ in range(n) ]

for i in range(len(a)):
    for j in range(len(a[0])):
        for k in range(len(a[0])):
            ab[i][j] += a[i][k] * b[k][j]

print(ab)


