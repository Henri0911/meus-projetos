valor = float(input("Qual o valor da conta? R$ "))
porcentagem = int(input("Qual a porcentagem da gorjeta? "))

gorjeta = valor * (porcentagem / 100)
total = valor + gorjeta
print(f"\nValor da gorjeta: R$ {gorjeta:.2f}")
print(f"Total a pagar: R$ {total:.2f}")

