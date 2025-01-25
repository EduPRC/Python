# Desafio - crie um programa que:
# - Pede pelo seu nome e idade
# - Dá oi para você
# - Conta quantas letras seu nome possui
# - Fala quantos anos você terá daqui a 5 anos

nome = input("Qual é o seu nome: ")
idade = int(input("Qual é sua idade: "))

print(f"Olá, {nome}")

quantidade_letras = len(nome)

print(f"A quantidade de letras é: {quantidade_letras}")

idade_somada = idade + 5

print(f"Voce tera: {idade_somada} daqui a 5 anos")