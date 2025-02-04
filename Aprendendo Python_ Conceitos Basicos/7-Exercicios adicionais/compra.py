precos = {'coca': 12, 'fanta': 10, 'cotuba': 9}

dudu = int(input("Quanto de dinheiro dudu tem? "))
hugo = int(input("Quanto de dinheiro hugo tem? "))

soma = dudu + hugo

soma_total = sum(precos.values())
for preco in precos:
    if soma >= soma_total:
        print(f"Da para comprar todos os refrigerantes pelos seus respectivos preços")
        break
    if soma >= precos[preco]:
        print(f'Da para comprar {preco} por {precos[preco]}')