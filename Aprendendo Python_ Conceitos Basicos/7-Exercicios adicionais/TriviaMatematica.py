#Exercício: Jogo de Trivia Matemática

#Crie um jogo de perguntas e respostas com operações matemáticas simples. O jogo deve funcionar da seguinte maneira:

#Prepare um banco de perguntas:

#Crie uma lista de dicionários, onde cada dicionário representa uma pergunta. Cada dicionário deve conter:
#A pergunta em si ("pergunta").
#A resposta correta ("resposta").
#Um nível de dificuldade ("nivel"), que pode ser "fácil", "médio" ou "difícil".

#Antes de começar o jogo, o jogador deve escolher um nível de dificuldade (fácil, médio, difícil). Apenas perguntas do nível escolhido serão apresentadas.

#O jogo sorteará perguntas aleatórias do nível selecionado. Use o módulo random para isso.

#O jogador deve responder cada pergunta. O programa deve verificar se a resposta está correta:

#Se a resposta estiver correta, exiba uma mensagem positiva e some pontos ao jogador.
#Se a resposta estiver errada, exiba a resposta correta e não some pontos.
#O jogador deve responder a 5 perguntas no total. Use uma estrutura de repetição para controlar isso.

#No final, o programa deve exibir:

#A pontuação total do jogador.
#Uma mensagem personalizada baseada na pontuação (ex.: "Excelente!", "Pode melhorar!", etc.).

#Dicas e Requisitos:

#Use random.choice() para sortear perguntas.
#Crie uma função chamada fazer_pergunta que recebe uma pergunta como argumento e retorna True se o jogador acertar e False se errar.
#Use estrutura condicional para verificar se a resposta está correta.
#Guarde a pontuação em uma variável que será incrementada a cada acerto.

#Extra (opcional):

#Permita que o jogador jogue novamente sem precisar reiniciar o programa.
#Adicione um temporizador usando o módulo time para limitar o tempo de resposta (ex.: 10 segundos por pergunta).


#Mudei um pouco porque achei algumas coisas simplesmente uma pessima implementação 

from unidecode import unidecode
import time

perguntas = [
    {"pergunta": "1 + 10", "resposta": "11", "nivel": "fácil"},
    {"pergunta": "20 + 12", "resposta": "32", "nivel": "fácil"},
    {"pergunta": "19 + 18", "resposta": "37", "nivel": "fácil"},
    {"pergunta": "40 + 21", "resposta": "61", "nivel": "fácil"},
    {"pergunta": "1 x 0", "resposta": "0", "nivel": "fácil"},
    {"pergunta": "5 x 10", "resposta": "50", "nivel": "médio"},
    {"pergunta": "4 x 7", "resposta": "28", "nivel": "médio"},
    {"pergunta": "93 x 0", "resposta": "0", "nivel": "médio"},
    {"pergunta": "20 / 2", "resposta": "10", "nivel": "médio"},
    {"pergunta": "12 x 12", "resposta": "144", "nivel": "médio"},
    {"pergunta": "144 / 12", "resposta": "12", "nivel": "difícil"},
    {"pergunta": "123 x 321", "resposta": "39483", "nivel": "difícil"},
    {"pergunta": "60 x 23", "resposta": "1380", "nivel": "difícil"},
    {"pergunta": "10000000 x 0", "resposta": "0", "nivel": "difícil"},
    {"pergunta": "0 ^ 0", "resposta": "1", "nivel": "difícil"}
]


def fazer_pergunta(perguntas):
    nivel = input("Qual nivel você deseja? (fácil), (médio), (difícil)\n\n")
    pontos = 0

    for dic in perguntas:
        for niveis in dic.keys():
            if unidecode(nivel) == unidecode(dic[niveis]):
                for pergunta in dic.keys():
                    if pergunta == "pergunta":
                        pergunta = dic[pergunta] 
                        for respostas in dic.keys(): 
                            if respostas == "resposta":
                                respostas = dic[respostas]
                                inicio = time.time()
                                resposta = input(f"Qual o resultado de {pergunta}:\n")
                                fim = time.time()
                                
                                if fim - inicio > 20:
                                    print("Se passaram 20 segundos, o tempo acabou")
                                
                                elif respostas == resposta:
                                    print("Parabens você acertou!")
                                    pontos += 1

                                else: 
                                    print("Você errou!")
                                    print(f"O resultado correto seria {respostas}")
                                
    if pontos == 5:
        print("Excelente!")
        print(f"Você acertou {pontos}")
                                
    elif pontos >= 3:
        print("Bom!")
        print(f"Você acertou {pontos}")
                                
    elif pontos >= 1:
        print("Ruim! Da para melhorar!")
        print(f"Você acertou {pontos}")
                                
    else:
        print("Pessimo!!!, Você é HORROROSO!!!")
        print("Tirou ZEROO!!!")

    return perguntas

fazer_pergunta(perguntas)