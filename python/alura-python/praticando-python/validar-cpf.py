# Validação de CPF
def validar_cpf(cpf):
    
    # Remover pontos e traços
    if not cpf.isdigit():
        
        # retornar mensagem de erro
        return "Erro: O CPF deve conter apenas números."
    
    # se for diferente de 11, retornar mensagem de erro
    if len(cpf) != 11:
        
        # retornar mensagem de erro
        return "Erro: O CPF deve conter exatamente 11 dígitos."
    
    # retornar mensagem de sucesso
    return "CPF válido."

# Solicitar entrada do usuário
cpf = input("Digite seu CPF: ")

# imprimir resultado da validação
print(validar_cpf(cpf))

# o que faz o .isdigit()?
# verifica se todos os caracteres na string são dígitos (0-9) 
# e se a string não está vazia.