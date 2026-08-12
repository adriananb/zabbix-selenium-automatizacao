print('Bem Vindo ao Calculo do IMC!')
print('Aqui você sabe se é gordo ou magro com humor!')

nome = input('Digite seu nome: ')
print('Olá, ' + nome + '!')
idade = int(input('Digite sua idade: '))
if idade >= 18:
    print('Você é maior de idade e já pode responder criminalmente pelos bolinhos roubados!')
else:
    print('Você é menor de idade e nem deveria estar aqui!')

altura = float(input('Digite sua altura: ').replace(',', '.'))
print('Ah ' + str(altura) + '!')
if altura >= 1.65:
    print('Você não é nem baixo e nem alto!')
else:
    print('Parabéns você não está longe do chão, então se cair, não se machuca !')

peso = float(input('Digite seu peso: ').replace(',', '.'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você é magro!')
elif imc <= 25:
    print('É, até que está bom. Seu coração agradece')
elif imc <= 30:
    print('Você está acima do peso, largue o bolinho!')
elif imc <= 35:
    print('Você está convidado para o quadro Quilos Mortais!') 