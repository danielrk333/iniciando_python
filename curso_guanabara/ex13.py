# EX 13

def salario_aumento():
    salario_base = float(input('Digite o salário atual do funcionário: '))
    return 'O salário de R${:.2f} do funcionário com 15% de aumento resulta em R${:.2f}'.format(
        salario_base, salario_base + (salario_base*15/100))


print(salario_aumento())