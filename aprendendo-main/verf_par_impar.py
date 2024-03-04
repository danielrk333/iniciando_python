# Identificador de número par/ímpar

def ident():
    entrada = input("Insira um número inteiro: ")
    x = float(entrada)
    verf = x / 2
    if verf.is_integer():
        print("Este número é PAR")
    else:
        print("Este número é ÍMPAR")


while not ident():
    ident()
