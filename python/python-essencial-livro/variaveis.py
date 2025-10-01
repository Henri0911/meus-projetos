nome = "João"
idade = 30

nome = "Maria"
idade = 35
print("Meu nome é", nome, "e tenho", idade, "anos.")

x = 10      #int
y = 3.14    #float

#int    => inteiro
#float  => real

#string delimitada por aspas duplas
frase1 = "Olá, Python!"

#string delimitada por aspas simples
frase2 = "Olá, Python!"

#string de multiplas linhas delimitada por 3 aspas duplas
frase3 = """Este é um texto com
            múltiplas linhas. Você deve
            usar 3 aspas duplas para delimitar
            o ínicio e o fim da string"""

a = True
b = False
print(type(a)) #saída: <class 'bool'>

print("***listas***")

#lista de numeros inteiros
numeros = [1, 2, 3, 4, 5]

#lista strings
frutas = ['maçã', 'banana', 'laranja']

#lista com dados de diferentes tipos
mista = [1, 'dois', 3.0, ['a', 'b', 'c']]

print("***dicionarios***")

#criando um dicionario com pares chave-valor
pessoa = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

#acessando um valor pela sua chave
print(pessoa['nome']) #saída: 'João'

#alterando o valor associado a uma chave
pessoa['idade'] = 31
print(pessoa['idade']) #saída: 31

#adicionando um novo par de chave:valor
pessoa['pais'] = 'Brasil'
print(pessoa)
#saída: {'nome': 'João', 'idade': 31, 'cidade': 'São Paulo', 'pais': 'Brasil'}

del pessoa['cidade']
print(pessoa)
#saída: {'nome': 'João', 'idade': 31, 'pais': 'Brasil'}

print("***conjuntos***")

#criacao de conjutos
conjunto1 = {1, 2, 3, 4, 5}
print(conjunto1) #saída: {1, 2, 3, 4, 5}

#o que é uma lista set?
#é uma coleção não ordenada de elementos únicos.
#criacao de um conjunto a partir de uma lista set
conjunto2 = set([1, 2, 3, 4, 5])
print(conjunto2) #saída: {1, 2, 3, 4, 5}

conjunto3 = {1, 2, 3, 4}
conjunto4 = {3, 4, 5, 6}

#união
print(conjunto3 | conjunto4) #saída: {1, 2, 3, 4, 5, 6}
#pega todos os elementos dos dois conjuntos, sem duplicatas

#intersecao
print(conjunto3 & conjunto4) #saída: {3, 4}
#pega somente os elementos que estão em ambos os conjuntos

#diferença
print(conjunto3 - conjunto4) #saída: {1, 2}
#pega os elementos que estão no conjunto3 mas não estão no conjunto4

#diferença simétrica
print(conjunto3 ^ conjunto4) #saída: {1, 2, 5, 6}
#pega os elementos que estão em um dos conjuntos, mas não em ambos

print("***tuplas***")

#tuplas vazias
tupla_vazia = ()
print(tupla_vazia) #saída: ()

#tupla com elementos
tupla = 1, 2, 3, 4
print(tupla) #saída: (1, 2, 3, 4)

#tupla com elementos delimitados por parênteses
tupla2 = (1, 2, 3, 4)
print(tupla2) #saída: (1, 2, 3, 4)

#acessando elementos da tupla
tupla3 = (1, 2, 3, 4)
print(tupla3[0]) #saída: 1
print(tupla3[-1]) #saída: 4

#tuplas com elementos de diferentes tipos
tupla4 = (1, 2, 'três', 4.0, True)
print(tupla4) #saída: (1, 2, 'três', 4.0, True)
#tuplas são imutáveis, ou seja, não podem ser alteradas após a criação

print("***Operadores de tuplas***")

#fatiamento de tuplas
tupla5 = (1, 2, 3, 4, 5)
print(tupla5[1:3]) #saída: (2, 3)
print(tupla5[:-2]) #saída: (1, 2, 3)

#desempacotamento de tuplas
tupla6 = (1, 2, 3)
a, b, c = tupla6
print(a) #saída: 1
print(b) #saída: 2
print(c) #saída: 3

#concatenação de tuplas
tupla7 = (1, 2, 3)
tupla8 = (4, 5, 6)
tupla_concatenada = tupla7 + tupla8
print(tupla_concatenada) #saída: (1, 2, 3, 4, 5, 6)

#funções nativas
tupla9 = (1, 2, 3, 4, 5)
print(len(tupla9)) #saída: 5
#len retorna o número de elementos na tupla

print(min(tupla9)) #saída: 1
#min retorna o menor valor da tupla

print(max(tupla9)) #saída: 5
#max retorna o maior valor da tupla

print(sum(tupla9)) #saída: 15
#sum retorna a soma dos elementos da tupla

print("***Operadores Matemáticos***")





