# importar função contar_palavras do módulo contador
from contador import contar_palavras
'''
# solicitar frase ao usuário
frase = input("Digite uma frase: ")
quantidade = contar_palavras(frase)
print(f"A frase tem {quantidade} palavras.")'''

# solicitar frase ao usuário
frase = input("Digite uma frase: ").strip()

# verificar se a frase está vazia
if not frase:

    # informar que a frase está vazia
    print("A frase está vazia.")

# se não estiver vazia
else:

    # chamar a função contar_palavras
    resultado = contar_palavras(frase)

    # imprimir o resultado
    if resultado:

        # imprimir a contagem de palavras
        print("Contagem de Palavras:")

        # para cada palavra e sua quantidade no dicionário resultado
        for palavra, quantidade in resultado.items():

            # imprimir a palavra e sua quantidade
            print(f"{palavra}:{quantidade}")

    # se o dicionário estiver vazio        
    else:

        # informar que a frase não contém palavras
        print(f"Nenhuma palavra válida foi encontrada.")



