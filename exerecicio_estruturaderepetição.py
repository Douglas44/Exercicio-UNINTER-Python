
# Sequência de 3 a 12 com For e While
x = 3
while x < 12+1:
    print(x)
    x += 1

for i in range(3, 12+1, 1):
    print(i)


# Sequência de 0 a 9, tirando o 9, com passo de 2
x = 0
while x < 9:
    print(x)
    x += 2

for i in range(0, 9, 2):
    print(i)


# Exercício 1
# Problema: Escreva um algoritmo que leia dois valores
# numéricos e que pergunte ao usuário qual
# operação ele deseja realizar: adição (+),
# subtração (-), multiplicação (*), divisão (/)
# e sair. Exiba na tela o resultado da operação
# desejada

# Repita até que a opção saída seja escolhida


while True:
    print('='*15)
    num1 = int(input('Diga um número: '))
    num2 = int(input('Diga mais um número: '))
    print('='*15)
    print('[+] Adição')
    print('[-] Subtração')
    print('[*] Multiplicação')
    print('[/] Divisão')
    print('[s] Sair')
    print('=' * 15)
    operacao = input('Digite a operação que deseja realizar: ').upper()
    if operacao != '+' and operacao != '-' and operacao != '*' and operacao != '/' and operacao != 'S':
        print('Operação inválida. Tente novamente')
        continue
    if operacao == '+':
        print('A operação de {} foi o valor {} '.format(operacao, num1+num2))
    elif operacao == '-':
        print('A operação de {} foi o valor de {}'.format(operacao, max(num1, num2) - min(num1, num2)))
    elif operacao == '*':
        print('A operação de {} foi o valor de {} '.format(operacao, num1*num2))
    elif operacao == '/':
        print('A operação de {} foi o valor de {} '.format(operacao, max(num1, num2)/min(num1, num2)))
    elif operacao == 'S':
        break



# Exercício 2
# Escreva um algoritmo que leia um valor
# e que imprima a quantidade de cédulas
# necessárias para pagar esse mesmo valor.
# Para simplificar, vamos trabalhar apenas
# com valores inteiros e com cédulas de R$
# 100, R$ 50, R$ 20, R$ 10, R$ 5 e R$ 1

valor = int(input('Diga um valor: R$'))
while True:
    if valor >= 100:
        cedulas100 = valor // 100
        valor = valor - cedulas100*100
        print('Cédulas de R$100: {}'.format(cedulas100))
        if valor == 0:
            break

    if valor >= 50:
        cedulas50 = valor // 50
        valor = valor - cedulas50*50
        print('Cédulas de R$50: {}'.format(cedulas50))
        if valor == 0:
            break

    if valor >= 20:
        cedulas20 = valor // 20
        valor = valor - cedulas20*20
        print('Cédulas de R$20: {}'.format(cedulas20))
        if valor == 0:
            break

    if valor >= 10:
        cedulas10 = valor // 10
        valor = valor - cedulas10*10
        print('Cédulas de R$10: {}'.format(cedulas10))
        if valor == 0:
            break

    if valor >= 5:
        cedulas5 = valor // 5
        valor = valor - cedulas5*5
        print('Cédulas de R$5: {}'.format(cedulas5))
        if valor == 0:
            break

    if valor >= 1:
        cedulas1 = valor // 1
        valor = valor - cedulas1*1
        print('Cédulas de R$1: {}'.format(cedulas1))
        if valor == 0:
            break


# Exercício 3

qntd_compras = 0
tot_dinheiro = 0
media_idade = 0
soma_idade = 0
while True:
    print('BEM VINDO AO CINEMA BOA-VISTA')
    print('='*20)
    idade = int(input('Informe sua idade por gentileza: '))
    soma_idade = soma_idade + idade
    print('*'*7)
    print('[Gratuito] - Até 2 anos')
    print('[R$15] - Entre 3 anos e 12 anos')
    print('[R$30] - Mais de 12 anos')
    print('[N] - Para Sair')
    print('*'*7)
    pergunta = input('Deseja comprar o ingresso?[S/N]: ').upper()
    if pergunta == 'S':
        qntd_compras += 1
        if idade < 3:
            tot_dinheiro += 0
            print('☑ Compra Feita com Sucesso')
            print('Valor - [Gratuito]')
            print('*'*10)
        elif 12 >= idade >= 3:
            tot_dinheiro += 15
            print('☑ Compra Feita com Sucesso')
            print('Valor - [R$15]')
            print('*'*10)
        elif idade > 12:
            tot_dinheiro += 30
            print('☑ Compra Feita com Sucesso')
            print('Valor - [R$30]')
            print('*'*10)
    elif pergunta == 'N':
        break
    else:
        print('Digite uma opção válida')
        continue

print('='*25)
print('RELATÓRIO DE COMPRAS')
print('='*25)
print('Total de pessoas que compraram os ingressos: {} pessoas'.format(qntd_compras))
print('Total de dinheiro arrecadado: R${}'.format(tot_dinheiro))
media_idade = soma_idade/qntd_compras
print('Média de idade entre as pessoas: {} anos'.format(int(media_idade)))
