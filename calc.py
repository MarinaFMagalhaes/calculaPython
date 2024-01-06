def soma(n1, n2):
    return n1+n2

def sub(n1, n2):
    return n1-n2

def mult(n1, n2):
    return n1*n2

def div(n1, n2):
    if n2==0:
        return "Não pode haver divisão por zero."
    else:
     return n1/n2
#Dica: faça um laço while para o menu

x = 1
while x == 1:
    print(f'Digite 1 para sair \nDigite 2 para somar')
    opc = input("Digite o que deseja: ")
    if opc == "1":
        x = 3
    if opc != "1":
        texto()
        