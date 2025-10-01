'''
frase = input("Digite uma frase: ")

# dividir a frase em palavras
#.split() divide a string em uma lista de palavras
palavras = frase.split()

# contar o número de palavras
# len() retorna o número de itens em um objeto
contador = len(palavras)

print(palavras)'''

# aprimorado
# função limpar texto
def limpar_texto(texto):

    # converter para minúsculas
    texto = texto.lower()

    # remover pontuação
    caracteres = ",.!|?;:\"'()[]{}"

    # para cada caractere na string de caracteres
    for char in caracteres:

        # substituir o caractere por vazio
        texto = texto.replace(char, "")

    # retorna o texto limpo    
    return texto

# função contar palavras
def contar_palavras(frase):

    # limpar a frase
    frase = limpar_texto(frase)

    # verificar se a frase está vazia
    if not frase.strip():

        # retornar 0
        return {}

    # dividir a frase em palavras
    palavras = frase.split()

    # dicionário para armazenar a contagem de palavras
    contagem = {}

    # contar a ocorrência de cada palavra
    for palavra in palavras:

        # incrementar a contagem da palavra no dicionário
        contagem[palavra] = contagem.get(palavra, 0) + 1
        
        # contagem[palavra] = contagem.get(palavra, 0) + 1
        return contagem

    '''
    # imprimir a lista de palavras
    print(palavras)

    # retornar o número de palavras
    return len(palavras)'''



