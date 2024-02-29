# EX 05
def most_num():
    num = int(input('Insira um número inteiro: '))
    return 'Seu antecessor é {} \n Seu sucessor é {}'.format(num-1,num+1)
#   OU... print('Seu antecessor é {} \n Seu sucessor é {}'.format(num-1, num+1))

print(most_num())