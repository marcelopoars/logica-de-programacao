'''
RS-20231-FSPOA-LPR-PRE-ADS1N23-1A (Lógica de Programação (ADS1N23-1A) - 63)
- Avaliação Final
- Marcelo Pereira da Silva
'''


# Listas para armazenar os dados dos alunos
lst_nome = []
lst_idade = []
lst_peso = []
lst_altura = []
lst_imc = []
# Lista para armazenar os logs coletados durante a execução do programa
lst_logs = []
# Lista com as opções do menu principal do programa
lst_menu_principal = [
    "1 - Incluir aluno(a)",
    "2 - Listar todos os alunos e seus dados",
    "3 - Listar os dados de um(a) aluno(a)",
    "4 - Listar os dados de todos alunos de uma determinada idade",
    "5 - Excluir um(a) aluno(a)",
    "6 - Imprimir LOGs",
    "0 - Sair",
]
# Lista com as opções do menu principal que o usuário pode escolher
lst_opcoes = ["0", "1", "2", "3", "4", "5", "6"]


# Função auxiliar para coletar logs durante a execução do programa
def pegarLog(text):
    lst_logs.append(text)


# A função auxiliar "imprimeTituloDestacado()" imprime um título destacado
def imprimeTituloDestacado(texto=''):
    pegarLog(f"Função imprimeTituloDestacado({texto.upper()})")

    print(f"\n{70 * '='}\n{texto.upper()}\n{70 * '='}")


# A função auxiliar "calcularImc()" calcula o IMC
def calcularImc(peso=None, altura=None):
    pegarLog("Função calcularImc()")

    if not peso or not altura:
        print("\n*** Peso e altura são obrigatórios ***\n")
        return  # Encerra a função

    return round((float(peso) / float(altura) ** 2), 2)


# A função auxiliar "clacularImcMedio()" recebe uma lista de IMCs
# e calcula o IMC médio
def clacularImcMedio(lista=[]):
    pegarLog("Função clacularImcMedio()")

    return round(sum(lista) / len(lista), 2)


# A função auxiliar "nomeValido()" verifica se é um nome válido
def nomeValido(nome):
    pegarLog("Função nomeValido()")

    if nome.strip() == '':
        print(f"\n*** Nome é obrigatório ***\n")
        return False  # Encerra a função e retorna "False"
    if nome.isdigit():
        print("\n*** Nome inválido. Digite apenas letras ***\n")
        return False  # Encerra a função e retorna "False"

    return True  # Encerra a função e retorna "True"


# A função auxiliar "cadastrarNome()" adiciona o nome na lista
def cadastrarNome():
    pegarLog("Função cadastrarNome()")

    while True:
        nome = input("Digite o NOME do(a) aluno(a): ")

        if nomeValido(nome):
            lst_nome.append(nome.strip().upper())
            break


# A função "idadeValida()" verifica se é uma idade válida
def idadeValida(idade):
    pegarLog("Função idadeValida()")

    if not idade.isdigit():
        print("\n*** Idade inválida. Digite um valor inteiro ***\n")
        return False  # Encerra a função e retorna "False"
    if int(idade) <= 0 or int(idade) > 150:
        print(
            "\n*** Idade inválida. Digite um valor maior que zero e menor que 150 ***\n")
        return False  # Encerra a função e retorna "False"

    return True  # Encerra a função e retorna "True"


# A função auxiliar "cadastrarIdade()" adiciona a idade na lista
def cadastrarIdade():
    pegarLog("Função cadastrarIdade()")

    while True:
        idade = input("Digite a IDADE do(a) aluno(a): ")

        if idadeValida(idade):
            lst_idade.append(int(idade))
            break


# A função auxiliar "pesoValido()" verifica se é um peso válido
def pesoValido(peso):
    pegarLog("Função pesoValido()")

    if peso.strip() == '':
        print(f"\n*** Peso é obrigatório ***\n")
        return False  # Encerra a função e retorna "False"
    if not peso.replace('.', '', 1).isdigit():
        print(
            "\n*** Peso inválido. Digite um valor positivos (inteiros ou floats) ***\n")
        return False  # Encerra a função e retorna "False"

    return True  # Encerra a função e retorna "True"


# A função auxiliar "cadastrarPeso()" adiciona o peso na lista
def cadastrarPeso():
    pegarLog("Função cadastrarPeso()")

    while True:
        peso = input("Digite o PESO do(a) aluno(a): ")

        if (pesoValido(peso)):
            peso = round(float(peso), 2)
            lst_peso.append(peso)
            break
    return peso  # Retorna peso no tipo float


# A função auxiliar "alturaValida()" verifica se é uma altura válido
def alturaValida(altura):
    pegarLog("Função cadastrarAltura()")

    if altura.strip() == '':
        print(f"\n*** Altura é obrigatório ***\n")
        return False  # Encerra a função e retorna "False"
    if not altura.replace('.', '', 1).isdigit():
        print(
            "\n*** Altura inválida. Digite um valor positivos (inteiros ou floats) ***\n")
        return False  # Encerra a função e retorna "False"
    if float(altura) > 2.5:  # Homem mais alto do mundo tem 2.5m
        print(f"\n*** Altura inválida. Digite um valor menor que 2.5 metros ***\n")
        return False  # Encerra a função e retorna "False"
    return True  # Encerra a função e retorna "True"


