s = input().split()
n = int(s[0])
m = int(s[1])
mas = [[0] * m for _ in range(n)]
nm = 0
mas[0][0] = 1

for q in range(n * m):
    for i in range(n):
        for j in range(m):
            if i+j == q:
                nm += 1
                mas[i][j] = nm


for i in range(n):
    for j in range(m):
        print(str(mas[i][j]).ljust(3), end=' ')
    print()
