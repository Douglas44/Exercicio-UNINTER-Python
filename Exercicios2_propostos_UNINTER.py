'''
    Ajudinha para aqueles que estão realizando os exercícios da UNINTER.
    Caso fiquem perdidos, aqui está as resoluções das atividades propostas durante as aulas.
    (OBS: NÃO SÃO AS RESPOSTAS DAS PROVAS. ESTUDE PARA FAZER!!!)

    Linkedin: https://www.linkedin.com/in/douglas-costa-78983a228/
    GitHUB: https://github.com/Douglas44
    Instagram: https://www.instagram.com/doug_pessoal/
'''

# Exercise 1
lado1 = int(input('Informe o valor desse lado: '))
lado2 = int(input('Agora informe o valor desse lado: '))
lado3 = int(input('Informe o valor só mais desse lado: '))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    if lado1 < lado2+lado3 and lado2 < lado1+lado3 and lado3 < lado1+lado2:
        if lado1 == lado2 == lado3:
            print('Esse é um triângulo equilátero')

        elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
            print('Esse é um triângulo isósceles')

        elif (lado1 != lado2 and lado3) or (lado2 != lado1 and lado3) or (lado3 != lado1 and lado2):
            print('Esse é um triângulo escaleno')

    else:
        print('Isso não é um triângulo!')

else:
    print('Isso não é um triângulo!')


# Exercise 2
num1 = int(input('Informe um valor: '))
num2 = int(input('Informe outro valor: '))
print('='*15)
print('[+] Adição')
print('[-] Subtração')
print('[*] Multiplicação')
print('[/] Divisão')
print('='*15)
operacao = input('Selecione a operação que deseja realizar: ')

if operacao == '+':
    soma = num1+num2
    print('O resultado da operação de {} foi de: {}'.format(operacao, soma))
elif operacao == '-':
    subtracao = num1-num2
    print('O resultado da operação de {} foi de: {}'.format(operacao, subtracao))
elif operacao == '*':
    multiplicacao = num1*num2
    print('O resultado da operação de {} foi de: {}'.format(operacao, multiplicacao))
elif operacao == '/':
    divisao = num1/num2
    print('O resultado da operação de {} foi de: {}'.format(operacao, divisao))
else:
    print('Operação desconhecida. Tente novamente.')


# Exercise 3
kwh = int(input('Informe quantos kWh foram consumidos: '))
print('='*15)
print('[R] - Residência')
print('[I] - Industrial')
print('[C] - Comercio')
tipo_residencia = input('Informe o tipo de instalação: ').upper()

if tipo_residencia == 'R':
    if kwh <= 500:
        valor_pagar = kwh*0.40
    else:
        valor_pagar = kwh*0.65
    print('O valor a se pagar é de R${:.2f}'.format(valor_pagar))

elif tipo_residencia == 'I':
    if kwh <= 5000:
        valor_pagar = kwh*0.55
    else:
        valor_pagar = kwh*0.60
    print('O valor a se pagar é de R${:.2f}'.format(valor_pagar))


elif tipo_residencia == 'C':
    if kwh <= 1000:
        valor_pagar = kwh*0.55
    else:
        valor_pagar = kwh*0.60
    print('O valor a se pagar é de R${:.2f}'.format(valor_pagar))
