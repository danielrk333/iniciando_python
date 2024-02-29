# EX 06
import math
def func_num():
    num = int(input('Insira um número inteiro: '))
    return 'Seu dobro é {} \n Seu triplo é {} \n Sua raiz quadrada é {:.2f}'.format(
        num*2, num*3, math.sqrt(num))

print(func_num())