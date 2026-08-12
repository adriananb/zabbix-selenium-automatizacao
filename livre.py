print ("Bem vindo a Eletrica Vivi e Cia, como você se chama?")
nome = input()
print (f"Olá, {nome}! É um prazer te conhecer. Como posso te ajudar hoje?")
ajuda = input()
print (f"Entendi, {nome}. Referente {ajuda}.")  
if "luz" in ajuda.lower() or "energia" in ajuda.lower():
    print ("Em caso de falta de luz, você deve entrar em contato com a companhia elétrica. Obrigado por entrar em contato conosco, até mais!")
print (f"Antes de começarmos, {nome}, preciso saber seu CEP sobre o local de atendimento.")
cep = input().strip()
print (f"Entendi, {nome}. Você informou o CEP: {cep}, está correto?")
if input().lower() in ['sim', 's']:
    cep_base = "09176-160"
    print (f"Somos de Santo André, infelizmenteatendemos regiões dentro de um raio de até 30 quilômetros.")
    if cep != cep_base:
        print ("Infelizmente não atendemos sua região, agradecemos pelo contato!")
        raise SystemExit
    print ("Agora, por favor, informe a distância em quilômetros até Santo André.")
    distancia_km = float(input())
    if distancia_km > 30:
        print ("Infelizmente não atendemos sua região, agradecemos pelo contato!")
        raise SystemExit
    else:
        print ("Ótimo, atendemos sua região!")
    print (f"Perfeito, {nome}. Agora, por favor, me informe o endereço completo para o atendimento.")
    endereco = input()
    print (f"Ótimo, {nome}. O endereço informado é: {endereco}. Está correto?")
    if input().lower() in ['sim', 's']:
        print (f"Excelente, {nome}. Em breve iremos te retornar para informar sobre a disponibilidade do atendimento no endereço fornecido. Enquanto isso, segue abaixo as instruções para o atendimento.")
        print ("Muito obrigado por fornecer todas as informações. Estamos ansiosos para atendê-lo!")
    else:
        print (f"Vamos corrigir o {cep}. Por favor, informe novamente o endereço completo.")
        print (f"Vamos corrigir o {endereco}. Por favor, informe novamente o endereço completo.")