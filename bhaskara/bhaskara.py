def bhaskara(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta >= 0:
        x1 = (-b + delta ** (1/2)) / (2 * a)
        x2 = (-b - delta ** (1/2)) / (2 * a)
        print("Valor de x1: {0}".format(x1))
        print("Valor de x2: {0}".format(x2))
    else:
        print("A equação não possui soluções reais.")


if __name__ == '__main__':
    while True:
        print("Calculando uma equação de segundo grau:\n")
        a = float(input("Digite um valor para a: "))
        b = float(input("Digite um valor para b: "))
        c = float(input("Digite um valor para c: "))

        bhaskara(a, b, c)

        continua = input("\nDeseja continuar? Digite 'q' para sair ou pressione enter para novo cálculo: ")
        if continua.lower() == 'q':
            break
