# criando maior numero
def maior_numero(x,y):
    if x > y:
        return x
    else:
        return y

numero_1 =float(input("digite um numero: "))
numero_2 =float(input("digite outro numero: ")) 

resultado =maior_numero(numero_1,numero_2)

#apresentando o maior numero
print(f"o maior numero digitado foi: {resultado}")