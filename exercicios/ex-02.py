'''
    02 - Escreva um algoritmo que leia dois números que deverão ser colocados, respectivamente nas variáveis vA e vB. O algoritmo deve, então, trocar os valores de vA por vB e vice-versa. Mostrar o conteúdo destas variáveis conforme a ordem de digitação antes da troca e após a troca.
'''

vA = input("Digite um valor para vA: ")
vB = input("Digite um valor para vB: ")

aux = vA

vA = vB
vB = aux

print(f"\nAgora vA tem: {vA}")
print(f"Agora vB tem: {vB}")