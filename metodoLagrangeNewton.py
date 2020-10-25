from sympy import Symbol
import sympy as sym
import math


def escolherPontos(x, y, grau):  # Solicita ao usuário remover alguns pontos para prosseguir com o calculo
    print('\n Escolha pontos que estejam próximos ao valor que deseja interpolar e que o valor esteja entre esses pontos!')
    print('\n Pontos informados:\n')
    while len(x) > grau:
        for i in range(len(x)):
            print(f'P{i + 1}=({x[i]}, {y[i]})')

        indice = int(input('\nInforme o numero de um ponto que NÃO deseja usar: ')) - 1
        x = [i for i in x if x.index(i) != indice]
        y = [i for i in y if y.index(i) != indice]

    print("\n Pontos restantes para o calculo: ")
    for i in range(len(x)):
        print(f'P{i + 1}=({x[i]}, {y[i]})')

    return x, y


def criaMatrizD(x, y, ordem):  # Cria matriz com valores de diferencas divididas para cada ordem (para auxiliar no calculo)
    matriz = [0 for i in range(len(x))]

    tam = len(x)
    for i in range(len(x)):
        matriz[i] = [0 for j in range(tam)]
        matriz[i][0] = y[i]
        tam -= 1

    linhas = len(x) - 1
    j = 1
    xi = 0
    for i in range(ordem):
        if linhas > -1:
            for k in range(linhas):
                matriz[k][j] = (matriz[k + 1][j - 1] - matriz[k][j - 1]) / (x[xi + 1] - x[k])
                xi += 1
            xi = j
            j += 1
            linhas -= 1

    return matriz

def procuraMaiorOrdem(matriz, grau, tamX):
    maior = matriz[0][grau]

    for i in range(tamX - grau):
        if matriz[i][grau] > maior:
            maior = matriz[i][grau]
            
    return maior


def calculaErro(X, Y, x, val, grau):  # Calcula erro limitante usando os tres pontos mais proximos do ponto informado
    erro = 1
    pontos = x

    matriz = criaMatrizD(X, Y, grau)
    maior = procuraMaiorOrdem(matriz, grau, len(X))

    for i in range(len(pontos)):
        erro *= math.fabs(val - pontos[i])
    erro *= math.fabs(maior)

    print(f'O erro limitante para o valor {val} é: {erro}')


def montaPolinomioLagrange(x, y):
    var = Symbol('x')  # Simbolo para montar o polinomio interpolador
    polinomio = 0  # Variavel usada para montar o polinomio interpolador
    pol = []  # Vetor para armazenar em cada iteração o valor atualizado do polinomio

    for i in range(len(x)):
        L = 1  # L usado para montar o polinomio de interpolação
        for j in range(len(x)):
            if i != j:
                L *= (var - x[j]) / (x[i] - x[j])
        pol.append(sym.expand(L))
        polinomio += y[i] * pol[i]

    print('\n ========================== POLINÔMIO INTERPOLADOR ==========================================')
    print(f'\nO polinomio interpolador dos pontos informados é: {polinomio}')
    print('\n ============================================================================================')


def interpolaValorLagrange(x, y, val):
    p = 0  # Variavel usada para calcular

    for i in range(len(x)):
        L = 1  # L usado no calculo do valor interpolado
        for j in range(len(x)):
            if i != j:
                L *= (val - x[j]) / (x[i] - x[j])
        p += y[i] * L

    print('\n================================================')
    print(f'\nO valor interpolado de {val} é {p}')


def metodoLagrange(X, Y, x, y):
    resp = int(input('Deseja interpolar algum valor? (1 para Sim) (0 para Não) '))

    if resp == 1:
        montaPolinomioLagrange(x, y)
        val = float(input('\nInforme o valor que deseja interpolar: '))
        interpolaValorLagrange(x, y, val)
        calculaErro(X, Y, x, val, len(x))
    else:
        montaPolinomioLagrange(x, y)


def atualizaD(x, d, ordem):
    if ordem == 0:
        return d
    else:
        auxD = d
        x0 = 0  # Variavel para usar nos denominadores
        xn = ordem  # Variavel para usar nos denominadores
        aux = []
        for i in range(len(d) - ordem):
            aux.append((auxD[i + ordem] - auxD[i + ordem - 1]) / (x[xn] - x[x0]))
            xn += 1
            x0 += 1

        i = 0
        for j in range(ordem, len(d)):
            d[j] = aux[i]
            i += 1
        return d


def montaPolinomioNewton(x, d):
    polinomio = 0  # Variavel usada para montar o polinomio interpolador
    var = Symbol('x')  # Simbolo para montar o polinomio interpolador
    pol = []  # Vetor para armazenar em cada iteração o valor atualizado do polinomio
    L = 1
    for i in range(1, len(d) - 1):
        if len(pol) == 0:
            pol.append(var - x[0])
        L *= pol[i - 1] * (var - x[i])
        pol.append(sym.expand(L))

    for i in range(len(pol)):
        polinomio += d[i + 1] * pol[i]
    polinomio += d[0]

    print('\n ========================== POLINÔMIO INTERPOLADOR ==========================================')
    print(f'\nO polinomio interpolador dos pontos informados é: {polinomio}')
    print('\n ============================================================================================')


def interpolaValorNewton(x, d, val):
    polinomio = 0  # Variavel usada para montar o polinomio interpolador
    pol = []  # Vetor para armazenar em cada iteração o valor atualizado do polinomio
    L = 1
    for i in range(1, len(d) - 1):
        if len(pol) == 0:
            pol.append(val - x[0])
        L *= pol[i - 1] * (val - x[i])
        pol.append(sym.expand(L))

    for i in range(len(pol)):
        polinomio += d[i + 1] * pol[i]
    polinomio += d[0]

    print('\n================================================')
    print(f'\nO valor interpolado de {val} é {polinomio}')


def metodoNewton(X, Y, x, y):
    d = y
    for o in range(len(x)):
        d = atualizaD(x, d, o)

    resp = int(input('\n Deseja interpolar algum valor? (1 para Sim) (0 para Não) '))

    if resp == 1:
        montaPolinomioNewton(x, d)
        print()
        val = float(input('\n Informe o valor que deseja interpolar: '))
        print()
        interpolaValorNewton(x, d, val)
        calculaErro(X, Y, x, val, len(x))
    else:
        montaPolinomioNewton(x, d)


def main():
    x = [0.2, 0.34, 0.4, 0.52, 0.6, 0.72]  # Vetor para armazenar os x's dos pontos tabelados
    y = [0.16, 0.22, 0.27, 0.29, 0.32, 0.37]  # Vetor para armazenar os y's respectivos dos pontos tabelados

    grau = int(input('\n Informe o grau do polinômio: ')) + 1
    if grau < len(x):
        auxX, auxY = escolherPontos(x, y, grau)
        resp = int(input('\n Deseja interpolar usando o Metodo de Lagrange (1) ou pelo Metodo de Newton (2) ? '))
        if resp == 1:
            metodoLagrange(x, y, auxX, auxY)
        else:
            metodoNewton(x, y, auxX, auxY)
    else:
        if grau > len(x) - 1:
            print('\n\n Impossível calcular com esse grau!')
        else:
            auxX = x
            auxY = y
            resp = int(input('\n Deseja interpolar usando o Metodo de Lagrange (1) ou pelo Metodo de Newton (2) ? '))
            if resp == 1:
                metodoLagrange(x, y, auxX, auxY)
            else:
                metodoNewton(x, y, auxX, auxY)


if __name__ == '__main__':
    main()
