nome = input("digite seu nome   ")
email = input("digite seu email   ")

arquivo = open("pessoa.txt", "a")
arquivo.write(f"{nome} | {email} /n")
arquivo.close()

with open("pessoa.txt","a") as arquivo:
    arquivo.write(f"{nome} | {email} /n")