'''
Marcelo Pereira da Silva
'''


def isValidNumber(value):
    if not value.isdigit():
        print("Valor inválido!")
        return False
    return True


def calc(number):
    print(f"\nTABUADA DO {number}")
    print("=" * 14)
    for i in range(10):
        print(f"{number} X {i+1} = {number * (i+1)}")


while True:
    value = input("\nDIgite um número: ")

    if value == '0':
        input("\nDigite ENTER para sair do programa")
        break

    if isValidNumber(value):
        number = int(value)

        calc(number)
