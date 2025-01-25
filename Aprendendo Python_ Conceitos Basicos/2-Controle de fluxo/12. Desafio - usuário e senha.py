# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como
# variávies dentro do próprio código.

usuarioc = 'Eduardo'
senhac = '1234'

usuario = input('Digite o usuario: ')
senha = input('Digite a senha: ')

if usuario == usuarioc and senha == senhac:
    print('Login bem sucedido!')
    print(f'Seja bem vindo {usuario}')

if usuario != usuarioc:
    print('Usuario incorreto ou não existe')

if senha != senhac:
    print('Senha incorreta')