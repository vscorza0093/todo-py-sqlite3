import main
import sqlite3


def ListAllTasks():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM tasks''')
    result = cursor.fetchall()
    print(f'id,  task name,     creation date,           description,              status\n')
    for data in result:
        print(data)
    conexao.close()
    print("\n")
    main.ApplicationTitle()
    main.ApplicationLoop()