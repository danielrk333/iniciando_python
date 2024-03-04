# EX 16
import math


def mostrar_int():
    entrada = float(input('Insira um número qualquer para mostrar seu valor inteiro: '))
    return 'O valor inteiro de {} é de {}'.format(entrada, math.trunc(entrada))


print(mostrar_int())
