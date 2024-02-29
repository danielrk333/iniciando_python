# EX 07
def media():
    aluno = input('Digite o nome do aluno: ')
    nota1 = float(input('Insira a primeira nota: '))
    nota2 = float(input('Insira a segunda nota: '))
    media = (nota1 + nota2) / 2

    return 'O aluno {} detém a média {}'.format(aluno, media)


print(media())
