'''
    07 - Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, 
    a multiplicação e os números.
'''

numbers = [1, 2, 3, 4, 5]

sum = 0
product = 0

for number in numbers:
    sum += number
    if product == 0:
        product += number
    else:
        product *= number

print(f"A soma dos números é: {sum}")
print(f"O produto dos números é: {product}")
print(f"Os números são: {numbers}")
