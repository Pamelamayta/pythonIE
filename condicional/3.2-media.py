nome = input("digite seu nome ")
nota_1 = float(input("digite primeira nota "))
nota_2 = float(input("digite segunda nota "))
nota_3 = float(input("digite terceira nota "))

#realizando a media do calculo 
media = (nota_1 + nota_2 + nota_3) / 3


if media < 4:
   situacao = "reprovado"
elif media <= 6:
    situacao = "recuperacao"
else:
    situacao = "aprovado parabens"

print(f"a media do aluno(a) {nome} é {media:.2f} e está {situacao}")