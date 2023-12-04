
# MARCELO PEREIRA DA SILVA

disciplinas_disponiveis = [
    "Lógica de Programação",
    "Fundamentos Computacionais",
    "Fundamentos de Redes de Computadores",
    "User Experience",
    "Desenvolvimento de Interfaces para Web"
]

listaA = []
listaB = []


def imprimeTituloDestacado(texto):
    print(f"\n{texto}\n{len(texto) * '='}")


def preencherListaA():  # Questão 01
    for disciplina in disciplinas_disponiveis:
        listaA.append(disciplina)


def preencherListaB():  # Questão 02
    imprimeTituloDestacado(
        "Preencha a listaB com números inteiros entre 100 e 500")
    while len(listaB) < 10:
        while True:
            value = input(f"Digite o {len(listaB) + 1}o valor: ")
            
            if not value.isdigit():
                print("\n*** OPS. Só valem números inteiros ***\n")

            elif (int(value) < 100 or int(value) > 500):
                print("\n*** OPS. Só vale números entre 100 e 500 ***\n")

            else:
                listaB.append(int(value))
                break


def escolhaUmaDasDisciplinas():  # Questão 03
    # Se a "listaA" estiver vazias, a função "preencherListaA()" é chamada
    if len(listaA) == 0:
        preencherListaA()  # Preencha a listaA

    # Imprime título sublinado
    imprimeTituloDestacado("Disciplinas do I Semeste")

    # Imprime a lista de disciplinas (original)
    for index, disciplina_in_listaA in enumerate(listaA):
        print(f"{index + 1} - {disciplina_in_listaA}")

    while True:  # Loop para pedir para usuário escolher uma opção
        lista_de_opcoes = ["1", "2", "3", "4", "5"]
        opcao = input("\nDigite uma mas opções: ")

        # ´Mostra mensagem de erro ae a opção digitada pelo usuário não estiver na lista
        if opcao not in lista_de_opcoes:
            print("\n** Opção inválida **")
        else:
            disciplina_escolhida = listaA[int(opcao) - 1]
            print(disciplina_escolhida)
            break

    # A função lambda pega um elemento "disciplina" e retorna o comprimento desse elemento "len(disciplina)"
    # A função sorted() retorna uma nova lista ordenada do MENOR para o MAIOR
    listaA_ordenada = sorted(listaA, key=lambda disciplina: len(disciplina))
    # Inverte a ordem da lista do MAIOR para o MENOR
    listaA_ordenada = listaA_ordenada[::-1]

    # Imprime título sublinado
    imprimeTituloDestacado("Lista ordenada do maior para menor")
    # Percorre a "listaA_ordenada" e encontra o índice da disciplina na "listaA_ordenada"
    for index, disciplina in enumerate(listaA_ordenada):
        if disciplina == disciplina_escolhida:
            indice_disciplina_escolhida = index + 1

        print(f"{index + 1} - {disciplina}")


    imprimeTituloDestacado("Resultado")

    print(f"- Disciplina escolhida: {disciplina_escolhida}")
    print(f"- Quantidade de letras: {len(disciplina_escolhida)}")
    print(
        f"- A disciplina é a {indice_disciplina_escolhida}a da lista com mais letras")


def numerosComRestoZero():  # Questão 04
    # Se a "listaB" estiver vazia, a função "preencherListaB" será invocada
    if len(listaB) == 0:
        print("\n*** A listaB está vazia! ***")
        preencherListaB()

    numeros_com_resto_zero = 0  # Contador

    for number in listaB:
        # Verifica quais números da lista tem resto zero
        if (number % 2) == 0:
            numeros_com_resto_zero += 1  # Incrementa o contador

    imprimeTituloDestacado("Resultado")

    print(f"Quantidade de números com resto zero: {numeros_com_resto_zero}")


def converterNumeroParaString():  # Questão 05
    # Se a "listaB" estiver vazia, a função "preencherListaB" será invocada
    if len(listaB) == 0:
        print("\n*** A listaB está vazia! ***")
        preencherListaB()

    imprimeTituloDestacado(f"\nListaB: {listaB}")  # listaB = [120, 235, 400]

    while True:
        # define o tamanho do maior indice do array
        indice_maximo = (len(listaB) - 1)

        valor_digitado = input(f"Escolha um índice da lista entre 0 e {indice_maximo}: ")
        
        # Verifica se valor digitado não é um numero
        if not valor_digitado.isdigit():
            print("\n*** OPS! Índice inválido! ***\n")

        # Converte o valor digitado para inteiro
        indice = int(valor_digitado)

        # Aqui verifico se o valor está no intervado de 0 a 9 (indices válidos)
        if indice < 0 or indice > indice_maximo:
            print(f"\n*** OPS! Índice inválido! Digite um número entre 0 e {indice_maximo} ***\n")
        else:
            # Sobrescreve o valor na lista no formato "string"
            listaB[indice] = str(listaB[indice])
            break # Encerra o loop

    imprimeTituloDestacado("Resultado")

    print(f"\nListaB: {listaB}")

def pegaAsTresPrimeirasLetras():
      # Se a "listaA" estiver vazias, a função "preencherListaA()" é chamada
    if len(listaA) == 0:
        preencherListaA()  # Preencha a listaA

    imprimeTituloDestacado("Lista de disciplinas")

    # Itera a listaA para pegar o valor de cada posição do array
    for disciplina in listaA:
        # Pegar as três primeira letras da disciplina
        tres_primeiras_letras = disciplina[0:3]

        print(f"{tres_primeiras_letras.upper()} - {disciplina}")


# **** TESTAR A QUESTÃO 01 ****
imprimeTituloDestacado("Questão 01")
print("Este algoritmo preenche a listaA com nomes das disciplinas do I semestre de ADS.")
preencherListaA()
print(f"\nlistaA: {listaA}")

# **** TESTAR A QUESTÃO 02 ****
# imprime_titulo_destacado("Questão 02")
# print("Este algoritmo preenche a listaB com 10 números entre 100 e 500.")
# preencherListaB()
# print(f"\nlistaB: {listaB}")

# **** TESTAR A QUESTÃO 03 ****
# imprime_titulo_destacado("Questão 03")
# print("Este algoritmo permite escolher uma das disciplinas da listaA, e retorna informações sobre o tamanho da mesma.")
# escolhaUmaDasDisciplinas()

# **** TESTAR A QUESTÃO 04 ****
# imprime_titulo_destacado("Questão 04")
# print("Este algoritmo retorna a quantidade de números com resto zero contidos na listaB.")
# numerosComRestoZero()

# **** TESTAR A QUESTÃO 05 ****
# imprime_titulo_destacado("Questão 05")
# print("Este algoritmo recebe um valor como índice da listaB e se índice for válido, converte o valor para 'string' e sobrescreve o valor original na listaB.")
# converterNumeroParaString()

# **** TESTAR A QUESTÃO 6 ****
# imprime_titulo_destacado("Questão 06")
# print("Este algoritmo imprime as três primeiras letras das disciplinas da 'listaA'.")
# pegaAsTresPrimeirasLetras()

