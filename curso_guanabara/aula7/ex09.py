# EX 09

def tabuada():
    entrada = int(input('Insira um número inteiro: '))
    print('A tabuada do {}: '.format(entrada))
    for i in range(11):
        print('{}x{} = {}'.format(entrada, i, entrada*i))

tabuada()