#Exercício: Gerenciador de Tarefas Simples

#Crie um programa que funcione como um gerenciador de tarefas simples. O usuário poderá adicionar tarefas, visualizar todas as tarefas, marcar tarefas como concluídas e excluir tarefas. O programa deve seguir estas instruções:

#Lista e Dicionário para Gerenciamento:

#Utilize uma lista para armazenar as tarefas.
#Cada tarefa será representada por um dicionário com as seguintes chaves:
#"id": Um número único que identifica a tarefa.
#"descrição": A descrição da tarefa.
#"concluída": Um valor booleano (True ou False) indicando se a tarefa foi concluída.

#Funções:

#Adicionar Tarefa: Permita que o usuário adicione uma nova tarefa informando a descrição.
#Visualizar Tarefas: Mostre todas as tarefas, indicando se estão concluídas ou não.
#Concluir Tarefa: Permita que o usuário marque uma tarefa como concluída, utilizando o id da tarefa.
#Excluir Tarefa: Permita que o usuário remova uma tarefa pelo id.

#Estrutura de Repetição e Menu:

#Use um loop para exibir um menu com as opções:

#Adicionar tarefa
#Visualizar tarefas
#Marcar tarefa como concluída
#Excluir tarefa
#Sair

#O programa só deve terminar quando o usuário escolher a opção "Sair".

#Validações e Condicionais:

#Valide as entradas do usuário (por exemplo, se o id fornecido existe antes de concluir ou excluir uma tarefa).
#Caso o usuário tente realizar uma ação inválida (como excluir um id inexistente), exiba uma mensagem de erro.
#Uso de Imports:

#Utilize a biblioteca uuid para gerar um identificador único para cada tarefa. (Dica: uuid.uuid4() pode ser convertido em string para isso.)

#Extras (Opcional):

#Salve as tarefas em um arquivo (como JSON) ao fechar o programa e carregue ao iniciá-lo novamente.
#Adicione uma opção para editar a descrição de uma tarefa.

#Dicas e Importações

#Para usar o uuid, importe com import uuid.
#Utilize a função print() para mostrar o menu de opções.
#Utilize for ou while para exibir a lista de tarefas.
#Para verificar se uma tarefa foi concluída, use if tarefa["concluída"].

import uuid

tarefas = [
    {"id": str(uuid.uuid4()), "descrição": "Escovar os dentes", "concluida": False},
    {"id": str(uuid.uuid4()), "descrição": "Lavar banheiro", "concluida": False},
    {"id": str(uuid.uuid4()), "descrição": "Lavar louça", "concluida": False},
]

def adicionar_tarefa():
    nova_tarefa = {}
    
        
    

adicionar_tarefa()