import sqlite3
from datetime import datetime

conexao = sqlite3.connect("todotasks.sqlite3")
cursor = conexao.cursor()
cursor.execute('''INSERT INTO category (id, category_name) VALUES (?, ?)''', (1, 'adm'))
data_atual = datetime.now()
data_cadastro = data_atual.strftime("%d/%m/%Y %H:%M:%S")
cursor.execute('''INSERT INTO tasks (id, task_name, creation_date, description, status)
                    VALUES (?, ?, ?, ?, ?)''', (1, 'a fazer', data_cadastro,
                                                'tarefas que estão em aberto', 'em aberto'))
conexao.commit()
conexao.close()