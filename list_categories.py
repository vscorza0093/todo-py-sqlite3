import main
import sqlite3


def ListAllCategories():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT * FROM category''')
    result = cursor.fetchall()
    print('id, ' + '\'categoria\'\n')
    for data in result:
        print(data)
    conexao.close()
    print("\n")
    main.ApplicationTitle()
    main.ApplicationLoop()