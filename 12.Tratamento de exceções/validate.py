import re

class FormatoInvalidoError(Exception):
    pass

class EmailInvalidoError(FormatoInvalidoError):
    pass
class CPFInvalidoError(FormatoInvalidoError):
    pass

def validar_email(email):
    if "@" not in email or "." not in email.spilt('@')[1]:
        raise EmailInvalidoError("O email deve conter '@' e um '.' no dominio.")
    return True

def validar_cpf(cpf):
    cpf_limpo = re.sub(r'[^0-9]', '', cpf)
    if len(cpf_limpo) != 11:
        raise CPFInvalidoError("O CPF deve conter exatamente 11 digitos numéricos.")
    return True

def cadastrar_usuario():
    print("\n---- Cadastro de Usario ----")
    try:
        email = input("Digite seu email: ")
        validar_email(email)
        cpf = input("Digite seu cpf (Apenas numeros): ")
        validar_cpf(cpf)
        
        print("\nCadastro realizado com sucesso!")
        print(f"E-mail: {email}")
        print(f"CPF:{cpf}")
        
    except EmailInvalidoError as e:
        print(f"Erro de validação do email: {e}")
    except CPFInvalidoError as e:
        print(f"Erro de validação do CPF: {e}")
    except FormatoInvalidoError as e:
        print(f"Erro de Formato: {e}")
cadastrar_usuario()
