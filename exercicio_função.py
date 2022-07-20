# Exercício 1 - Fatorial
def fatorial(num, validacao):
    if validacao(num):
        x = num
        for i in range(num, 1, -1):
            x = x * (i-1)
        return x


def numero_validado(x):
    if x > 0:
        return x


resultado = fatorial(5, numero_validado)
print(resultado)


# Exercício 2 - Cadastro de Jogos
# Tela Inicial
def tela_inicial():
    print('+ '+'-'*10 + '+')
    print('|GAME MANIA|')
    print('+ '+'-'*10 + '+')
    menu_cadastro()


# Menu Geral Para Cadastro
def menu_cadastro():
    while True:
        try:
            print('[1] - Cadastrar Novo Item')
            print('[2] - Listar Jogos Cadastrados')
            print('[3] - Sair')
            opcao = int(input('Selecione uma opção: '))
            if opcao == 1:
                cadastro_novoItem()
            elif opcao == 2:
                listar_jogosCadastrados()
            elif opcao == 3:
                print('Finalizando programa...')
                break
            else:
                print('Informe um valor que seja 1, 2 ou 3! Tente novamente...')
                continue
        except ValueError:
            print('Informe um número inteiro! Tente novamente...')
            continue


# Menu Para Cadastrar um Novo Item
def cadastro_novoItem():
    while True:
        nome_jogo = input('Informe o novo do Jogo: ')
        pertence_videogame = input('Informe o video-game que ele pertence: ')
        adicionar_jogos(nome_jogo, pertence_videogame)
        continuar = input('Deseja continuar cadastrando?[S/N]: ').upper()
        if continuar == 'S':
            continue
        elif continuar == 'N':
            print('+ '+'-'*10 + '+')
            print('Saindo...')
            print('+ ' + '-' * 10 + '+')
            break
        else:
            print('Digite somente S - Sim ou N - Não! Tente novamente...')
            continue


# Listar Todos os Jogos Cadastrados
def listar_jogosCadastrados():
    arquivo = open("jogos.txt", "r")
    print(arquivo.readlines())


# Função para Cadastrar os Jogos
def adicionar_jogos(jogo, videogame):
    global arquivo
    arquivo = open("jogos.txt", "a")
    frases = list()
    frases.append("\n"+jogo + " - " + videogame)
    arquivo.writelines(frases)


# Onde Tudo se Inicia
tela_inicial()
