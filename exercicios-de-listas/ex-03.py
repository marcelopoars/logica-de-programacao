'''
    03 - Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
'''

grades = [7, 8.5, 9, 7.9]

average = sum(grades) / 4

for grade in grades:
    print(grade)

print(f"A média é: {average}")
