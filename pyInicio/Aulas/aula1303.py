# Aula 13/03 - Cálculo de média

def media():
    valor1 = float(input('Insira a primeira nota: '))
    valor2 = float(input('Insira a segunda nota: '))
    valor3 = float(input('Insira a terceira nota: '))
    med = (valor1+valor2+valor3)/3
    return med

if media() >= 7:
    print('O aluno foi APROVADO')
else:
    print('O aluno foi REPROVADO')
