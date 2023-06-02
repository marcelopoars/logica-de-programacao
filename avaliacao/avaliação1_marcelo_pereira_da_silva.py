'''
Faça um algoritmo que leia o nome de dos meses do ano  e armazene esses nomes em uma lista chamada lst_meses.

Após preencher a lista:
Cada  cada mês da lista receberá uma uma temperatura média do mês.
 
Mostre o mês com maior temperatura
Mostre também a média das temperaturas do Ano. 
Mostre o mês com a temperatura mais alta e o o mês com a temperatura mais baixa.
'''

lst_meses = [] # armazena os 12 meses digitados pelo usuário
lst_temperaturas = [] # armazena as 12 temperaturas digitadas pelo usuário
mes_com_maior_temperatura = ""
mes_com_menor_temperatura = ""
media_de_temperatura_anual = 0

print("\n===== Digite os 12 meses do ano e suas temperaturas =====")

while(True):
    # Encerra o programa quando usuário digitar os 12 meses
    if (len(lst_meses) == 12):
        break
    mes = input("Digite o nome do mês: ").lower()
    temperatura = input(f"Digite a média da temperatura do mês de {mes.capitalize()}: ")
    
    lst_meses.append(mes) # adiciona o mês digitado na lista
    lst_temperaturas.append(float(temperatura)) # adiciona a temperatura digitada na lista

    maior_temperatura = max(lst_temperaturas) # encontra a maior temperatura
    menor_temperatura = min(lst_temperaturas) # encontra a menor temperatura

    indice_da_maior_temperatura = lst_temperaturas.index(maior_temperatura) # encontra o indice da maior temperatura
    indice_da_menor_temperatura = lst_temperaturas.index(menor_temperatura) # encontra o indice da menor temperatura

    mes_com_maior_temperatura = lst_meses[indice_da_maior_temperatura].capitalize() # encontra o mês com a maior temperatura
    mes_com_menor_temperatura = lst_meses[indice_da_menor_temperatura].capitalize() # encontra o mês com a menor temperatura

    media_de_temperatura_anual = round(sum(lst_temperaturas) / len(lst_temperaturas), 2) # calcula a média da temperatura anual

print("\n=============== RESULTADO ===============")
print(f"O mês com a MAIOR temperatura é: {mes_com_maior_temperatura}")
print(f"O mês com a MENOR temperatura é: {mes_com_menor_temperatura}")
print(f"A MÉDIA da temperatura anual é: {media_de_temperatura_anual}º")