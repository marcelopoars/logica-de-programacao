'''
    08 - Faça um Programa que peça a idade e a altura de 5 pessoas,
    armazene cada informação no seu respectivo vetor.

    Imprima a idade e a altura na ordem inversa a ordem lida
'''
persons = []
ages = []
heights = []

for i in range(2):
    name = input(f"Digite o nome da {i+1}º pessoa: ").upper()

    persons.append(name)

    age = int(input(f"Digite a idade de {name}: "))
    height = float(input(f"Digite a altura de {name}: "))

    ages.append(age)
    heights.append(height)

    print(f"{30 * '*'}")

inverted_persons = persons[::-1]
inverted_ages = ages[::-1]
inverted_heights = heights[::-1]

print(inverted_persons)
print(inverted_ages)
print(inverted_heights)
