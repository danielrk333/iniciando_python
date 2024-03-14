# Verificação de números pares e ímpares

def ver_par_impar():
    num = int(input('Digite um número inteiro: '))
    div = num/2
    return div.is_integer()


if ver_par_impar() == True:
    print('O número é PAR!')
else:
    print('O número é ÍMPAR')
