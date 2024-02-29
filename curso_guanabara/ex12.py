# EX 12

def preco_desconto():
    preco = float(input('Insira o valor atual do produto: '))
    print('O valor do produto com 5% de desconto é de {:.2f} reais'.format(
        preco - (preco*5/100)))


preco_desconto()