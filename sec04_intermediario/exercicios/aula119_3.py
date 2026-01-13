# Use Json para criar uma base de dados da lista de tarefas

import os
import json

# Pega o caminho absoluto da pasta onde ESTE script (.py) está
DIR_PATH = os.path.dirname(__file__)

FILE_PATH = os.path.join(DIR_PATH, 'aula119.json')


def load_list():
    try:
        with open(FILE_PATH, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save(task_list):
    with open(FILE_PATH, 'w', encoding='utf-8') as file:
        json.dump(
            task_list,
            file,
            indent=2,
            ensure_ascii=False
        )


def show_tasks(tasks):
    print()
    if not tasks:
        print('Nenhuma tarefa para listar.')
        return

    print('Tarefas:')
    for i, task in enumerate(tasks, start=1):
        print(f'\t{i}. {task}')
    print()


def add_task(task, tasks, redo_stack):
    if not task.strip():
        print('\nVocê não digitou uma tarefa.')
        return

    tasks.append(task)
    save(tasks)
    redo_stack.clear()
    show_tasks(tasks)


def undo(tasks, redo_stack):
    if not tasks:
        print('\nNenhuma tarefa para desfazer')
        return

    task = tasks.pop()
    save(tasks)
    redo_stack.append(task)
    show_tasks(tasks)


def redo(tasks, redo_stack):
    if not redo_stack:
        print('\nNenhuma tarefa para refazer.')
        return

    task = redo_stack.pop()
    tasks.append(task)
    save(tasks)
    show_tasks(tasks)


if __name__ == '__main__':
    task_list = load_list()
    redo_stack = []
    while True:
        print('Comandos: listar, desfazer, refazer, clear')
        user_input = input('Digite uma tarefa ou comando: ')

        commands = {
            # lambda para adiar a execução da função
            'listar': lambda: show_tasks(task_list),
            'desfazer': lambda: undo(task_list, redo_stack),
            'refazer': lambda: redo(task_list, redo_stack),
            'clear': lambda: os.system('clear'),
            'adicionar': lambda: add_task(user_input, task_list, redo_stack),
        }

        # Pega o comando. Se não for comando, usa 'adicionar' como padrão
        action = commands.get(user_input, commands['adicionar'])

        action()


# "Resposta"

# def listar(tarefas):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para listar')
#         return

#     print('Tarefas:')
#     for tarefa in tarefas:
#         print(f'\t{tarefa}')
#     print()


# def desfazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas:
#         print('Nenhuma tarefa para desfazer')
#         return

#     tarefa = tarefas.pop()
#     print(f'{tarefa=} removida da lista de tarefas.')
#     tarefas_refazer.append(tarefa)
#     print()
#     listar(tarefas)


# def refazer(tarefas, tarefas_refazer):
#     print()
#     if not tarefas_refazer:
#         print('Nenhuma tarefa para refazer')
#         return

#     tarefa = tarefas_refazer.pop()
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# def adicionar(tarefa, tarefas):
#     print()
#     tarefa = tarefa.strip()
#     if not tarefa:
#         print('Você não digitou uma tarefa.')
#         return
#     print(f'{tarefa=} adicionada na lista de tarefas.')
#     tarefas.append(tarefa)
#     print()
#     listar(tarefas)


# def ler(tarefas, caminho_arquivo):
#     dados = []
#     try:
#         with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
#             dados = json.load(arquivo)
#     except FileNotFoundError:
#         print('Arquivo não existe')
#         salvar(tarefas, caminho_arquivo)
#     return dados


# def salvar(tarefas, caminho_arquivo):
#     dados = tarefas
#     with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
#         dados = json.dump(tarefas, arquivo, indent=2, ensure_ascii=False)
#     return dados


# CAMINHO_ARQUIVO = 'aula119.json'
# tarefas = ler([], CAMINHO_ARQUIVO)
# tarefas_refazer = []

# while True:
#     print('Comandos: listar, desfazer e refazer')
#     tarefa = input('Digite uma tarefa ou comando: ')

#     comandos = {
#         'listar': lambda: listar(tarefas),
#         'desfazer': lambda: desfazer(tarefas, tarefas_refazer),
#         'refazer': lambda: refazer(tarefas, tarefas_refazer),
#         'clear': lambda: os.system('clear'),
#         'adicionar': lambda: adicionar(tarefa, tarefas),
#     }
#     comando = comandos.get(tarefa) if comandos.get(tarefa) is not None else \
#         comandos['adicionar']
#     comando()
#     salvar(tarefas, CAMINHO_ARQUIVO)
