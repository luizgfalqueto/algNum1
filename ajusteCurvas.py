from sympy import Symbol
import matplotlib.pyplot as plt


def geraFuncao(a, b):
    func = 0
    var = Symbol('x')  # Simbolo para montar o polinomio interpolador

    return a + b * var


def calculaReta(a, b, x):
    Y = a + b * x

    return Y


def tabelaQuadradosMinimos(x, y):
    x2 = 0
    xy = 0
    xi = 0
    yi = 0
    for i in range(len(x)):
        x2 += x[i] ** 2
        xy += x[i] * y[i]
        xi += x[i]
        yi += y[i]

    b = ((xi * yi) - (len(x) * xy)) / (xi ** 2 - (len(x) * x2))
    a = (yi - (b * xi)) / len(x)

    return xi, yi, xy, x2, a, b


def calculaDesvio(x, y, a, b):
    D = 0
    for i in range(len(x)):
        D += (y[i] - (a + b * x[i])) ** 2

    return D


def calculaAjuste(x, y, a, b):
    num = 0
    den1 = 0
    den2 = 0
    for i in range(len(x)):
        num += (y[i] - a - b * x[i]) ** 2
        den1 += y[i] ** 2
        den2 += y[i]

    return 1 - num / (den1 - (1 / len(x)) * den2 ** 2)


def mostraGrafico(x, y, a, b, funcao, val):
    vetorXRetaAjuste = [61, 81]
    vetorYRetaAjuste = [calculaReta(a, b, 61), calculaReta(a, b, 81)]

    if val != 'null':
        pontoY = round(a + b * val, 2)
        plt.scatter(val, pontoY, color='yellow')
        plt.text(val, pontoY, f"P({val},{pontoY})", fontsize=8, horizontalalignment='right')

    plt.scatter(x[0], y[0], color='yellow')
    plt.scatter(x[1], y[1], color='yellow')
    plt.scatter(x[2], y[2], color='yellow')
    plt.scatter(x[3], y[3], color='yellow')
    plt.scatter(x[4], y[4], color='yellow')
    # plt.plot(x, y, marker='o', label='Curva real')
    plt.plot(vetorXRetaAjuste, vetorYRetaAjuste, label=f'f(x) = {funcao}')
    plt.title('Ajuste de Curvas')
    plt.xlabel('eixo X')
    plt.ylabel('eixo Y')
    plt.grid(True)
    plt.legend(loc=0)

    plt.show()


def main():
    # x = [0.3, 2.7, 4.5, 5.9, 7.8]
    # y = [1.8, 1.9, 3.1, 3.9, 3.3]

    x = [0.5, 1.2, 2.1, 3.5, 5.4]
    y = [5.1, 3.2, 2.8, 1.0, 0.4]

    xi, yi, xy, x2, a, b = tabelaQuadradosMinimos(x, y)

    funcao = geraFuncao(round(a, 4), round(b, 4))

    resp = float(input('Deseja avaliar um ponto da reta? (1 para SIM) ou (0 para NÃO): '))

    if resp == 1:
        val = float(input('Informe o valor que deseja calcular: '))
    else:
        val = 'null'

    mostraGrafico(x, y, a, b, funcao, val)

    a = 4.3271
    b = -0.7272

    D = calculaDesvio(x, y, a, b)

    r2 = calculaAjuste(x, y, a, b)

    print(f'a = {a}')
    print(f'b = {b}')
    print(f'\nCurva: {funcao}')
    print(f'Valor do desvio = {D}')
    print(f'Qualidade do ajuste = {r2}')


if __name__ == '__main__':
    main()
