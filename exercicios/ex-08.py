'''
    08 - Faça um algoritmo que leia valores para as variáveis a, b e c e mostre o resultado da seguinte
    expressão: ( a - b ) * c
'''

letters = ["a", "b", "c"]

result = 0

for char in range(len(letters)):
    value = float(input(f"Digite um vlor para {letters[char]}: "))
