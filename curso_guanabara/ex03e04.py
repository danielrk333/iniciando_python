# Uso do print.format
num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))
soma = num1 + num2
print('O resultado da soma entre {} e {} é {}'.format(num1, num2, soma))
soma = str(soma)
print('A classe deste resultado é {}'.format(type(soma)), # preciso pular linha a cada argumento, mas não consegui usar o end='\n'
      'O resultado é letra? {}'.format(soma.isalpha()),
      'O resultado é número? {}'.format(soma.isnumeric()),
      'O resultado é decimal? {}'.format(soma.isdecimal()),
      'O resultado é identificador? {}'.format(soma.isidentifier())
      )

