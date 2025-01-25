# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder
# o nome da capital de cada Estado do Brasil. O jogo deve perguntar
# ao usuário "Qual a capital do Estado X?", e checar se o usuário
# respondeu de forma correta. Após cada pergunta, o usuário pode escolher
# parar o jogo ou continuar para a próxima pergunta. Quando o usuário
# decidir parar, ou quando todas as perguntas forem respondidas,
# o código mostra o número bruto e porcentagem de acertos.

from unidecode import unidecode

capitais = {
    "Acre": "Rio Branco",
    "Alagoas": "Maceió",
    "Amapá": "Macapá",
    "Amazonas": "Manaus",
    "Bahia": "Salvador",
    "Ceará": "Fortaleza",
    "Distrito Federal": "Brasília",
    "Espírito Santo": "Vitória",
    "Goiás": "Goiânia",
    "Maranhão": "São Luís",
    "Mato Grosso": "Cuiabá",
    "Mato Grosso do Sul": "Campo Grande",
    "Minas Gerais": "Belo Horizonte",
    "Pará": "Belém",
    "Paraíba": "João Pessoa",
    "Paraná": "Curitiba",
    "Pernambuco": "Recife",
    "Piauí": "Teresina",
    "Rio de Janeiro": "Rio de Janeiro",
    "Rio Grande do Norte": "Natal",
    "Rio Grande do Sul": "Porto Alegre",
    "Rondônia": "Porto Velho",
    "Roraima": "Boa Vista",
    "Santa Catarina": "Florianópolis",
    "São Paulo": "São Paulo",
    "Sergipe": "Aracaju",
    "Tocantins": "Palmas"
}

rodadas = 0
quantidade_acertos = 0
for estado in capitais:
    capital = capitais[estado]
    resposta = input(f"Qual a capital do estado {estado}? \n")
    
           
    if unidecode(resposta).lower() == unidecode(capital).lower():
        print("Resposta Correta")
        rodadas += 1
        quantidade_acertos += 1
        decisao = input("Deseja parar o jogo? digite 'sair' para sair e qualquer letra para continuar \n")
        if decisao == "sair":
            print("Voce saiu!")
            break
        else:
            continue
                    
    if unidecode(resposta).lower() != unidecode(capital).lower():
        print("Resposta incorreta!")
        rodadas += 1
        decisao = input("Deseja parar o jogo? digite 'sair' para sair e qualquer letra para continuar \n")
        if decisao == "sair":
            print("Voce saiu!\n")
            break
        else:
            continue

print("O jogo acabou!!!")
print(f"Quantidade de acertos: {quantidade_acertos}/{rodadas}")
porcentagem = quantidade_acertos / rodadas * 100
print(f"A porcentagem dos acertos é {round(porcentagem)}%")           