import main
import sqlite3


def ConcludeByIdOrByName():
    print("\nI - Conclude by Id\nN - Conclude by Name\nC - Cancel")
    id_or_name_input = input().lower().rstrip()
    match id_or_name_input:
        case 'c':
            main.ApplicationTitle()
            main.ApplicationLoop()
        case 'i':
            ConcludeTaskById()
        case 'n':
            ConcludeTaskByName()
        case other:
            print("Invalid input")
            ConcludeByIdOrByName()


def ConcludeTaskById():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("Type a Id to mark the task as concluded")
    user_input = input().rstrip()
    print('\n')
    try:
        int(user_input)
    except ValueError:
        print("Invalid input, it must be a integer")
        ConcludeTaskById()
    cursor.execute('''SELECT status FROM tasks''')
    cursor.execute(f'''UPDATE tasks SET status = \'concluido\' 
                        WHERE id = {user_input}''')
    conexao.commit()
    conexao.close()
    print(f"Task marked as concluded")
    main.ApplicationTitle()
    main.ApplicationLoop()


def ConcludeTaskByName():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT status FROM tasks''')
    print("Type a Task Name to mark as concluded")
    user_input = input().rstrip()
    print('\n')
    cursor.execute(f'''UPDATE tasks SET status = \'concluido\' 
                        WHERE task_name = \'{user_input}\'''')
    conexao.commit()
    conexao.close()
    print(f"Task {user_input} marked as concluded")
    main.ApplicationTitle()
    main.ApplicationLoop()
