# Use of strings and concatenation of STRINGS
# first_name = "Daniel"
# last_name = "Lavorini"
# full_name = first_name + " " + last_name
# print(type(name))
# print("Hello, " + full_name)

# Use of int and concatenating a STRING with a INT using the + str(int)
# age = 17
# age += 1
# print("Your age is: " + str(age))
# print(type(age))

# Use of float and concatenating a STRING with a FLOAT
# height = 183.5
# print("Your height is: " + str(height) + "cm")
# print(type(height))

# Use of a boolean and concatenating a STRING with a BOOLEAN
# human = True
# print("Are you a human: " + str(human))
# print(type(human))


# Multiple assignment - assign multiple variables in 1 line

# name = "Daniel"
# age = 17
# lindo = True

# Applying the rule of multiple assignment...
# name, age, lindo = "Daniel", 17, True
# print(name)
# print(age)
# print(lindo)

# Pato = 15
# Galinha = 15
# Ganso = 15

# Applying the multiple assignment...
# Pato = Galinha = Ganso = 15
# print(Pato, Galinha, Ganso)


# String Methods

# name = "Daniel Lavorini"
# print(len(name))
# print(name.find("i"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(name.isalpha())
# print(name.count("i"))
# print(name.replace("o","!"))
# print(name*5)


# Type Casting - convert a data type of a value into another data type

# x = 1 #int
# y = 2.0 #float
# z = "3" #str

# Definitive type casting
# y = int(y)

# Type cast on the print command (not definitive)
# print("X is " + str(x))
# print ("Y is " + str(y))
# print("Z is " + str(z))


# User input

# name = input("What is your name? ")
# age = int(input("How old are you? "))
# height = float(input("How tall are you? "))

# print("Hello " + name)
# print("You are " + str(age) + " years old")
# print("You are " + str(height) + "cm tall")


# Math Functions

# import math
# pi = 3.14
# x = 1
# y = 2
# z = 3

# print(round(pi))    # arredonda
# print(math.ceil(pi)) # arredonda para mais
# print(math.floor(pi)) # arredonda para menos
# print(abs(pi))         # mostra o valor absoluto, sem ser positivo nem negativo
# print(pow(pi,2))        # eleva a variável ao quadrado por exemplo
# print(math.sqrt(pi))     # acha a raiz quadrada
# print(max(x,y,z))         # mostra o maior valor entre as variáveis citadas
# print(min(x,y,z))          # mostra o menor valor


# String slicing - create a substring by extracting elements from another string
# func. = indexing[] or slice() -> [start:stop:step]

# Indexing
# name = "Daniel Lavorini"
# first_name = name[:6] # ou [0:6]
# last_name = name[7:]  # ou [7:15]
# apelido = name[::3] # how to use the step, ou seja, quantas letras ele vai pular, 1 em 1, 2 em 2...
# reversed_name = name[ : :-1]

# print(first_name)
# print(last_name)
# print(reversed_name)

# Slice Func.
# website1 = "https://microsoft.com"
# website2 = "https://unifafibe.com"

# slice = slice(8,-4)
# print(website1[slice])
# print(website2[slice])


# IF Statement
# age = int(input("How old are you? "))

# if age == 100:
# print("You are a century old!")
# elif age >= 18:
# print("You are an adult!")
# elif age < 0:
# print("You haven´t been born yet!")
# else:
# print("You are a minor!")


# Logical operators (and, or)

# temp = int(input("Quantos graus está fazendo hoje? "))

# if temp < 0 or temp > 29:
# print("O tempo está péssimo! Mantenha-se dentro de casa.")
# elif temp >= 0 and temp <= 18:
# print("Está frio hoje")
# print("Busque um agasalho!")
# else:
# print("A temperatura está boa e amena")
# print("Vá viver a vida!")


# While loops = execute it's block of code as long as the condition stays true

# name = "" # or None
# while len(name) == 0: # or while not name:
# name = input("Enter your name: ")
# print("Hello, welcome " + name.capitalize())


# For loops = it execute it's blocks of code a limited amount of times
#               While loop -> unlimited
#               For loop -> limited
# import time

# for count in range(10):
#    print(count+1)
# for count in range(0,10+1,2):
#    print(count)
# for count in "Daniel Lavorini":
#    print(count)
# for segundos in range(10,0,-1): #-1 para contagem regressiva
#    print(segundos)
#    time.sleep(1) # é o que conta os segundos
# print("FELIZ ANO NOVOO!")


# Nested loops

# linhas = int(input("Quantas linhas seu retângulo terá? "))
# colunas = int(input("Quantas colunas seu retângulo terá? "))
# simbolo = input("Insira um símbolo para usar: ")

# for i in range(linhas):
#    for j in range(colunas):
#        print(simbolo, end="")
#    print()


