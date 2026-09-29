#solicitar nome e a idade ao usuário 
nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

#criando uma condição caso for >= a 18 anos 
if  idade >= 18:
    possui_carteira = input("possui carteira de motorista s/n: ")
    if possui_carteira == "s":
        print("pode dirigir")
    else:
        print("não pode dirigir ")
else:
    print("menor de idade ")
