'''
    Fazer um algoritmo para ler duas notas, os pesos de cada nota e mostrar a média ponderada.

                                  (nota 1 * peso da nota 1) + (nota 2 * peso da nota 2)
    Cálculo da Média Ponderada =  -----------------------------------------------------
                                                  soma dos pesos

'''

note1 = float(input("Digite a primeira nota: "))
weight_note1 = float(input("Digite o peso da primeira nota: "))

note2 = float(input("Digite a segunda nota: "))
weight_note2 = float(input("Digite o peso da segunda nota: "))

weighted_average = ((note1 * weight_note1) + (note2 * weight_note2)) / (weight_note1 + weight_note2)

print(f"A média ponderada é: {weighted_average}")