casa = float(input('Qual o valor da casa? R$ '))
salar = float(input('Qual o seu salário mensal? R$ '))
ano = int(input('Em quantos anos você pretende pagar? '))

if ano > 0:
    prazo = ano * 12
    prestacaomensal = casa / prazo
    limite = salar * (30 / 100)

    if prestacaomensal <= limite:
        print('Empréstimo aprovado!')
    else:
        print('Empréstimo negado!')

    print(f'Sua prestação mensal ficará em R$ {prestacaomensal:.2f}')
else:
    print('O prazo precisa ser maior que zero!')
