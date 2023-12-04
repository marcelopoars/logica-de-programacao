'''
1) Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 
'''


def sumNumber(value1, value2, value3):
    return sum([value1, value2, value3])


title = "Este programa recebe três valores e retora a soma dos mesmo"

print(f"\n{title}\n{len(title) * '='}")

values = []

for index in range(3):
    value = int(input(f"Digite o {index + 1}º valor: "))
    values.append(value)

result = sumNumber(values[0], values[1], values[2])

print(f"\nA soma dos números digitados é: {result}")
