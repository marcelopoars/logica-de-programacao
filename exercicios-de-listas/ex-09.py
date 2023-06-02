'''
    09 - Faça um Programa que leia um vetor A com 10 números inteiros, 
    calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = []

for number in numbers:
    square.append(number * number)

print(square)