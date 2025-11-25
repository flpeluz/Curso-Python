faturamento = 1000
custo = 200
lucro = faturamento - custo
margem = lucro / faturamento

print(f"O faturamento foi: R$ {faturamento:,.2f}\n"
      f"O custo foi: R$ {custo:,.2f}\n"
      f"O lucro foi: R$ {lucro:,.2f}")

# f = para formatação
# \n = Enter -> pula uma linha

# para formatação finaceira: 
# (,) = separação de milhar
# (.) = para a virgula (decimal)
# (2) = para duas casas decimais
# (f) = para float (numeros decimais)

print(f"A Margem de lucro foi: {margem:.0%}")

# para porcentagem:
# (0) = para não ter casa decimal
# (%) = para o %