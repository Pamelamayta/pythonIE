#coletando renda e situação do corretista 
renda = float(input("digite sua renda mensal R$: "))
situacao = input("possui restrição / nome negativo (s/n): ")

#validando renda e situação de restrição
Emprestimo = (renda >=3000) and situacao =="n"

print("emprestimo aprovado: ", Emprestimo)
