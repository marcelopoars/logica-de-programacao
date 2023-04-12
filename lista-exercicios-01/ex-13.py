'''
    13.	Ler um número n e imprimir MENSAGEM 1, MENSAGEM 2 ou MENSAGEM 3, conforme a condição:

    se n <= 10 imprima MENSAGEM 1,
    se n > 10 e <= 100 imprima MENSAGEM 2
    se n >100 imprima MENSAGEM 3,
'''

number = int(input("Por favor digite um número: "))

if(number <= 10):
    print("MENSAGEM 1")
elif(number > 10 and number <= 100):
    print("MENSAGEM 2")
else:
    print("MENSAGEM 3")