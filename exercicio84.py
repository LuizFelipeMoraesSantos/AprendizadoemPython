dados = []
pessoas = []
tot_cadastro = 0
maior = menor = 0
while True:
    dados.append(input('Digite seu nome: '))
    tot_cadastro += 1
    dados.append(float(input('Digite seu peso: ')))
    pessoas.append(dados[:])
    escolha = input("Deseja continuar[S/N]: ").upper().split()[0]
    dados.clear()

    if escolha in "Nn":
        print('\033[31mPrograma encerrado\033[m!')
        break
    menor = maior = pessoas[0][1]
    for pesos in pessoas:
        if pesos[1] >= maior:
            maior = pesos[1]
        if pesos[1] <= menor:
            menor = pesos[1]
print(f'o menor peso é de {menor}')
print(f'O maior peso é de {maior}')


print(f'O total de pessoas cadastradas foram {tot_cadastro}')




