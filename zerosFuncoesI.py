def secante(a, b, epsilon, grau, coefs, iterMax):
    Fa = funcao(grau, coefs, a)
    Fb = funcao(grau, coefs, b)
    if abs(Fa) < abs(Fb):
        t = a
        a = b
        b = t
        t = Fa
        Fa = Fb
        Fb = t
    iter = 0
    x = b
    Fx = Fb
    while iter < iterMax:
        iter += 1
        deltaX = -Fx / (Fb - Fa) * (b - a)
        x += deltaX
        Fx = funcao(grau, coefs, x)
        print(
            f'Iterações: {iter} - a: {round(a, 5)} - b: {round(b, 5)} - x: {round(x, 5)} - Fx: {round(Fx, 5)} - deltaX: {round(deltaX, 5)}')
        if abs(deltaX) < epsilon and abs(Fx) < epsilon:
            break
        a = b
        Fa = Fb
        b = x
        Fb = Fx

    raiz = x
    if abs(deltaX) < epsilon and abs(Fx) < epsilon:
        erro = 0
    else:
        erro = 1

    return raiz, iter, erro


def Dfuncao(grau, coefs, val):
    deriv = []
    coef = grau
    for i in range(len(coefs) - 1):
        deriv.append(coefs[i] * coef)
        coef -= 1

    exp = grau - 1
    pol = 0
    for i in range(len(deriv)):
        pol += deriv[i] * pow(val, exp)
        exp -= 1

    return pol


def newton(x0, epsilon, iterMax, grau, coefs):
    Fx = funcao(grau, coefs, x0)
    Dfx = Dfuncao(grau, coefs, x0)
    x = x0
    iter = 0

    while iter < iterMax:
        DeltaX = -Fx / Dfx
        x = x + DeltaX
        Fx = funcao(grau, coefs, x)
        Dfx = Dfuncao(grau, coefs, x)
        iter += 1
        print(f'Iterações: {iter} - x: {round(x, 5)} - Fx: {round(Fx, 5)} - DeltaX: {round(DeltaX, 5)}')
        if (abs(DeltaX) < epsilon and abs(Fx) < epsilon) or abs(Dfx) == 0:
            break

    raiz = x
    if abs(Fx) < epsilon:
        erro = 0
    else:
        erro = 1

    return raiz, iter, erro


def bissecao(a, b, epsilon, grau, coefs, iterMax):
    Fa = funcao(grau, coefs, a)
    Fb = funcao(grau, coefs, b)

    if Fa * Fb > 0:
        print('Função não muda de sinal nos extremos do intervalo dado!')
    else:
        deltaX = abs(b - a) / 2
        iter = 0
        while iter < iterMax:
            iter += 1
            x = (a + b) / 2
            Fx = funcao(grau, coefs, x)
            print(
                f'Iterações: {iter} - a: {round(a, 5)} - b: {round(b, 5)} - x: {round(x, 5)} - Fx: {round(Fx, 5)} - deltaX: {round(deltaX, 5)}')
            if (deltaX < epsilon and abs(Fx) < epsilon) or iter >= iterMax:
                break

            if (Fa * Fx) > 0:
                a = x
                Fa = Fx
            else:
                b = x

            deltaX /= 2

        raiz = x
        if (deltaX < epsilon) and (abs(Fx) < epsilon):
            erro = 0
        else:
            erro = 1
    return raiz, iter, erro


def trocaSinal(z, grau,
               coefs):  # Implementado por conta do exercicio da lista 02, nao esta sendo usado nesse arquivo, porem pode ser adicionado
    if z == 0:
        a = -0.05
        b = 0.05
    else:
        a = 0.95 * z
        b = 1.05 * z

    iter = 0
    Aureo = 2 / ((5 ** 0.5) - 1)
    Fa = funcao(grau, coefs, a)
    Fb = funcao(grau, coefs, b)
    print(
        f'Iterações: {iter} - a: {round(a, 5)} - b: {round(b, 5)} - Fa: {round(Fa, 5)} - Fb: {round(Fb, 5)}')

    while iter < 20:
        if Fa * Fb <= 0:
            break
        iter += 1
        if abs(Fa) < abs(Fb):
            a -= Aureo * (b - a)
            Fa = funcao(grau, coefs, a)
        else:
            b -= Aureo * (b - a)
            Fb = funcao(grau, coefs, b)
        print(
            f'Iterações: {iter} - a: {round(a, 5)} - b: {round(b, 5)} - Fa: {round(Fa, 5)} - Fb: {round(Fb, 5)}')

    return a, b


def funcao(grau, coefs, val):
    pol = 0
    exp = grau
    for i in range(len(coefs)):
        pol += coefs[i] * pow(val, exp)
        exp -= 1
    return pol


def main():
    grau = int(input('Informe o grau do polinômio\n'))

    coefs = []
    for i in range(grau + 1):
        coefs.append(float(input(f'Informe o coeficente de grau {grau - i}\n')))

    resp = 1
    while (resp != 0):
        resp = int(
            input('Deseja resolver por qual método?\n 1 por Bissecção\n 2 por Newton\n 3 por Secante\n 0 para Sair\n'))

        if resp == 1:
            print('-------------------------------------------------------------------------------')
            print('----------------------- Calculando pelo método da Bissecção -------------------')
            print('-------------------------------------------------------------------------------')
            iterMax = int(input('Informe o número máximo de iterações:\n'))
            epsilon = float(input('Informe o epsilon:\n'))
            a = float(input('Informe o menor valor do intervalo:\n'))
            b = float(input('Informe o maior valor do intervalo:\n'))
            raiz, iter, erro = bissecao(a, b, epsilon, grau, coefs, iterMax)

            csi = u"\u03be"
            print(f'Resultado: \n    {csi} = {round(raiz, 4)}\n    Iterações = {iter}\n    Erro = {erro}\n\n')

        if resp == 2:
            print('----------------------------------------------------------------------------')
            print('----------------------- Calculando pelo método de Newton -------------------')
            print('----------------------------------------------------------------------------')
            iterMax = int(input('Informe o número máximo de iterações:\n'))
            epsilon = float(input('Informe o epsilon:\n'))
            x0 = float(input('Informe o um valor inicial:\n'))
            raiz, iter, erro = newton(x0, epsilon, iterMax, grau, coefs)

            csi = u"\u03be"
            print(f'Resultado: \n    {csi} = {round(raiz, 4)}\n    Iterações = {iter}\n    Erro = {erro}\n\n')

        if resp == 3:
            print('-----------------------------------------------------------------------------')
            print('----------------------- Calculando pelo método da Secante -------------------')
            print('-----------------------------------------------------------------------------')
            iterMax = int(input('Informe o número máximo de iterações:\n'))
            epsilon = float(input('Informe o epsilon:\n'))
            a = float(input('Informe o menor valor do intervalo:\n'))
            b = float(input('Informe o maior valor do intervalo:\n'))
            raiz, iter, erro = secante(a, b, epsilon, grau, coefs, iterMax)

            csi = u"\u03be"
            print(f'Resultado: \n    {csi} = {round(raiz, 4)}\n    Iterações = {iter}\n    Erro = {erro}\n\n')

        if resp == 0:
            print('-----------------------------------------------------------------')
            print('----------------------- Encerrando o Programa -------------------')
            print('-----------------------------------------------------------------')


if __name__ == '__main__':
    main()