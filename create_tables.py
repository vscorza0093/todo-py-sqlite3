import sqlite3

conexao = sqlite3.connect("todotasks.sqlite3")
cursor = conexao.cursor()

to_do_table = ''' CREATE TABLE tasks 
                    (id INTEGER PRIMARY KEY,
                    task_name VARCHAR(100) NOT NULL,
                    creation_date VARCHAR(10) NOT NULL,
                    description VARCHAR(500),
                    status VARCHAR(10) NOT NULL              
                    );
'''

category_table = ''' CREATE TABLE category
                        (id INTEGER PRIMARY KEY,
                        category_name TEXT (100) NOT NULL
                        );
'''

cursor.execute(to_do_table)
cursor.execute(category_table)
conexao.commit()
conexao.close()
