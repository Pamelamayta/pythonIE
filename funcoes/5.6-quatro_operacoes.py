def somar(x,y):
        return x + y
def subtrair(x,y):
        return x - y
def multiplcar(x,y):
        return x * y
def dividir(x,y):
    if x // y:
        return x / y
    
numero_1 =float(input("digite um numero: "))
numero_2 =float(input("digite outro numero: "))

resultado =somar(numero_1,numero_2)
resultado1 =subtrair(numero_1,numero_2)
resultado2 =multiplcar(numero_1,numero_2)
resultado3 =dividir(numero_1,numero_2)

print(f"o valor soma é {resultado}, subtracao é {resultado1}, a multuplicação é {resultado2} e a divisão é {resultado3}")

