import math
import numpy as np


def read_a(A, n):
    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = float(input("Digite o valor de A[{}][{}]:".format(i + 1, j + 1)))
    return A


def read_b(b, n):
    for i in range(0, n):
        for j in range(0, 1):
            b[i] = float(input("Digite o valor de b[{}]:".format(i + 1)))
    return b


def cria_matriz_a(n):
    l = c = n
    matriz = [0] * l
    for i in range(0, l):
        matriz[i] = [0] * c
    return matriz


def cria_matriz_b(n):
    matriz = [0] * n
    for i in range(0, 1):
        matriz[i] = [0] * 1
    return matriz


def fator_lu(A, n):
    U = np.copy(A)

    L = [0] * n
    for i in range(0, n):
        L[i] = [0] * n

    for j in range(n - 1):
        for i in range(j + 1, n):
            L[i][j] = U[i][j] / U[j][j]
            for k in range(j + 1, n):
                U[i][k] = U[i][k] - L[i][j] * U[j][k]
            U[i][j] = 0

    for i in range(n):
        for j in range(n):
            if i==j:
                L[i][j] = 1

    return L, U

def vet_y(L, n, b):
    y = [0 for f in range(0, n)]
    y[0] = b[0] / L[0][0]

    for i in range(1, n):
        soma = 0
        for j in range(0, n):
            soma = soma + L[i][j] * y[j]
        y[i] = (b[i] - soma) / L[i][i]
    return y

def vet_x(U, n, y):
    x = [0 for f in range(0, n)]
    n = n - 1
    x[n] = y[n] / U[n][n]

    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i, n + 1):
            soma = soma + U[i][j] * x[j]
        x[i] = (y[i] - soma) / U[i][i]
    return x

def main():
    o = int(input("Digite a ordem da matriz: "))
    print()

    A = cria_matriz_a(o)
    b = cria_matriz_a(o)

    print("Criando matriz A: ")
    print()
    A = read_a(A, o)

    print()
    print("Criando matriz dos termos independentes (b): ")
    print()
    b = read_b(b, o)

    print()
    print("Matriz informada: ")
    for l in range(0, o):
        for c in range(0, o):
            print(f'[ {A[l][c]} ]', end='')
        print(f' = [ {b[l]} ]')

    L, U = fator_lu(A, o)
    y = vet_y(L, o, b)
    x = vet_x(U, o, y)

    print()
    print('Solução: ')
    for l in range(0, o):
        print(f'[ {x[l]} ]', end='')
    print()

if __name__ == '__main__':
    main()
