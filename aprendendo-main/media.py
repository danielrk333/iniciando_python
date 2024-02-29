# Cálculo de média

def notas():
    nota1 = float(input("Insira a primeira nota: "))
    nota2 = float(input("Insira a segunda nota: "))
    nota3 = float(input("Insira a terceira nota: "))
    soma = nota1+nota2+nota3
    resultado = float(soma/3)
    if resultado >= 7.0:
        print("Aprovado")
    else:
        print("Reprovado")

notas()