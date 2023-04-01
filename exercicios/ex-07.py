'''
    07 - Ler 3 números e imprimi-los em ordem crescente
'''

values = []

for step in range(1, 4, 1):
    value = int(input(f"Digite o {step}º valor: "))
    values.append(value)

values_sorted = sorted(values)

for number in values_sorted:
    print(number)
