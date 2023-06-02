'''
    06 - Fazer um algoritmo para ler dois números e mostrar o maior deles
'''

number1 = input("Digite o primeiro número: ")
number2 = input("Digite o segundo número: ")

bigger = number1 if number1 > number2 else number2 

print(f"O maior número digitado é: {bigger}")