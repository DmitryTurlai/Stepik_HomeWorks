s = input().split()
n = int(s[0])
m = int(s[1])
mas = [[0] * m for _ in range(n)]
number = 1
def round(mas, n, m, number, a = 0, b = 0):
    i = a
    for j in range(b, m - b):
        if n * m < number:
            return mas, number
        mas[i][j] = number
        number += 1

    for i in range(a + 1, n - a):
        if n * m < number:
            return mas, number
        mas[i][j] = number
        number += 1

    for j in range(m - 2 - a, b - 1, -1):
        if n * m < number:
            return mas, number
        mas[i][j] = number
        number += 1

    for i in range(n - 2 - a, a, -1):
        if n * m < number:
            return mas, number
        mas[i][j] = number
        number += 1

    return mas, number
a = b = 0
while True:
    if n * m <= number - 1:
        break
    mas, number = round(mas, n, m, number, a, b)
    a += 1
    b += 1

    if a >= n or b >= m:
        break

for i in range(n):
    for j in range(m):
        print(str(mas[i][j]).ljust(3), end=' ')
    print()