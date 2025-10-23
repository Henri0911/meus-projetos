temp = float(input("Digite a temperatura atual: "))

if temp > 25:
    print(f"ALERTA! Temperatura acima do limite permitido.\n Valor da Temperatura {temp} ")
else:
    print(f"Temperatura dentro do limite seguro.\n Valor da Temperatura {temp}")