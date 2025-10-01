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

#lista de numeros inteiros
numeros = [1, 2, 3, 4, 5]

#lista strings
frutas = ['maçã', 'banana', 'laranja']

#lista com dados de diferentes tipos
mista = [1, 'dois', 3.0, ['a', 'b', 'c']]

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


