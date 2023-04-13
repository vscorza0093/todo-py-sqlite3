import main
import sqlite3


def GetNewCategoryData():
    print("Insert category name:")
    category_name = input().rstrip()
    if len(category_name) > 100:
        print("The name you entered is too long")
        GetNewCategoryData()
    else:
        CheckIfCategoryNameIsAvailable(category_name)


def CheckIfCategoryNameIsAvailable(category_name):
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT category_name FROM category''')
    name_query = cursor.fetchall()

    if len(category_name) < 3:
        print("Entered name is too short")

    for data in name_query:
        if str(category_name) == str(data[0]):
            print("Category name is not available\n")
            GetNewCategoryData()

    CreateCategory(GetNewId(), category_name)


def CreateCategory(id, category_name):
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''INSERT INTO category (id, category_name) VALUES (?, ?)''', (id, category_name))
    conexao.commit()
    print(f"Category {category_name}, id {id} created")
    conexao.close()
    print('\n')
    main.ApplicationTitle()
    main.ApplicationLoop()


def GetNewId():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT id FROM category ORDER BY id DESC''')
    id_result = cursor.fetchall()
    return id_result[0][0] + 1


def UpdateCategory():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    cursor.execute('''SELECT category_name FROM category''')
    print("Enter the current Category Name")
    current_name = input().rstrip()
    print("Enter the new Category Name")
    new_name = input().rstrip()
    name_query = cursor.fetchall()

    for data in name_query:
        print(data)
        if str(new_name) == str(data[0]):
            print("Category name is not available\n")
            UpdateCategory()
            return

    cursor.execute(f'''UPDATE category SET category_name = \'{new_name}\' 
                        WHERE category_name = \'{current_name}\'''')
    conexao.commit()
    conexao.close()
    print(f"Category {new_name} updated")
    main.ApplicationTitle()
    main.ApplicationLoop()


def DeleteByIdOrByName():
    print("\nI - Delete by Id\nN - Delete by Name\nC - Cancel")
    id_or_name_input = input().lower().rstrip()
    match id_or_name_input:
        case 'c':
            main.ApplicationTitle()
            main.ApplicationLoop()
        case 'i':
            DeleteCategoryById()
        case 'n':
            DeleteCategoryByName()
        case other:
            print("Invalid input")
            DeleteByIdOrByName()


def DeleteCategoryById():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("Type a Id to remove category from table")
    user_input = input().rstrip()
    print('\n')
    try:
        int(user_input)
    except ValueError:
        print("Invalid input, it must be a integer")
        DeleteCategoryById()
    cursor.execute(f'''DELETE FROM category WHERE id = {user_input}''')
    conexao.commit()
    conexao.close()
    print(f"Category {user_input} deleted")
    main.ApplicationTitle()
    main.ApplicationLoop()


def DeleteCategoryByName():
    conexao = sqlite3.connect("todotasks.sqlite3")
    cursor = conexao.cursor()
    print("Type a Category Name to remove category from table")
    user_input = input().rstrip()
    print('\n')
    cursor.execute(f'''DELETE FROM category WHERE category_name = \'{user_input}\'''')
    conexao.commit()
    conexao.close()
    print(f"Category {user_input} deleted")
    main.ApplicationTitle()
    main.ApplicationLoop()

