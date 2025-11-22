faturamento = 1520 # variável tipo int > número inteiro.
custo = 483.50 # variável tipo float > ponto flutuante = numero c/ casas decimais.
imposto = faturamento * 0.10
lucro = faturamento - custo - imposto
margem_lucro = lucro / faturamento

print("o lucro mensal foi: R$", lucro)
print("o valor pago em imposto foi de: R$ ", imposto)
print("a margem de lucro foi de: ", round(margem_lucro, 2)) #round = numero de casas depois da vírgula (no caso 2).


# Operador Mod -> % = indica o resto de uma divisão.
print("Uso da variável Mod")
print("Mod é o resto da divisão")
print("Exemplo: 10 / 3 resto:")

resto = 10 % 3
print(resto)

#Exemplo: 170 meses são quantos anos?
Tempo_contrato = 170
print("Tempo de contrato total em meses:", Tempo_contrato)
tempo_anos = 170 / 12
print("Tempo em anos: ", int(tempo_anos)) #int = inteiro / para deixar o numero sem casas decimais.
# quantos meses sobram nessa conta?
tempo_meses = 170 % 12
print("Tempo restante em meses: ", tempo_meses)