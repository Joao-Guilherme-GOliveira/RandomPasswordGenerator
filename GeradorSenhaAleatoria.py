import random
import string

def perguntar_tipos():
    incluir_maiusculas = input("Deseja incluir letras maiusculas?(S/N):").strip().upper() == "S"
    incluir_minusculas = input("Deseja incluir letras minusculas?(S/N):").strip().upper() == "S"
    incluir_numeros = input("Deseja incluir numeros?(S/N):").strip().upper() == "S"
    incluir_simbolos = input("Deseja incluir caracteres especiais??(S/N):").strip().upper() == "S"
    return incluir_maiusculas,incluir_minusculas,incluir_numeros,incluir_simbolos
def main():
    tamanho_senha = int(input("Digite o tamanho da sua senha:"))
    
    maiusculas,minusculas,numeros,simbolos = perguntar_tipos()

    caracteres_possiveis = ""
    if maiusculas:
        caracteres_possiveis += string.ascii_uppercase
    if minusculas:
        caracteres_possiveis += string.ascii_lowercase
    if numeros:
        caracteres_possiveis += string.digits
    if simbolos:
        caracteres_possiveis += string.punctuation

    if not caracteres_possiveis:
        print("Voce precisa incluir pelo menos um tipo de caractere.")
        return

    senha = ""
    for i in range(tamanho_senha):
        senha+=random.choice(caracteres_possiveis)

    print(senha)

if __name__=="__main__":
    main()