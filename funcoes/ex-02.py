'''
2) Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere "P", se seu argumento for positivo, e "N", se seu argumento for zero ou negativo.
'''


def positiveOrNegative(value):
    if (value < 0):
        print("N")
    else:
        print("P")


positiveOrNegative(-1)
positiveOrNegative(0)
positiveOrNegative(1)
