from datetime import datetime
dados = {}
ano = datetime.now().year
print('-=-' *30)
dados['nome'] = input('Nome: ')
dados['nasc'] = int(input('Ano de nascimento: '))
dados['ctps'] = int(input('Carteira de trabalho(0 não tem): '))
idade = ano - dados["nasc"]
if dados["ctps"] != 0:
    dados['ano_cont'] = int(input('Ano de contratação: '))
    dados['salario'] = int(input('salário: '))
    cont = ano - dados["ano_cont"]
    print(f'Nome tem o valor {dados["nome"]}')
    print(f'Idade tem valor {idade}')
    print(f'CTPS temo o valor de {dados["ctps"]} ')
    print(f'Contratado em {dados["ano_cont"]}')
    print(f'O salário é de {dados["salario"]}')
    print(f'Anos de contribuição {cont}')
else:
    print('\033[32m-=-\033[m' * 30)
    print(f'Nome tem o valor {dados["nome"]}')
    print(f'Idade tem valor {idade}')
    print(f'CTPS tem o valor de {dados["ctps"]} ')

