email = "email.qualquer@gmail.com"

print(email)

# ----- FUNÇÕES EM TEXTO ------
print(email.lower()) # .lowe() -> deixa tudo minúsculo
print(email.find("@")) # .find -> encontra a posição (indice) dentro de um texto | indice inicia sempre em 0

print(email[14]) # mostra o que contém no indice entre [] dentro da variavel texto

posicao = email.find("@") # define a posição encontrada no texto
servidor = email[posicao :] # define o texto posterior a posição
nome_email = email[: posicao] # define o texto anterior a posição

print(servidor) # mostra o texto posterior a posição
print(nome_email) # mostra o texto anterior a posição


print(len(email)) # len() -> mostra o tamanho do texto, ou seja quantos caracteres o texto possui

tamanho = len(email)
print(tamanho)

novo_email = email.replace("gmail.com", "hotmail.com") # .replace() -> troca trechos do texto
print(novo_email)

nome = "felipe luz"
print(nome.capitalize()) # .capitalize() -> deixa a primeira letra maiúscula
print(nome.title()) # .title() -> deixa Todas as PRIMEIRAS letras maiúsculas