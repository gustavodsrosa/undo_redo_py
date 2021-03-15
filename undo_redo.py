'''
Adicionar tarefa
Listar Tarefas
Desfazer
Refazer
'''

pilha = []


def adicionar_tarefa(tarefa):
    pilha.append(tarefa)


def listar_tarefas():
    if len(pilha) == 0:
        return "Você precisa adicionar uma tarefa!"
    return f"As tarefas são: {pilha}"


while True:
    print()
    print("=-=-=- UNDO / REDO =-=-=-")
    print()
    print("[1] - Adicionar tarefa")
    print("[2] - Listar tarefas")
    print("[3] - Desfazer / Refazer")

    escolhendo = int(input("O que deseja fazer? "))

    if escolhendo == 1:
        tarefa = str(input("Digite uma tarefa para incuir: "))
        adicionar_tarefa(tarefa)
    elif escolhendo == 2:
        print()
        print(listar_tarefas())
    elif escolhendo == 3:
        print()
        print('[1] - Desfazer')
        print('[2] - Refazer')
        resposta = int(input("O que deseja fazer? "))

        if resposta == 1:
            elemento = pilha[-1]
            pilha.pop(-1)
        elif resposta == 2:
            pilha.append(elemento)
        else:
            print("Digite algo válido!")
    else:
        print("Digite algo válido!")
