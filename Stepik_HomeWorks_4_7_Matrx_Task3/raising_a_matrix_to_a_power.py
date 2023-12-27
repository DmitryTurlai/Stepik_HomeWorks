import copy

n = int(input())  # entering the matrix size from the keyboard

matrix1 = []

for _ in range(n):  # matrix input from keyboard
    row = list(map(int, input().split()))
    matrix1.append(row)

m = int(input())  # entering the value of the power to which you want to raise

matrix2 = copy.deepcopy(matrix1)  # creating a copy of the matrix

for step in range(m - 1):  # raising a matrix of size n to the power m
    result = [[0 for _ in range(n)] for _ in range(n)]  # create emty matrix
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    matrix1 = copy.deepcopy(result)  # saving the result of matrix multiplication

for i in range(n):  # print result matrix
    for j in range(n):
        print(str(matrix1[i][j]).ljust(1), end=' ')
    print()
