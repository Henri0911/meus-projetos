macas = int(input("Digite a quantidade de maçãs vendidas: "))
bananas = int(input("Digite a quantidade de bananas vendidas: "))

if macas > bananas:
    print(f"As maçãs tiveram mais vendas, quantidade: {macas}")
elif bananas > macas:
    print(f"As bananas tiveram mais vendas, quantidade: {bananas}")
else:
    print(f"As vendas foram iguais, {macas} maçãs e {bananas} bananas.")

