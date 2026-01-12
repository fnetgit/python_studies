# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os

todo_list = []
stack = []


def print_tasks():
    if not todo_list:
        print('Lista de tarefas vazia.')
    else:
        print('TAREFAS:')
        for i, tarefa in enumerate(todo_list, start=1):
            print(f'\t{i}. {tarefa}')


def clear():
    os.system('clear')


def add_task(task):
    todo_list.append(task)
    stack.clear()
    print_tasks()


def undo():
    if not todo_list:
        print('Nada para desfazer.')
        return

    undoded = todo_list.pop()
    stack.append(undoded)
    print_tasks()


def redo():
    if not stack:
        print('Nada para refazer.')
        return

    item = stack.pop()
    todo_list.append(item)
    print_tasks()


def manage_tasks(command):
    if command == "listar":
        print_tasks()
    elif command == "desfazer":
        undo()
    elif command == "refazer":
        redo()
    elif command == 'clear':
        clear()
    else:
        add_task(command)


while True:
    print('\nComandos: listar, desfazer, refazer, clear')
    user_input = input('Digite uma tarefa ou comando: ').strip()
    if not user_input:
        continue
    manage_tasks(user_input)
