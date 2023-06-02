'''
    05 - Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
    Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. 
    Imprima os três vetores.
'''

number_list = []  # lista de números digitados
even_numbers = []  # pares
odd_numbers = []  # impares

while (True):
    number = int(input("Digite um número: "))

    number_list.append(number)

    if (number % 2 == 0):
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

    if (len(number_list) == 20):
        break

print(f"Números digitados: {number_list}")
print(f"Números pares: {even_numbers}")
print(f"Números ímpares: {odd_numbers}")
