sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidos! por favor informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))


#como eu fiz.
'''sexo = ''
masc = 'M'
fem = 'F'
while sexo == 'M' or 'F':
    sexo = str(input('Digite seu sexo [M/F]: ')).upper()
    if sexo == 'M':
        print('Seu sexo é Masculino') 
        break
    if sexo == 'F':
        print('Seu sexo é feminino.')
        break
    if sexo != masc or fem:
        print('Sexo inexistente')
        print('Digite novamente!')'''





