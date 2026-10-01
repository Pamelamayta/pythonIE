lista_inicial = ["João", "Pamela", "Dominique"]

print("lista_inicial: " ,lista_inicial)
print(80 * "-")

lista_inicial.append("Eduarda")
print("apos append", lista_inicial)
print(80 * "-")

lista_inicial.insert(0,"Matheus")
print("apos insert()" , lista_inicial)
print(80 * "-")

lista_inicial[1] = "nycolas"
print("apos modificações" , lista_inicial)
print(80 * "-")

del lista_inicial[1]
print("apos del" , lista_inicial)
print(80 * "-")

lista_inicial.remove("Eduarda")
print("apos remove" , lista_inicial)
print(80 * "-")

removido = lista_inicial.pop(0)
print(f"apos pop, removido {removido}", lista_inicial)
print(80 * "-")