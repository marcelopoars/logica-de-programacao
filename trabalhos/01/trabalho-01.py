'''
MARCELO PEREIRA DA SIVA
------------------------------------------------------------------------------
Lógica de Programação
UNISENAC - CENTRO UNIVERSITÁRIO SENAC-RS.
------------------------------------------------------------------------------

Faça um programa que, para um número indeterminado de pessoas: leia a idade de cada uma, sendo que a idade 0 (zero) indica o fim da leitura e não deve ser considerada. A seguir calcule: 

- a quantidade de pessoas;
- a idade média do grupo;
- a menor idade e a maior idade.
'''

age_list = []
minor_age = 0
older_age = 0

while(True):
    age = int(input("Digite a idade: ")) # idade digitada pelo usuário

    if (age == 0): # se usuário digitar zero, encerra o programa
        break

    age_list.append(age) # adiciona a idade digitada no array

    if (minor_age == 0 and older_age == 0):
        minor_age = age
        older_age = age
    
    if (age < minor_age): # teasta a menor idade
        minor_age = age

    if (age > older_age): # testa a maior idade
        older_age = age

if(len(age_list)):
    print("\n*** Resultado ***")
    print(f"Quantidade de pessoas: {len(age_list)}") # Retorna o tamanho ro array
    print(f"A idade média do grupo é: {sum(age_list)/len(age_list)}") # Retorna a soma do array dividido pelo seu tamanho
    print(f"A menor idade digitada é: {minor_age}") # Retorna a manor idade digitada
    print(f"A maior idade digitada é: {older_age}") # Retorna a maior idade digitada
else:
    print("\n*** Fim do programa! ***")
    