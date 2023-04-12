'''
    12.	Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã.

    Dados extras:
    -	Distância da casa de Maria até sua irmã : 520 km
    -	Seu carro consome 12 Km/litro de combustível.
    -	Ela abastece sempre no mesmo posto, onde o preço da gasolina é R$ 4,50 o litro.

    Desenvolva um algoritmo onde o usuário digite a distância, o consumo e o valor do litro de combustível, com estes dados o algoritmo deverá calcular a quantidade de litros de combustível para a viagem e o custo da viagem.
'''

distancia = float(input("Digite o distância: "))
consumo = float(input("Digite o consumo do automóvel: "))
preco_gasolina = float(input("Digite o valor da gasolina: "))

custo_da_viagem = (distancia / consumo) * preco_gasolina

print(f"O custo para percorrer {distancia}km é de {custo_da_viagem}")