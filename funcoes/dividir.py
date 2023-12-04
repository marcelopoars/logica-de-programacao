def multiplicacao(number1, number2):
    return round(number1 * number2, 2)


def dividir(number1, number2):
    return round(number1 / number2, 2)


print(f"\nESCOLHA A OPERAÇÃO:\n{32 * '='}")

operacao = input("1 - Multiplicação | 2 - Divisão: ")

number1 = float(input("Digite um número: "))
number2 = float(input("Digite outro número: "))

if operacao == '1':
    print(f"{number1} * {number2} = {multiplicacao(number1, number2)}")

if operacao == '2':
    print(f"{number1} / {number2} = {dividir(number1, number2)}")
