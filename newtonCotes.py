def geraX(a, b, m):
    xi = []
    xi.append(a)
    h = (b - a) / m

    for j in range(1, m + 1):
        xi.append(xi[j - 1] + h)

    return xi


def geraY(xi, coefs, grau):
    yi = []
    for i in range(len(xi)):
        yi.append(funcao(grau, coefs, xi[i]))

    return yi


def funcao(grau, coefs, val):
    pol = 0
    exp = grau
    for i in range(len(coefs)):
        pol += coefs[i] * pow(val, exp)
        exp -= 1
    return pol


def trapezios_repetidos(coefs, grau, a, b, m):
    h = (b - a) / m
    xi = geraX(a, b, m)
    yi = geraY(xi, coefs, grau)

    soma = 0
    for i in range(m + 1):
        if i != 0 and i != m:
            soma += 2 * yi[i]
        else:
            soma += yi[i]

    Itr = h / 2 * soma

    return Itr


def simpson_1_3(coefs, grau, a, b, m):
    h = (b - a) / m
    xi = geraX(a, b, m)
    yi = geraY(xi, coefs, grau)

    soma = 0
    for i in range(m + 1):
        if i != 0 or i != m:
            if i % 2 == 0:
                soma += 2 * yi[i]
            else:
                soma += 4 * yi[i]
        else:
            soma += yi[i]

    I2r = h / 3 * soma
    return I2r


def simpson_3_8(coefs, grau, a, b, m):
    h = (b - a) / m
    xi = geraX(a, b, m)
    yi = geraY(xi, coefs, grau)

    soma = 0
    for i in range(m + 1):
        if i != 0 or i != m:
            if i % 3 == 0:
                soma += 2 * yi[i]
            else:
                soma += 3 * yi[i]
        else:
            soma += yi[i]

    I3r = (3 * h) / 8 * soma
    return I3r


def main():
    grau = int(input('Informe o grau do polinômio\n Resposta: '))

    coefs = []
    for i in range(grau + 1):
        coefs.append(float(input(f'Informe o coeficente de x^{grau - i} -> ')))

    resp = 1
    while (resp != 0):
        resp = int(
            input('\nDeseja resolver por qual método?\n 1 - Trapézios Repetidos\n 2 - 1/3 Simpson repetido\n'
                  ' 3 - 3/8 Simpson repetido\n 0 - Sair\n Resposta: '))

        if resp == 1:
            print('-------------------------------------------------------------------------------')
            print('------------- Calculando pelo método dos Trapézios Repetidos ------------------')
            print('-------------------------------------------------------------------------------')
            print('Entrada de dados:\n')

            a = float(input('Informe o início do intervalo -> '))
            b = float(input('Informe o final do intervalo -> '))
            m = int(input('Informe o numero de subdivisões do intervalo -> '))

            I = trapezios_repetidos(coefs, grau, a, b, m)
            print(
                f'\n A area da região a baixo da curva da função e dentro do intervalo informado é aprox. {round(I, 5)}')

        if resp == 2:
            print('----------------------------------------------------------------------------')
            print('------------ Calculando pelo método do 1/3 de Simpson ----------------------')
            print('----------------------------------------------------------------------------')
            print('Entrada de dados:\n')

            a = float(input('Informe o início do intervalo -> '))
            b = float(input('Informe o final do intervalo -> '))
            m = int(input('Informe o numero (multiplo de 2) de subdivisões do intervalo -> '))

            if m % 2 != 0:
                while m % 2 != 0:
                    m = int(input('Informe o numero (multiplo de 2) de subdivisões do intervalo -> '))

            I2r = simpson_1_3(coefs, grau, a, b, m)
            print(
                f'\n A area da região a baixo da curva da função e dentro do intervalo informado é aprox. {round(I2r, 5)}')

        if resp == 3:
            print('-----------------------------------------------------------------------------')
            print('------------ Calculando pelo método dos 3/8 de Simpson ----------------------')
            print('-----------------------------------------------------------------------------')
            print('Entrada de dados:\n')

            a = float(input('Informe o início do intervalo -> '))
            b = float(input('Informe o final do intervalo -> '))
            m = int(input('Informe o numero (multiplo de 3) de subdivisões do intervalo -> '))

            if m % 3 != 0:
                while m % 3 != 0:
                    m = int(input('Informe o numero (multiplo de 3) de subdivisões do intervalo -> '))

            I3r = simpson_3_8(coefs, grau, a, b, m)
            print(
                f'\n A area da região a baixo da curva da função e dentro do intervalo informado é aprox. {round(I3r, 5)}')

        print('\n ------------------------------------------------------------------------------------')
        print(' ------------------------------------------------------------------------------------')
        sair = int(input('\nDeseja realizar outra operação? \n 1 - SIM \n 2 - NÃO \n Resposta -> '))
        if sair == 1:
            resp = 4

            opcao = int(input('\nDeseja alterar o polinomio? \n 1 - SIM \n 2 - NÃO \n Resposta -> '))
            if opcao == 1:
                grau = int(input('\nInforme o grau do polinômio\n Resposta: '))

                print()
                coefs = []
                for i in range(grau + 1):
                    coefs.append(float(input(f'Informe o coeficente de x^{grau - i} -> ')))
        else:
            resp = 0
            print('-----------------------------------------------------------------')
            print('----------------------- Programa encerrado ----------------------')
            print('-----------------------------------------------------------------')


if __name__ == '__main__':
    main()
