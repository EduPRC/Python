#Exercício: Jogo da Adivinhação com Recursos Extras

#Objetivo:
#Criar um jogo de adivinhação onde o jogador tenta adivinhar uma palavra escolhida aleatoriamente de uma lista. O programa deve usar estruturas condicionais, estruturas de repetição, funções, dicionários, listas, e importar bibliotecas.

#Requisitos do Jogo:
#Lista de palavras: Crie uma lista com pelo menos 5 palavras diferentes.

#Dicionário com dicas: Cada palavra na lista deve ter uma dica associada em um dicionário.
#Exemplo: {'banana': 'É uma fruta amarela.', 'python': 'Linguagem de programação.'}

#Escolha aleatória da palavra: Use o módulo random para escolher uma palavra aleatoriamente.

#Sistema de tentativas:
#O jogador terá um número limitado de tentativas (ex.: 5 tentativas).
#Cada erro diminui o número de tentativas.

#Verificação de vitória:
#O jogador vence se acertar a palavra antes de esgotar as tentativas.
#Caso contrário, o programa exibe a mensagem de derrota e revela a palavra correta.

#Mostrar progresso:
#Mostre o progresso do jogador usando uma lista para exibir as letras descobertas até o momento (como no estilo de "Forca").
#Exemplo: Para a palavra "python", se o jogador acertar "p" e "o", mostre algo como: p _ _ _ o _.

#Entrada do jogador:
#Permita que o jogador digite uma letra ou tente adivinhar a palavra inteira.
#Diferencie maiúsculas e minúsculas.

#Estrutura do Código (sugestão):
#Imports necessários:
#Use o módulo random para sortear uma palavra da lista.

#Funções principais:

#Uma função para escolher a palavra e fornecer a dica correspondente.
#Uma função para verificar se o jogador acertou ou errou.
#Uma função para atualizar o progresso (as letras já adivinhadas).
#Uma função para exibir o estado atual do jogo.

#Dicas:

#Use o método .lower() para normalizar as entradas do jogador.
#Use loops while ou for para controlar o fluxo de tentativas.
#Trabalhe com índices para atualizar o progresso do jogador na palavra.

#Exemplo de Fluxo do Jogo:
#O jogo escolhe aleatoriamente a palavra "python" com a dica: "Linguagem de programação."
#O jogador recebe: Progresso: _ _ _ _ _ _ | Dica: Linguagem de programação.
#O jogador digita a letra "p".
#O jogo responde: Acertou! Progresso: p _ _ _ _ _ | Tentativas restantes: 4
#O jogador tenta a palavra inteira: "java".
#O jogo responde: Errou! Tentativas restantes: 3
#O jogador tenta "python".
#O jogo responde: Parabéns! Você acertou!

import random
from unidecode import unidecode

palavras = [
    'python', 'banana', 'munstang', 'VScode', 'java', 
    'pizza', 'caneta', 'guitarra', 'paris', 'tigre',
    'oceano', 'galaxia', 'montanha', 'astronauta', 'diamante',
    'café', 'helicoptero', 'esmeralda', 'cachoeira', 'satelite',
    'leopardo', 'microfone', 'floresta', 'neve', 'canguru'
]

dicas = {
    'python': 'Linguagem de programação',
    'banana': 'Fruta amarela',
    'munstang': 'Carro',
    'VScode': 'IDE',
    'java': 'Linguagem de programação',
    'pizza': 'Comida italiana redonda',
    'caneta': 'Objeto para escrever',
    'guitarra': 'Instrumento musical de cordas',
    'paris': 'Capital da França',
    'tigre': 'Felino listrado',
    'oceano': 'Grande corpo de água salgada',
    'galaxia': 'Conjunto de estrelas e planetas',
    'montanha': 'Grande elevação natural do terreno',
    'astronauta': 'Pessoa que viaja para o espaço',
    'diamante': 'Pedra preciosa e brilhante',
    'café': 'Bebida feita de grãos torrados',
    'helicoptero': 'Veículo aéreo com hélices',
    'esmeralda': 'Pedra preciosa verde',
    'cachoeira': 'Queda de água',
    'satelite': 'Objeto que orbita um planeta',
    'leopardo': 'Felino com pintas',
    'microfone': 'Dispositivo para amplificar som',
    'floresta': 'Área com muitas árvores',
    'neve': 'Precipitação branca e fria',
    'canguru': 'Animal marsupial da Austrália'
}


def escolher_palavra():
    aleatorio = random.choice(palavras)
    for palavra in dicas.keys():
        if aleatorio == palavra:
            dica = dicas[palavra]
            lista = list(aleatorio)
            for i in range(len(lista)):
                lista[i] = '_ '
            print(f'Progresso: {"".join(lista)}| Dica: {dica}')
    
    return aleatorio


def acao(aleatorio, tentativas=4):
    executou = False
    letras_corretas = []
    for i in range(tentativas,-1,-1):
        resposta = input("Digite uma letra ou a palavra: ")
        indice = unidecode(aleatorio).lower().find(unidecode(resposta).lower()) 
        
            
        if unidecode(aleatorio).lower() == unidecode(resposta).lower():
            print(f"Parabéns! Você acertou!")
            break
            
        elif indice > -1:
            lista = list(aleatorio)
            if executou == False:
                for _ in range(len(lista)):
                    letras_corretas.append('_ ')
                    executou = True
            for j in range(len(aleatorio)):
                if unidecode(aleatorio[j]) == unidecode(resposta):
                    letras_corretas.pop(j)
                    letras_corretas.insert(j, resposta)
    
                       
            print(f"Acertou! Progresso: {"".join(letras_corretas)}| Tentativas restantes: {i}")
            
        else:
            print(f"Errou! Tentativas restantes: {i}")
    if resposta != aleatorio:        
        print(f"A palavra era {aleatorio}")

decisao = input('Deseja jogar? s ou n\n')   
while decisao == 's':
    aleatorio = escolher_palavra()
    acao(aleatorio)
    decisao = input('\nDeseja continuar a jogar? s ou n\n')