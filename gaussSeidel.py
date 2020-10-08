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

    for i in range(n):
        for j in range(n):
            if i == j:
                C[i][j] = b[j] / A[i][j]
            else:
                C[i][j] = -1 * A[i][j] / A[i][i]
    return C


def gaussJacobi(C, X, n): # Função que calcula o vetor aproximado da solução

    for i in range(n):
        soma = 0
        for k in range(n):
            if k != i:
                soma += C[i][k] * X[k]
        X[i] = soma + C[i][i]

    return X


def erro(X, aux, n): # Função que calcula o erro relativo do problema, servindo como teste de parada

    maiorx = -10000
    maioraux = -10000

    for i in range(n):
        if math.fabs(X[i]) > maiorx:
            maiorx = math.fabs(X[i])
        if math.fabs(aux[i]) > maioraux:
            maioraux = math.fabs(aux[i])

    dif = math.fabs(maioraux - maiorx)

    if maioraux == 0:
        return 1.0
    else:
        return dif / maioraux


def convergencia(A, n):
    betas = []

    soma=0
    for i in range(1, n):
        soma += A[0][i]
    betas.append(soma/A[0][0])

    for i in range(n):
        soma = 0
        for j in range(1, i-1):
            soma += math.fabs(A[i][j]) * betas[j]
        for k in range(i+1, n):
            soma += math.fabs(A[i][k])
        betas.append(soma/A[i][i])

    maior = -10000
    for i in range(len(betas)):
        if betas[i] > maior:
            maior = betas[i]

    return maior

def main():
    stop = 0.005
    d = 1.0

    n = int(input('Informe a ordem da Matriz: '))

    A = cria_matriz(n)
    b = cria_vetor(n)

    while True:
        A = read_a(A, n)

        if convergencia(A, n) >= 1:
            print('Não se pode ter certeza sobre a convergencia da matriz A!')
            print('Favor, tentar outra vez!')

        if not convergencia(A, n) >= 1:
            break

    b = read_b(b, n)
    ite = int(input('Informe o numero de iterações: '))

    C = matriz_coef(A, b, n)
    X = [0 for i in range(n)]
    aux = [0 for i in range(n)]

    while ((ite > 0) and (d > stop)):
        ite -= 1

        copia_vetor(aux, X, n)
        X = gaussJacobi(C, X, n)
        d = erro(X, aux, n)

    copia_vetor(X, aux, n)

    print("Solução aproximada: ")
    imprime_vetor(n, X)  # Imprimindo solução aproximada


if __name__ == '__main__':
    main()
