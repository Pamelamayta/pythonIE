#solicitando idade e se é estudante
idade = int(input("digite sua idade "))
estudante = input("você é estudante s/n ")

#validando meia entrada 
meia = (idade >= 60) or estudante == "s"

#aprsentando o resultado ao usúario 
print("tem direito a meia-entrada", meia )