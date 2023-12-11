s = input().split()
n = int(s[0])
m = int(s[1])
mas = [[0] * m for _ in range(n)]



for i in range(n):
    for j in range(m):
        print(str(mas[i][j]).ljust(3), end=' ')
    print()
