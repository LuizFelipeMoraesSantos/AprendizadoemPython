valor_imovel = float(input('Valor do imóvel: '))
salario = float(input('Qual a sua renda mensal: '))
parcela = int(input('Dividido em quantos anos: '))
mensal = parcela * 12
pago_por_mes = valor_imovel / mensal
salario_30 = salario * (30/100)

if pago_por_mes <= salario_30:
    print(f'O valor do imovél é R$ {valor_imovel} dividido em {parcela} anos no valor de R$ {mensal} ')
    print('Aprovado!!')
else:
    print('Infelizmente o Banco não autorizou sua compra.')
