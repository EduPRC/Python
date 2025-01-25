# Dado duas listas, printe todos os valores que aparecerem
# duplicados nas duas listas.

valores1 = [1,2,3,4,5]
valores2 = [2,4,6,7,1]

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2:
            print(f"O valor {valor1} aparece nas duas listas")

# Dado duas listas, printe uma mensagem dizendo se existe
# algum elemento em comum entre elas ou não.

lista1 = [11, 'xx', False]
lista2 = [True, 'xxx']

elemento_em_comum = False

for valor1 in lista1:
    for valor2 in lista2:
        if valor1 == valor2:
            elemento_em_comum = True

if elemento_em_comum:
    print("existe elemento em comum")

else:
    print("Não existe elementos em comum")