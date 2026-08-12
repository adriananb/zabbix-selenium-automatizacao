nome = 'Drika'
idade = 35
altura = 1.65
peso = 79.5


nome = input('Digite seu nome: ')


if nome == 'Drika':
    print('Olá, Drika! Seja bem vinda!')
else:
    print('Olá ' + nome + '! Seja bem vindo(a)!')

idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você é maior de idade!')
else: 
    print('Você é menor de idade!')
altura = float(input('Digite sua altura: ').replace(',', '.'))
if altura >= 1.65:
    print('Você é esta na média!')
else: 
    print('Você não tem essa altura!')

peso = float(input  ('Digite seu peso: ').replace(',', '.'))
if peso >= 80:
    print('Você está acima do peso!')
else: print('Para estar no peso ideal, você precisa pesar até 65kg!')