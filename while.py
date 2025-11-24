# --------- WHILE ----------

#Exemplo 1:

# numero = 1

# while numero <= 20:
#     print("Numero: ", numero)
#     numero += 1

# print()


#Exemplo 2:

# numero = 1

# valor = 20

# while numero <= valor:
#     print("Numero: ", numero)
#     numero += 1

# print()

#Exemplo 3:

# numero_usuario = 1

# somatoria = 0

# indice = 0

# while numero_usuario != 0:
#     numero_usuario = int(input("Digite um numero: "))
#     if numero_usuario == 0:
#         break

#     somatoria += numero_usuario
#     indice += 1

#     print(f"\nno loop {indice}º a somatoria é: {somatoria}\n")

# print (f"\nA somatoria dos numeros digitados é: {somatoria}\n")



#Exemplo 4:

total = 0
indice = 0

numero = int(input("Digite um número: "))
total += numero

while (total <= 100):
    numero = int(input("Digite um número: "))
    total += numero
    indice += 1

print(f"No {indice}º loop o total excedeu o limite de 100 somando: {total}")