import math


def read_a(A, n): # Função para ler os elementos para preencher a Matriz A
    for i in range(0, n):
        for j in range(0, n):
            A[i][j] = float(input("Digite o valor de A[{}][{}]:".format(i + 1, j + 1)))
    return A


def read_b(b, n): # Função para ler os elementos para preencher o vetor b
    for i in range(0, n):
        b[i] = float(input("Digite o valor de b[{}]:".format(i + 1)))
    return b


def cria_matriz(n): # Cria matriz de ordem nXn
    matriz = [[0 for i in range(n)]for j in range(n)]
    return matriz


def cria_vetor(n): # Cria vetor de tamanho n
    vetor = [0 for j in range(n)]
    return vetor


def copia_vetor(v1, v2, n):  # Função que copia valores de v2 para v1 para aproximação da solução
    for i in range(0, n):
        v1[i] = v2[i]
    return v1


def imprime_matriz(n, matriz):
    for l in range(0, n):
        for c in range(0, n):
            print(f'[ {matriz[l][c]} ]', end='')
        print()


def imprime_vetor(n, vetor):
    for l in range(0, n):
        print('[ %.3f ]' % vetor[l])
    print()


def matriz_coef(A, b, n): # Função que gera a matriz C e vetor g de X = Cx + g
    C = [[0 for i in range(n)] for j in range(n)]
    g = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            if i == j:
                C[i][j] = b[j] / A[i][j]
            else:
                C[i][j] = -1 * A[i][j] / A[i][i]
        g[i] = b[i] / A[i][i]
    return C, g


def gaussJacobi(C, X, n): # Função que calcula o vetor aproximado da solução
    aux = [0 for i in range(n)]

    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(n):
                if k != i:
                    soma += C[i][k] * X[k]
            aux[i] = soma + C[i][i]

    return aux


def erro(X, aux, n): # Função que calcula o erro relativo do problema, servindo como teste de parada

    maiorx = -10000
    maioraux = -10000

    for i in range(n):
        if math.fabs(X[i]) > maiorx:
            maiorx = math.fabs(X[i])
        if math.fabs(aux[i]) > maioraux:
            maioraux = math.fabs(aux[i])

    dif = math.fabs(maioraux - maiorx)

    if maiorx == 0:
        return 1.0
    else:
        return dif / maioraux


def convergencia(A, n):
    conv = 0
    for i in range(n):
        soma=0
        for j in range(n):
            if i != j:
                soma+=A[i][j]
        if A[i][i] > soma:
            conv+=1

    return conv

def main():
    stop = 0.05
    d = 1.0

    n = int(input('Informe a ordem da Matriz: '))

    b = cria_vetor(n)
    A = cria_matriz(n)

    while True:
        A = read_a(A, n)
        b = read_b(b, n)

        if convergencia(A, n) != n:
            print('Não se pode ter certeza sobre a convergencia da matriz A!')
            print('Favor, tentar outra vez!')

        if not convergencia(A, n) != n:
            break

    #A = [[10, 2, 1], [1, 5, 1], [2, 3, 10]]
    #b = [7, -8, 6]

    # A = [[10, 3, -2], [2, 8, -1], [1, 1, 5]]
    # b = [57, 20, -4]

    ite = int(input('Informe o numero de iterações: '))

    C, g = matriz_coef(A, b, n)
    X = [0 for i in range(n)]
    aux = [0 for i in range(n)]

    copia_vetor(X, g, n)

    while ((ite > 0) and (d > stop)):
        ite -= 1

        aux = gaussJacobi(C, X, n)
        d = erro(X, aux, n)
        copia_vetor(X, aux, n)

    print("Solução aproximada: ")
    imprime_vetor(n, X)  # Imprimindo solução aproximada


if __name__ == '__main__':
    main()
