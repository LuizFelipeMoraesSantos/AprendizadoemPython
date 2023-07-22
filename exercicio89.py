turma = []
while True:
    dados = []
    nome = input('Nome aluno: ')
    nota_1 = float(input("Nota primeiro semestre: "))
    nota_2 = float(input('Nota segundo semestre: '))
    dados.append(f'{nome},{nota_1},{nota_2}')
    turma.append(dados[:])
    perg = input('Deseja continuar[S/N]: ')
    if perg in 'Nn':
        break
for i,aluno in enumerate(turma):
    notas = (aluno[1] + aluno[2]) / 2
print(f'O aluno {aluno[0]} ficou com média {notas}')




