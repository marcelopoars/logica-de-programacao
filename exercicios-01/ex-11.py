'''
    Escrever um algoritmo para ler uma temperatura em Fahrenheit e apresentá-la convertida em graus
    Celsius.

                         (Fahrenheit - 32) x 5
    Fórmula: Celsius =  ---------------------- 
                                  9
'''


fahrenheit = float(input("Digite a temperatura em Fahrenheit: "))

degrees_celsius = ((fahrenheit - 32) * 5) / 9

print(f"A temperatura convertida para graus Celsius é: {degrees_celsius}")