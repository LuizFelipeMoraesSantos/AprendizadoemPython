cont = 0
maior_idade = 0
menor_idade = 0
for cont in range(0, 7):
    cont += 1
    idade =  int(input('Digite sua idade: '))
    if idade >= 18:
        maior_idade = maior_idade + 1
    else:
        menor_idade = menor_idade + 1
print(f'foram somadas {cont} e {maior_idade} pessoas são maior de idade e {menor_idade} são menores.')