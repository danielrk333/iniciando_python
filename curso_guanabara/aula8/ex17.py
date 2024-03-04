import math


def hipotenusa():
    cat_op = float(input('Insira o cateto oposto para calcular: '))
    cat_adj = float(input('Insira o cateto adjacente: '))
    return 'O comprimento da hipotenusa é de {:.2f}'.format(math.hypot(cat_op, cat_adj) )


print(hipotenusa())