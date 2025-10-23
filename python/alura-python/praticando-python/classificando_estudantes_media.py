nota1 = float(input("Digite a primeira nota "))
nota2 = float(input("Digite a segunda nota "))
nota3 = float(input("Digite a terceira nota "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print(f"Aprovado.\n Nota:{media:.2f}")
elif 5 <= media < 7:
    print(f"Recuperação.\n Nota:{media:.2f}")
else:
    print(f"Reprovado.\n Nota:{media:.2f}")

