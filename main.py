s = input().split()
n = int(s[0])
m = int(s[1])
k = 1
mas = [[0] * m for _ in range(n)]
i0 = j0 = 0
im = jm = 1
mas[0][0] = 1


def diag(mas, k, id, jd):
    for j in range(jd + 1):
        mas[j][jd - j] = k
        k += 1
    return mas, k

def diag(mas, k, id, jd):
    for j in range(jd + 1):
        mas[j][jd - j] = k
        k += 1
    return mas, k
def diag2(mas, k, id, jd):
    for j in range(jd + 1):
        mas[j - id][jd - j] = k
        k += 1
    return mas, k


for q in range(m):
    mas, k = diag(mas, k, 0, q)

for q in range(1, n):
    mas, k = diag2(mas, k, q, m)

for i in range(n):
    for j in range(m):
        print(str(mas[i][j]).ljust(3), end=' ')
    print()
