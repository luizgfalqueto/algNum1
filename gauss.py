def metodogauss(A, n, b):
    for k in range(n - 1):
        for i in range(k + 1, n):
            m = ((-1) * A[i][k]) / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] + m * A[k][j]
            b[i] = b[i] + m * b[k]

    return A, b


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


def sub_ret(A, n, b):
    x = [0 for f in range(0, n)]
    n = n - 1
    x[n] = b[n] / A[n][n]

    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i, n + 1):
            soma = soma + A[i][j] * x[j]
        x[i] = (b[i] - soma) / A[i][i]
    return x


def gauss():
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

    A, b = metodogauss(A, o, b)

    print()
    print('Matriz triangularizada: ')
    for l in range(0, o):
        for c in range(0, o):
            print(f'[ {A[l][c]} ]', end='')
        print(f' = [ {b[l]} ]')

    x = sub_ret(A, o, b)
    print()
    print('Solução: ')
    for l in range(0, len(x)):
        print(f'[ {x[l]} ]', end='')
        print()


if __name__ == '__main__':
    gauss()
