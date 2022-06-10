'''
    Ajudinha para aqueles que estão realizando os exercícios da UNINTER.
    Caso fiquem perdidos, aqui está as resoluções das atividades propostas durante as aulas.
    (OBS: NÃO SÃO AS RESPOSTAS DAS PROVAS. ESTUDE PARA FAZER!!!)

    Linkedin: https://www.linkedin.com/in/douglas-costa-78983a228/
    GitHUB: https://github.com/Douglas44
    Instagram: https://www.instagram.com/doug_pessoal/
'''

# Booleans Expressions - True or False
print(2 + 2 < 4)
print(7 // 3 == 1 + 1)
print((3**2) + (4**2) == 25)
print(2 + 4 + 6 > 12)
print(1387 % 19 == 0)
print(31 % 2 == 0)
print(min(34, 29, 31) < 30)

# Simple Condition
# a:
idade = int(input('Digite sua idade: '))
if idade > 60:
    print('Você tem direito aos benefícios')

# b:
dano = int(input('Digite o quanto de dano: '))
escudo = int(input('Digite o quanto de escudo: '))
if dano > 10 and escudo == 0:
    print('Você está morto!')

# c:
norte = False
sul = False
leste = True
oeste = False

if (norte == True) or (sul == True) or (leste == True) or (oeste == True):
    print('Você escapou!')


# Compost Condidional

# a:
ano = int(input('Digite um ano: '))
if ano % 4 == 0:
    print('Pode ser um ano bissexto')
else:
    print('Definitivamente não é um ano bissexto')

# b:
cima = True
baixo = False
if (cima == True) and (baixo == True):
    print('Decida-se!')
else:
    print('Você escolheu um caminho!')
