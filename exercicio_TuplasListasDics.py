""" Exercicio 1: """

palavras = ('Maça', 'Pera', 'Chocolate', 'Laranja', 'Carne', 'Uva')

for p in palavras:
    print('\n', p, ': ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')


""" Exercício 2: """
from random import randint
computador = randint(1, 3)
placar = []
jogada = []
soma_jogador = 0
soma_computador = 0

print('='*25)
print('PEDRA - PAPEL - TESOURA')
print('='*25)
while True:
    escolha = int(input('Faça sua escolha:\n[1] - Pedra\n[2] - Papel\n[3] - Tesoura\n'))
    if escolha == 1:
        print('Você escolheu 1 - Pedra', end='')
        if computador == 1:
            jogada.append('EMPATOU!')
            print(' e o computador escolheu {} - Pedra'.format(computador))
        elif computador == 2:
            soma_computador += 1
            jogada.append('COMPUTADOR VENCEU!')
            print(' e o computador escolheu {} - Papel'.format(computador))
        elif computador == 3:
            soma_jogador += 1
            jogada.append('JOGADOR VENCEU!')
            print(' e o computador escolheu {} - Tesoura'.format(computador))
        print('-'*15)

    elif escolha == 2:
        print('Você escolheu 2 - Papel', end='')
        if computador == 1:
            soma_jogador += 1
            jogada.append('JOGADOR VENCEU!')
            print(' e o computador escolheu {} - Pedra'.format(computador))
        elif computador == 2:
            jogada.append('EMPATOU!')
            print(' e o computador escolheu {} - Papel'.format(computador))
        elif computador == 3:
            soma_computador += 1
            jogada.append('COMPUTADOR VENCEU!')
            print(' e o computador escolheu {} - Tesoura'.format(computador))

    elif escolha == 3:
        print('Você escolheu 3 - Tesoura', end='')
        if computador == 1:
            soma_computador += 1
            jogada.append('COMPUTADOR VENCEU!')
            print(' e o computador escolheu {} - Pedra'.format(computador))
        elif computador == 2:
            soma_jogador += 1
            jogada.append('JOGADOR VENCEU!')
            print(' e o computador escolheu {} - Papel'.format(computador))
        elif computador == 3:
            jogada.append('EMPATOU!')
            print(' e o computador escolheu {} - Tesoura'.format(computador))
    placar.append(jogada[:])
    print(jogada)
    continuar = int(input('Deseja continuar?[0 - Não | 1 - Sim]: '))
    jogada.clear()
    if continuar == 0:
        break
    elif continuar == 1:
        continue

print('*'*25)
for jogo in placar:
    print(jogo)
print('*'*25)
if soma_jogador > soma_computador:
    print('O JOGADOR GANHOU O FINAL DO TORNEIO!!!')
elif soma_jogador < soma_computador:
    print('O COMPUTADOR GANHOU O FINAL DO TORNEIO!!!')
else:
    print('O TORNEIO FINAL TEVE EMPATE!!!')


""" Exercício 3 """
dic = {'nome': [],
       'ano_nascimento': [],
       'sexo': []}

m_menos30 = []
h_acimaMedia = []

tot_cadastro = 0
soma_idade = 0

while True:
    nome = input('Digite um nome: ')
    ano_nascimento = int(input('Digite o ano de nascimento: '))
    sexo = input('Informe o sexo[M/F]: ').upper()
    dic['nome'].append(nome)
    dic['ano_nascimento'].append(ano_nascimento)
    dic['sexo'].append(sexo)
    tot_cadastro += 1
    soma_idade += (2022-ano_nascimento)
    if sexo == 'F' and 2022 - ano_nascimento < 30:
        m_menos30.append(nome)
    continuar = int(input('Deseja continuar?[0 - Não 1 - Sim]: '))
    if continuar == 0:
        break
    elif continuar == 1:
        continue

print('O total de cadastros efetuados foi de {} cadastros'.format(tot_cadastro))
print('A média de idade das pessoas é de {} anos'.format(soma_idade/tot_cadastro))
print('A lista das mulheres com menos de 30 anos: ')
for m in m_menos30:
    print(m)