# Loop Control Statemets -> break == terminate the loop entirely
#                           continue == skips and forces the loop to start at the next iteration
#                           pass == means there is no code to execute here, and continue

# while True:
#    name = input("Enter your name: ")
#    if name != "":
#        break

# phone_number = "17-98840-0664"
# for i in phone_number:
#    if i == "-":
#        continue
#    print(i, end="")

# for i in range(1,21):
#    if i == 13:
#        pass
#    else:
#        print(i, end=",")


# List = used to store multiple items in a single variable

# food = ["pizza", "hamburguer", "hotdog", "macarrão"]
# food[0] = "sushi"
# food.append("sorvete")
# food.remove("hotdog")
# food.pop()
# food.insert(2, "açaí")
# food.sort()
# food.clear()
# print(food[0])
# for x in food:
#    print(x)


# 2D Lists

#drinks = ["caipirinha", "soda italiana", "coca"]
#jantar = ["pizza", "lasanha"]
#sobremesa = ["pavê", "sorvete", "muçyr"]
#comida = [drinks, jantar, sobremesa]

#print(comida[2][2])


# Tuple = semelhante a listas, porém são imutáveis

#student = ("Daniel", 17, "Masculino")
#print(student.count("Daniel"))
#print(student.index("Masculino"))

#for i in student: # prints all the tuple elements
#    print(i)

#if "Daniel" in student:
#    print("Presente")


# Sets = uma coleção que não tem ordem ou index e não aceita valores duplicados

#utensilios = {"garfo", "faca", "colher", "copo"}
#loucas = {"prato", "copo", "tapuer"}

#utensilios.add("pano de prato")
#utensilios.remove("garfo")
#utensilios.clear()
#utensilios.update(loucas)
#mesa_de_jantar = utensilios.union(loucas)

#print(loucas.difference(utensilios))
#print(utensilios.intersection(loucas))

#for i in mesa_de_jantar:
#    print(i)


# Dictionary = uma coleção desordenada e mutável de pares de chaves:valores

#capitais = {"Brasil":"Brasília",
#            "India":"Nova Delhi",
#            "Coréia do Sul":"Seoul",
#            "Argentina":"Buenos Aires"}
#capitais.update({"Alemanha":"Berlim"})  #adiciona
#capitais.update({"Brasil":"Fortaleza"})  #atualiza item existente
#capitais.pop("Argentina")  #remove um item inteiro
#capitais.clear()  #limpa tudo

#print(capitais["India"]) # ruim pq da erro se inserir alguma chave não existente na coleção
#print(capitais.get("Russia")) # melhor para acessar o valor da chave, caso insira uma chave que não exista, ele não dá erro como no print acima
#print(capitais.keys())
#print(capitais.values())
#print(capitais.items())

#for key,value in capitais.items():
#    print(key,"/",value)


# Index operator []

#name = "daniel Lavorini!"

#if (name[0].islower()):
#    name = name.capitalize()

#first_name = (name[0:6].capitalize())
#last_name = (name[7:].upper())
#last_character = name[-1]
#print(first_name)
#print(last_name)
#print(last_character)


# Functions = a block of code which is executed only when is called
#import datetime
#def greetings(first_name,last_name,age):
#    print("Hello! Nice to meet you, " + first_name + " " + last_name)
#    print("You are " + str(age) + " years old")
#    print(datetime.datetime.now())

#greetings("Daniel", "Lavorini",17)


# Return Statement = return the results of a function back to the caller

#def multiply(num1,num2):
#    return  num1 * num2

#r = multiply(7,5)
#print(r)


# Keyword arguments = igual um argumento posicional, porém neste a ordem não importa, pq atribuimos um identificador ao parametro da func.

#def hello(first,middle,last):
#    print("Hello, " + first + " " + middle + " " + last)


#hello(middle="Niel", first="Daniel", last="Lavorini")


# Nested function calls = chamadas de funções dentro de outras chamadas funções
#print(round(abs(float(input("Enter a whole positive number: ")))))


# Variable scope = a variable that is only avaliable inside the region that is creates, like inside a function
#name = "Lavorini" # variavel global
#def display_name():
#    name = "Daniel" # variavel local
#    return name

#print(display_name())
#print(name)


# Args = a parameter that pack all the arguments of a func. into a tuple, so it can accept varying amount os args

#def soma(*args):
#    adc = 0
#    for i in args:
#        adc += i
#    return adc

#print(soma(8,569, 854, 7632, 9814))


# Kwargs = like args but'll pack the arguments into a dictionary // a ordem dos args. na chamada da func. IMPORTA

#def oi(**kwargs):
#    print("Hello", end=" ")
#    for key,value in kwargs.items():
#        print(value, end=" ")
#oi(first="Daniel", last="Lavorini")





