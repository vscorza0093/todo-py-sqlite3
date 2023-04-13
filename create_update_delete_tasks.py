import main
from datetime import datetime
import sqlite3


def GetNewTaskData():
    print("Enter task name:")
    task_name = input().rstrip()
    if len(task_name) > 100:
        print("The name you entered is too long")
        GetNewTaskData()
    else:
        CheckIfTaskNameIsAvailable(task_name)


def CheckIfTaskNameIsAvailable(task_name):
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT task_name FROM tasks''')
    name_query = cursor.fetchall()

    if len(task_name) < 3:
        print("Entered name is too short")

    for data in name_query:
        if str(task_name) == str(data[0]):
            print("Task name is not available\n")
            GetNewTaskData()

    CreateTask(GetNewId(), task_name)


def CreateTask(id, task_name):
    data_atual = datetime.now()
    data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("\nEnter task description")
    task_description = input()
    print("\nEnter task status")
    status = input()
    cursor.execute('''INSERT INTO tasks (id, task_name, creation_date, description, status) 
                        VALUES (?, ?, ?, ?, ?)''', (id, task_name, data_formatada, task_description, status))
    conexao.commit()
    conexao.close()
    main.ApplicationTitle()
    main.ApplicationLoop()


def GetNewId():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT id FROM tasks ORDER BY id DESC''')
    id_result = cursor.fetchall()
    return id_result[0][0] + 1


def UpdateTaskByIdOrByName():
    print("\nI - Update by Id\nN - Update by Name\nC - Cancel")
    id_or_name_input = input().lower().rstrip()
    match id_or_name_input:
        case 'c':
            main.ApplicationTitle()
            main.ApplicationLoop()
        case 'i':
            UpdateTaskById()
        case 'n':
            UpdateTaskByName()
        case other:
            print("Invalid input")
            UpdateTaskByIdOrByName()


def UpdateTaskById():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("Type a Id to update the task")
    user_input = input().rstrip()
    print('\n')
    try:
        int(user_input)
    except ValueError:
        print("Invalid input, it must be a integer")
        UpdateTaskById()

    print("Enter task name")
    task_name = input()
    print("\nEnter task description")
    task_description = input()
    print("\nEnter task status")
    task_status = input()

    cursor.execute(f'''UPDATE tasks SET task_name = \'{task_name}\',
                                        description = \'{task_description}\',
                                        status = \'{task_status}\'
                    WHERE id = {user_input}''')
    conexao.commit()
    conexao.close()
    print(f"Task {task_name} updated")
    main.ApplicationTitle()
    main.ApplicationLoop()


def UpdateTaskByName():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("Type a Task Name to update the task")
    user_input = input().rstrip()
    print('\n')

    print("Enter task name")
    task_name = input()
    print("\nEnter task description")
    task_description = input()
    print("\nEnter task status")
    task_status = input()

    cursor.execute(f'''UPDATE tasks SET task_name = \'{task_name}\',
                                        description = \'{task_description}\',
                                        status = \'{task_status}\'
                    WHERE task_name = \'{user_input}\'''')
    conexao.commit()
    conexao.close()
    print(f"Task {task_name} updated")
    main.ApplicationTitle()
    main.ApplicationLoop()


def DeleteTaskByIdOrByName():
    print("I - Delete by Id\nN - Delete by Name\nC - Cancel")
    id_or_name_input = input().lower().rstrip()
    match id_or_name_input:
        case 'c':
            main.ApplicationTitle()
            main.ApplicationLoop()
        case 'i':
            DeleteTaskById()
        case 'n':
            DeleteTaskByName()
        case other:
            print("Invalid input")


def DeleteTaskById():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("\nType a Id to remove the task from table")
    user_input = input().rstrip()
    print('\n')
    try:
        int(user_input)
    except ValueError:
        print("Invalid input, it must be a integer")
        DeleteTaskById()
    cursor.execute(f'''DELETE FROM tasks WHERE id = {user_input}''')
    conexao.commit()
    conexao.close()
    main.ApplicationTitle()
    main.ApplicationLoop()


def DeleteTaskByName():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("\nType a Task Name to remove the task from table")
    user_input = input().rstrip()
    print('\n')
    cursor.execute(f'''DELETE FROM tasks WHERE task_name = \'{user_input}\'''')
    conexao.commit()
    conexao.close()
    main.ApplicationTitle()
    main.ApplicationLoop()
