# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 20



for n in range(1,4):

    numero = int(input('Digite um numero: '))

    if numero == numero_secreto:
        print(f'Parabens voce acertou, era o numero {numero}')
        break

    if numero <= numero_secreto:
        print('O numero é mais alto')

    if numero >= numero_secreto:
        print('O numero é mais baixo')

else:
    print(f'Era o numero {numero_secreto}')
    