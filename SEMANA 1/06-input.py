
# Input texto:

nome = input("Digite aqui seu nome: ")
email = input("Digite aqui seu email: ")

posição_nome = nome.find(" ")
primeiro_nome = nome[:posição_nome]
posição_email = email.find("@")
servidor = email[posição_email:]
primeira_letra = email[0]

print(f"\nUsuario: {primeiro_nome} cadastrado com o email: {email}\n")

print(f"Enviamos um link de confirmação para o email: {primeira_letra}******{servidor}\n")




# Input Numeros:

# Bonus -> 1% das vendas

vendas = input("Digite suas vendas: ")
vendas = float(vendas) * 0.01 # Bonus de 1% = 0,01

print(vendas)


# *** tenha o cuidado de usar "float" para converter "strings" em numeros decimais

vendas_dia1 = input("Digite suas vendas do dia 1: ")
vendas_dia2 = input("Digite suas vendas do dia 2: ")
total_de_vendas = float(vendas_dia1) + float(vendas_dia2)
bonus = total_de_vendas * 0.01


print(f"\nO total de vendas foi: {total_de_vendas}")

print(f"Bonus: {bonus}\n")



# ----------- OU ---------

# Use o float já no "input": 

vendas_dia1 = float(input("Digite suas vendas do dia 1: "))
vendas_dia2 = float(input("Digite suas vendas do dia 2: "))
total_de_vendas = (vendas_dia1) + (vendas_dia2)
bonus = total_de_vendas * 0.01


print(f"\nO total de vendas foi: {total_de_vendas}")

print(f"Bonus: {bonus}\n")