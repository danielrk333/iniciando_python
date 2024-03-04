import random


def sort_ordem():
    al1 = str(input('Primeiro aluno: '))
    al2 = str(input('Segundo aluno: '))
    al3 = str(input('Terceiro aluno: '))
    al4 = str(input('Quarto aluno: '))
    alunos = [al1, al2, al3, al4]
    print('A ordem de apresentação será, respectivamente: ')
    return random.shuffle(alunos)


print(sort_ordem())