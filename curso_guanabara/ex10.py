# EX 10

def conv_dolares():
    real = float(input('Quantos reais você pretende converter? '))
    return 'Você terá {:.2f} dólar(es)'.format(real/3.27)

print(conv_dolares())