# A função auxiliar "cadastrarAltura()" adiciona a aultura na lista
def cadastrarAltura():
    pegarLog("Função cadastrarAltura()")

    while True:
        altura = input(
            "Digite a ALTURA do(a) aluno(a) em METROS. (Ex.: 1.80): ")

        if alturaValida(altura):
            altura = round(float(altura), 2)
            lst_altura.append(altura)
            break

    return altura  # Retorna altura no tipo float


# A função auxiliar "cadastrarAltura()" adiciona a aultura na lista
def cadastrarAluno():  # Opção "1"
    pegarLog("Função cadastrarAluno()")

    imprimeTituloDestacado("Cadastrar aluno(a)")

    cadastrarNome()
    cadastrarIdade()

    peso_aluno = cadastrarPeso()
    altura_aluno = cadastrarAltura()

    imc_aluno = calcularImc(peso_aluno, altura_aluno)
    lst_imc.append(imc_aluno)

    print("\n*** Aluno(a) cadastrado(a) com sucesso ***")


# A função auxiliar "listaDeAlunoEstaVazia()" verifica se existem alunos cadastrados
# Se a lista estiver vazia, retorna 'True'
def listaDeAlunoEstaVazia():
    pegarLog("Função listaDeAlunoEstaVazia()")

    if len(lst_nome) == 0:
        pegarLog("*** Não existem alunos cadastrados ***")

        print("\n*** Não existem alunos cadastrados ***")
        return True  # Este "return" encerra a função listaDeAlunoEstaVazia()
    return False  # Retorna "False" se a lista não estiver vazia


# A função auxiliar "imprimeCabecalhoDaLista()" imprime o cabeçalho formatada,
# facilitando a leitura dos dados do(a) aluno(a)
def imprimeCabecalhoDaLista():
    pegarLog("Função imprimeCabecalhoDaLista()")

    print("{:<30}".format("Nome"), end="")
    print("{:<8}".format("Idade"), end="")
    print("{:<8}".format("Peso"), end="")
    print("{:<10}".format("Altura"), end="")
    print("{:<8}".format("IMC"))

    print("=" * 70)


# A função auxiliar "listarDadosDoAluno()" recebe um índice e imprime os dados
# deste aluno formatados, facilitando a leitura destes dados
def listarDadosDoAluno(indice):
    pegarLog("Função listarDadosDoAluno()")

    # Verifica se existem alunos cadastrados
    if listaDeAlunoEstaVazia():
        return  # Este "return" encerra a função listarDadosDoAluno()

    print("{:<30}".format(lst_nome[indice]), end="")
    print("{:<8}".format(lst_idade[indice]), end="")
    print("{:<8}".format(lst_peso[indice]), end="")
    print("{:<10}".format(lst_altura[indice]), end="")
    print("{:<8}".format(lst_imc[indice]))

    print("-" * 70)


# A função auxiliar "listarDadosDosAlunos()" iprime os dados de todos os alunos cadastrados
# e imprime o IMC geral do grupo
def listarDadosDosAlunos():  # Opção "2"
    pegarLog("Função listarDadosDosAlunos()")

    # Verifica se existem alunos cadastrados
    if listaDeAlunoEstaVazia():
        return  # Este "return" encerra a função listarDadosDosAlunos()

    imprimeTituloDestacado("Dados dos alunos")

    imprimeCabecalhoDaLista()

    #
    for indice, _ in enumerate(lst_nome):
        listarDadosDoAluno(indice)

    # Imprime o IMC geral do grupo no final da lista
    print("IMC médio do grupo:", clacularImcMedio(lst_imc))


# A função auxiliar "listarDadosDoAlunoPorNome()" verifica se o nome do(a) aluno(a) está na lista 'lst_nome'
# Se o aluno for encontrado, imprime os dados deste aluno
def listarDadosDoAlunoPorNome():  # Opção "3"
    pegarLog("Função listarDadosDoAlunoPorNome()")

    # Verifica se existem alunos cadastrados
    if listaDeAlunoEstaVazia():
        return  # Este "return" encerra a função listarDadosDoAlunoPorNome()

    imprimeTituloDestacado("Buscar aluno(a) pelo nome")

    while True:
        nome_do_aluno = input("Digite o nome do(a) aluno(a): ").strip().upper()

        if nomeValido(nome_do_aluno):
            if nome_do_aluno not in lst_nome:
                print(f"\n*** O nome {nome_do_aluno} não foi encontrado ***")
                break
            else:
                indice_do_aluno = lst_nome.index(nome_do_aluno)
                imprimeTituloDestacado(f"Dados do(a) aluno(a) {nome_do_aluno}")
                imprimeCabecalhoDaLista()
                listarDadosDoAluno(indice_do_aluno)
                break


