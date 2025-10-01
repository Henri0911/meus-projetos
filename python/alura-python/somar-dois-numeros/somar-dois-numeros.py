# ****modo simples****
# Leia dois números do usuário e imprima a soma deles
'''num1 = float(input())
num2 = float(input())

soma = num1 + num2
print(soma)'''

# ****melhorando código****
# encapsulando em função
'''def somar(a, b):
    return a + b

numero1 = float(input('Digite o primeiro número: '))
numero2 = float(input('Digite o segundo número: '))

resultado = somar(numero1, numero2)
print(f"A soma é: {resultado}")'''

# ****adicionando tratamento de erro****
# usando try e except para tratar erro de valor inválido
def somar(a, b):
    return a + b
try:
    numero1 = float(input('Digite o primeiro número: '))
    numero2 = float(input('Digite o segundo número: '))

    resultado = somar(numero1, numero2)
    print(f"A soma é: {resultado}")
except ValueError:
    print("Por favor, digite apenas números válidos.")
