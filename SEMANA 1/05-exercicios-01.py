
# Exercicio 1:

nome = "Felipe Amaral da Luz"
email = "emailqualquer@gmail.com"
posição = email.find("@")
servidor = email[posição :]
nome_email = email[:posição]



# Mostre o servidor do email:

print(email.find("@"))
print(posição)
print(email[posição:])
print(servidor)


# Mostre o nome antes do @:
print(email[:posição])
print(nome_email)




# Mostre o 1º nome do usuario:

nome = "João da Silva Sasntos"
email = "joaodasilvasantos@gmail.com"
posição = nome.find(" ")
primeiro_nome = nome[:posição]

print(posição)
print(primeiro_nome)



# Construa uma mensagem: Usuario: 1º nome cadastrado com o email: 

print(f"Usuario: {primeiro_nome} cadastrado com o email: {email}")




# Construa uma mensagem: Enviamos um link para o email:


nome = "Joao da Silva Santos"
email = "joaodasilvasantos@gmail.com"
posição = email.find("@")
primeiro_nome = nome[:posição]
servidor = email[posição:]
primeira_letra = email[0]

print(primeira_letra)
print(servidor)

print(f"Enviamos um link de confirmação para o email: {primeira_letra}******{servidor}")



