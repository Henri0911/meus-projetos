hora_atual = int(input("Digite a hora atual (Formato 24 horas): "))

if 8 <= hora_atual < 18:
    print(f"Acesso permitido. =)\n Hora Atual: {hora_atual}h")
else:
    print(f"Acesso negado. =(\n Hora Atual: {hora_atual}h")
