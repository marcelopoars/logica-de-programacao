'''
    04 - Faça um Programa que leia um vetor de 10 caracteres, 
    e diga quantas consoantes foram lidas. Imprima as consoantes.
'''

vowels = ["a", "e", "i", "o", "u"]
characters = ["a", "f", "d", "i", "x", "y", "z", "y", "u", "t"]

for char in characters:
    if (char.lower() not in vowels):
        print(char)