# A função auxiliar "listarDadosDeAlunosPorIdade()" busca alunos na lista com a idade informada
# A função imprime os dados dos alunos e o IMC médio do grupo com a idade informada
def listarDadosDeAlunosPorIdade():  # Opção "4"
    pegarLog("Função listarDadosDeAlunosPorIdade()")

    # Verifica se existem alunos cadastrados
    if listaDeAlunoEstaVazia():
        return  # Este "return" encerra a função listarDadosDeAlunosPorIdade()

    imprimeTituloDestacado("Dados de alunos por idade")

    while True:
        idade_digitada = input("\Digite uma idade: ")

        if idadeValida(idade_digitada):
            idade_digitada = int(idade_digitada)

            if idade_digitada not in lst_idade:
                print(
                    f"\n*** Não existem alunos com {idade_digitada} anos ***")
                break
            else:
                lst_imc_por_idade = []

                imprimeCabecalhoDaLista()

                for indice_na_lista, idade_na_lista in enumerate(lst_idade):
                    if idade_na_lista == idade_digitada:
                        lst_imc_por_idade.append(lst_imc[indice_na_lista])
                        listarDadosDoAluno(indice_na_lista)

                # Imprime o IMC médio deste grupo
                print("IMC médio do grupo:",
                      clacularImcMedio(lst_imc_por_idade))
                # Encerra o laço
                break


# A função auxiliar "excluirAluno()" exclui os dados do(a) aluno(a) de todas as listas
def excluirAluno():  # Opção "5"
    pegarLog("Função excluirAluno()")

    # Verifica se existem alunos cadastrados
    if listaDeAlunoEstaVazia():
        return  # Este "return" encerra a função excluirAluno()

    imprimeTituloDestacado("Excluir aluno(a) pelo nome")

    while True:
        nome_do_aluno = input("Digite o nome do(a) aluno(a): ").strip().upper()

        if nomeValido(nome_do_aluno):
            # Verifica se o nome digitado está na lista de alunos
            if nome_do_aluno not in lst_nome:
                print(f"\n*** O nome {nome_do_aluno} não foi encontrado ***")
                break
            else:
                # Busca na lista o índice do aluno
                indice_do_aluno = lst_nome.index(nome_do_aluno)

                # Remove das listas dos dados do aluno
                lst_nome.remove(lst_nome[indice_do_aluno])
                lst_idade.remove(lst_idade[indice_do_aluno])
                lst_peso.remove(lst_peso[indice_do_aluno])
                lst_altura.remove(lst_altura[indice_do_aluno])
                lst_imc.remove(lst_imc[indice_do_aluno])

                print(
                    f"\n*** Os dados do(a) aluno(a) {nome_do_aluno} foram excluidos ***")
                # Encerra o laço
                break


# A função auxiliar "imprimirLogs()" imprime a lista
# com todas as funções que foram chamadas, durante a execução do programa
def imprimirLogs():  # Opção "6"
    pegarLog("Função imprimirLogs()")

    imprimeTituloDestacado("Logs do programa")

    pegarLog("Imprime lista de logs")

    for indice_do_log, log in enumerate(lst_logs):
        print(f"{indice_do_log + 1} - {log}")
        print("-" * 70)


# A função auxiliar "encerrarPrograma()" encerra o programa
def encerrarPrograma():  # Opção "0"
    pegarLog("encerrarPrograma()")

    input("\nDeseja sair do programa? Digite ENTER para sair. ")
    print("\n*** Programa encerrado ***")

    pegarLog(">Usuário deu ENTER para sair")


##########################
#    FUNÇÃO PRINCIPAL    #
##########################
# A função "executarPrograma()" vai chamar todas as outras funções auxiliares
def executarPrograma():
    pegarLog("> Início: executarPrograma()")

    while True:
        pegarLog(">> while True")

        imprimeTituloDestacado("Programa de cadastro de alunos")

        for item in lst_menu_principal:
            print(item)

        pegarLog(">>> Digite uma das opções:")

        opcao = input("\nDigite uma das opções: ")

        if opcao not in lst_opcoes:
            print("\n*** Opção inválida ***")

        if opcao == '0':
            encerrarPrograma()
            pegarLog(">>>> Opção 0")
            break
        if opcao == '1':
            cadastrarAluno()
            pegarLog(">>>> Opção 1")
        if opcao == '2':
            listarDadosDosAlunos()
            pegarLog(">>>> Opção 2")
        if opcao == '3':
            listarDadosDoAlunoPorNome()
            pegarLog(">>>> Opção 3")
        if opcao == '4':
            listarDadosDeAlunosPorIdade()
            pegarLog(">>>> Opção 4")
        if opcao == '5':
            excluirAluno()
            pegarLog(">>>> Opção 5")
        if opcao == '6':
            imprimirLogs()
            pegarLog(">>>> Opção 6")

        input("\nDigite ENTER para continuar... ")


# Invocando a função principal
executarPrograma()
