soma_sexo_m = 0
soma_idade = 0
soma_mulheres_20 = 0
while True:
    print('-' * 30)
    print('CADASTRO PESSOA')
    print('-' * 30)

    idade = int(input('Digite sua idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper().strip()
    stop = str(input('Você deseja interromper [S/N]:')).upper().strip()
    if idade > 18:
        soma_idade +=1
    if sexo == 'M':
        soma_sexo_m += 1
    if sexo == 'F' and idade < 20:
        soma_mulheres_20 += 1
    if stop == "S":
        break
print(f'\033[35mTotal de pessoas com mais de 18 anos: {soma_idade}')
print(f'\033[35mTotal de homens cadastrados foi: {soma_sexo_m}')
print(f'\033[35mTotal de mulheres com menos de 20 anos é:{soma_mulheres_20}')