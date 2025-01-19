# Crie um código que implementa a "Cifra de César", isto é, que
# transforma um string movendo cada letra um certo número de
# passos no alfabeto. O número de passos é dado por uma chave.
# Letra com acentos, espaços e pontuação permanecem iguais.

# Exemplos:
# "abc" com chave 1 = "bcd"
# "ABCDE" com chave 2 = "CDEFG"
# "Cachorro" com chave -1 = "Bzbgnqqn"
# "Olá Mundo!" com chave 3 = "Roá Pxqgr!"

# DICA: construa 2 strings com as letras do alfabeto em ordem,
# um para letra minúsculas e outra para as maiúsculas, e use este
# string para guiar as substituições.

alfabetoMaiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alfabetoMinusculo = "abcdefghijklmnopqrstuvwxyz"

texto = input("Escreva um texto: ")
chave = int(input("Escreva a chave: "))

lista = []

for letra in texto:
                
        if letra in alfabetoMaiusculo:
            indice = alfabetoMaiusculo.index(letra)
            indice = indice + chave
            while indice >= len(alfabetoMaiusculo):
                indice = indice - len(alfabetoMaiusculo)
            resultado = alfabetoMaiusculo[indice]
            lista.append(resultado)
                  
        elif letra in alfabetoMinusculo:
            indice = alfabetoMinusculo.index(letra)
            indice = indice + chave
            while indice >= len(alfabetoMinusculo):
                indice = indice - len(alfabetoMinusculo)
            resultado = alfabetoMinusculo[indice]
            lista.append(resultado)
            
        else:
            resultado = letra
            lista.append(resultado)
                   
print(''.join(lista))
    
        
    