'''
    05 - Ler um conjunto de 5 dados numéricos e imprimir sua soma e sua média.
'''

sum = 0
average = 0

for step in range(1, 6, 1):
    value = float(input(f"Digite o {step}º valor: "))

    sum += value
    average = sum / (step + 1)

print(f"A soma dos valores é: {sum}")
print(f"A média dos valores é: {average}")