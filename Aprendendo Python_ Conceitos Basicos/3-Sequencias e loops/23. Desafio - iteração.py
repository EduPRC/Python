# Dado uma sequência de números, calcule a soma e média dos números.
# ATENÇÃO: não vale usar a função sum() !

numeros = [10,2,3,4,5]

soma = 0
for n in numeros:
    soma = n + soma

media = soma / len(numeros)
print("\n")
print(f"A soma de {numeros} é {soma}")
print(f"A média de {soma} é {media}")
print("\n\n\n")

# Dado uma sequência de números, calcule o maior valor da sequência.
# ATENÇÃO: não vale usar a função max() !

numeros = [10,2,3,4,5]

maximo = numeros[0]
for n in numeros:
    if n > maximo:
        maximo = n

print(f"O maior numero da lista {numeros} é o {maximo}")

minimo = numeros[0]
for n in numeros:
    if n < minimo:
        minimo = n

print(f"O menor numero da lista {numeros} é o {minimo}")
print("\n\n\n")

# Dado uma lista de palavras, printe todas as palavras
# com pelo menos 5 caracteres.

palavras = ["avon", "boticario", "caneca", "garrafa"]

for p in palavras:
    if len(p) >= 5:
        print(p)

print("\n\n\n")

