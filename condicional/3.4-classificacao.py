nome = input("digite seu nome: ")
idade = int(input("digite sua idade: "))

if idade < 3:
    situacao = "bebe"
elif idade <= 10:
    situacao = "criança"
elif idade <= 14:
    situacao = "adolecente"
elif idade <= 30:
    situacao = "jovem"
elif idade <= 64:
    situacao = "adulto"
else:
    situacao = "vintage"
print(f" O usuario {nome} é {situacao}")