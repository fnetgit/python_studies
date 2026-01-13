# Guard Clause
# (Cláusula de Guarda): É a verificação feita no início da função (if not ...)
# para barrar casos inválidos imediatamente com 'return'.
# Isso elimina a necessidade de usar 'else', deixando o código mais limpo (sem indentação excessiva).

import os


def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return

    print('Tarefas:')
    for i, tarefa in enumerate(tarefas, start=1):
        print(f'\t{i}. {tarefa}')
    print()


def desfazer(tarefas, tarefas_refazer):
    if not tarefas:
        print('\nNenhuma tarefa para desfazer')
        return

    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
    listar(tarefas)


def refazer(tarefas, tarefas_refazer):
    if not tarefas_refazer:
        print('\nNenhuma tarefa para refazer')
        return

    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
    listar(tarefas)


def adicionar(tarefa, tarefas, tarefas_refazer):
    if not tarefa.strip():
        print('\nVocê não digitou uma tarefa.')
        return

    tarefas.append(tarefa)
    tarefas_refazer.clear()
    listar(tarefas)


tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer, refazer, clear')
    comando_usuario = input('Digite uma tarefa ou comando: ')

    # Dicionário de comandos (Dispatch Table)
    comandos = {
        'listar': lambda: listar(tarefas),
        'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
        'refazer': lambda: refazer(tarefas, tarefas_refazer),
        'clear': lambda: os.system('clear'),
        'adicionar': lambda: adicionar(comando_usuario, tarefas, tarefas_refazer),
    }

    # Tenta pegar o comando. Se não existir (é None), executa 'adicionar'
    funcao = comandos.get(comando_usuario, comandos['adicionar'])

    funcao()
