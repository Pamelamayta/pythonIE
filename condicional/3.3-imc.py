# solicitando o peso altura ao usúario 
nome = input("digite seu nome: ")
peso = float(input("digite o peso em (kg): "))
altura = float(input("digite sua altura (m): "))

imc = peso / altura**2

# definindo o quadro do paciente sengundo o imc

if imc < 18.5:
    situacao = "abaixo do peso"
elif imc <= 24.9:
    situacao = "peso normal"
elif imc <= 29.9:
    situacao = "sobrepeso"
elif imc <= 34.9:
    situacao = "obesidade grau i"
elif imc <= 39.9:
    situacao = "obesidade grau ii"
else:
    situacao = "obesidade grau iii"

print(f"O (a) paciente {nome} tem seu imc {imc:.2f} e sua situação é {situacao} ")