tabela = list()
for ico in range(1, 6):
    tabela.append(int(input('Digite um número: ')))
print(f'Os valores digitados foram {tabela}')
print(f'O maior valor é {max(tabela)} e está na posição {tabela.index(max(tabela))+1}.')
print(f'O menor valor é {min(tabela)} e está na posição {tabela.index(min(tabela))+1}.')

